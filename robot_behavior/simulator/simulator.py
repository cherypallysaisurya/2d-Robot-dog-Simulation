import tkinter as tk
from ..core.robot import Robot, Direction
from typing import List, Tuple
import time
import os

# Optional PIL import for dog image support
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

class RobotSimulator:
    def __init__(self, width: int = 10, height: int = 10, cell_size: int = 50, random_robot: bool = False):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.walls = set()
        self.robot = Robot(simulator=self, random_start=random_robot)  # Pass random_start parameter
        self.robot_trace: List[Tuple[int, int]] = []  # Track robot movement path
        
        # Animation variables
        self.robot_display_x = 0.0  # Smooth position for display
        self.robot_display_y = 0.0
        self.is_animating = False
        
        # Create main window FIRST (required for PhotoImage)
        self.root = tk.Tk()
        self.root.title("Robot Behavior Simulator")
        
        # Load dog image AFTER root window is created
        self.dog_image = None
        self._load_dog_image()
        
        # Create canvas
        canvas_width = width * cell_size
        canvas_height = height * cell_size
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack()
        
        # Draw grid
        self._draw_grid()
        
        # Initialize display position to robot's actual position
        robot_pos = self.robot.get_position()
        self.robot_display_x = float(robot_pos[0])
        self.robot_display_y = float(robot_pos[1])
        
        # Add initial position to trace
        self.robot_trace.append(self.robot.get_position())
        
        # Initial robot drawing
        self._draw_robot()

    def _load_dog_image(self):
        """Load the dog PNG image for the robot."""
        if not PIL_AVAILABLE:
            print("ℹ️ Pillow not installed. Using default triangle.")
            print("   Install with: pip install Pillow")
            self.dog_image = None
            self.dog_images = {}
            return
            
        try:
            # Try to find the dog image in various locations
            possible_paths = [
                os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'dog.png'),
                os.path.join(os.getcwd(), 'assets', 'dog.png'),
                'assets/dog.png',
                'dog.png'
            ]
            
            self.dog_images = {}  # Store rotated versions
            
            for path in possible_paths:
                if os.path.exists(path):
                    # Load and resize the image to fit in the cell
                    pil_image = Image.open(path)
                    # Resize to 80% of cell size
                    size = int(self.cell_size * 0.8)
                    pil_image = pil_image.resize((size, size), Image.Resampling.LANCZOS)
                    
                    # Create rotated versions for each direction
                    # Assuming original image faces NORTH (up)
                    self.dog_images[Direction.NORTH] = ImageTk.PhotoImage(pil_image)  # 0° rotation
                    self.dog_images[Direction.EAST] = ImageTk.PhotoImage(pil_image.rotate(-90, expand=True))  # 90° clockwise
                    self.dog_images[Direction.SOUTH] = ImageTk.PhotoImage(pil_image.rotate(180, expand=True))  # 180°
                    self.dog_images[Direction.WEST] = ImageTk.PhotoImage(pil_image.rotate(90, expand=True))   # 90° counter-clockwise
                    
                    self.dog_image = self.dog_images[Direction.NORTH]  # Default image
                    print(f"✅ Dog image loaded and rotated from: {path}")
                    return
            
            print("ℹ️ Dog image not found. Using default triangle.")
            print("   Place dog.png in assets/ folder to use custom image.")
            self.dog_image = None
            self.dog_images = {}
            
        except Exception as e:
            print(f"⚠️ Error loading dog image: {e}")
            self.dog_image = None
            self.dog_images = {}
    
    def _draw_grid(self):
        """Draw the grid on the canvas."""
        # Draw vertical lines
        for i in range(self.width + 1):
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, self.height * self.cell_size, fill="gray", width=1)
            
        # Draw horizontal lines
        for i in range(self.height + 1):
            y = i * self.cell_size
            self.canvas.create_line(0, y, self.width * self.cell_size, y, fill="gray", width=1)
    
    def _draw_robot(self):
        """Draw the robot (dog) on the canvas using smooth display position."""
        direction = self.robot.get_direction()
        
        # Use smooth display position instead of grid position
        # Calculate center of cell (note: y-axis is flipped in Tkinter)
        center_x = (self.robot_display_x + 0.5) * self.cell_size
        center_y = ((self.height - 1 - self.robot_display_y) + 0.5) * self.cell_size
        
        self.canvas.delete("robot")  # Remove previous robot drawing
        
        if hasattr(self, 'dog_images') and self.dog_images and direction in self.dog_images:
            # Use rotated dog PNG image based on direction
            rotated_dog_image = self.dog_images[direction]
            self.canvas.create_image(
                center_x, center_y, 
                image=rotated_dog_image, 
                tags="robot"
            )
            
        elif hasattr(self, 'dog_image') and self.dog_image:
            # Fallback: use original dog image with arrow indicator
            self.canvas.create_image(
                center_x, center_y, 
                image=self.dog_image, 
                tags="robot"
            )
            
            # Add direction indicator (small arrow) as fallback
            arrow_size = self.cell_size * 0.2
            if direction == Direction.NORTH:
                arrow_points = [
                    center_x, center_y - self.cell_size * 0.45,
                    center_x - arrow_size/2, center_y - self.cell_size * 0.3,
                    center_x + arrow_size/2, center_y - self.cell_size * 0.3
                ]
            elif direction == Direction.EAST:
                arrow_points = [
                    center_x + self.cell_size * 0.45, center_y,
                    center_x + self.cell_size * 0.3, center_y - arrow_size/2,
                    center_x + self.cell_size * 0.3, center_y + arrow_size/2
                ]
            elif direction == Direction.SOUTH:
                arrow_points = [
                    center_x, center_y + self.cell_size * 0.45,
                    center_x - arrow_size/2, center_y + self.cell_size * 0.3,
                    center_x + arrow_size/2, center_y + self.cell_size * 0.3
                ]
            else:  # WEST
                arrow_points = [
                    center_x - self.cell_size * 0.45, center_y,
                    center_x - self.cell_size * 0.3, center_y - arrow_size/2,
                    center_x - self.cell_size * 0.3, center_y + arrow_size/2
                ]
            
            self.canvas.create_polygon(arrow_points, fill="red", outline="darkred", width=1, tags="robot")
            
        else:
            # Fallback to triangle if no dog image
            body_size = self.cell_size * 0.7
            
            # Draw robot as a triangle pointing in the current direction
            if direction == Direction.NORTH:
                points = [
                    center_x, center_y - body_size/2,
                    center_x - body_size/2, center_y + body_size/2,
                    center_x + body_size/2, center_y + body_size/2
                ]
            elif direction == Direction.EAST:
                points = [
                    center_x + body_size/2, center_y,
                    center_x - body_size/2, center_y - body_size/2,
                    center_x - body_size/2, center_y + body_size/2
                ]
            elif direction == Direction.SOUTH:
                points = [
                    center_x, center_y + body_size/2,
                    center_x - body_size/2, center_y - body_size/2,
                    center_x + body_size/2, center_y - body_size/2
                ]
            else:  # WEST
                points = [
                    center_x - body_size/2, center_y,
                    center_x + body_size/2, center_y - body_size/2,
                    center_x + body_size/2, center_y + body_size/2
                ]
                
            self.canvas.create_polygon(points, fill="blue", outline="darkblue", width=2, tags="robot")
    
    def _draw_trace(self):
        """Draw the movement trace as red lines connecting robot positions."""
        self.canvas.delete("trace")  # Remove previous trace
        
        if len(self.robot_trace) < 2:
            return
            
        for i in range(1, len(self.robot_trace)):
            prev_x, prev_y = self.robot_trace[i-1]
            curr_x, curr_y = self.robot_trace[i]
            
            # Convert to canvas coordinates
            prev_canvas_x = (prev_x + 0.5) * self.cell_size
            prev_canvas_y = ((self.height - 1 - prev_y) + 0.5) * self.cell_size
            curr_canvas_x = (curr_x + 0.5) * self.cell_size  
            curr_canvas_y = ((self.height - 1 - curr_y) + 0.5) * self.cell_size
            
            # Draw line connecting positions
            self.canvas.create_line(
                prev_canvas_x, prev_canvas_y,
                curr_canvas_x, curr_canvas_y,
                fill="red", width=3, tags="trace"
            )

    def add_wall(self, x: int, y: int):
        """Add a wall at the specified coordinates."""
        if (x, y) not in self.walls:  # Prevent duplicate walls
            self.walls.add((x, y))
            self._draw_walls()
    
    def _draw_walls(self):
        """Draw all walls on the canvas."""
        self.canvas.delete("wall")  # Remove previous walls
        for x, y in self.walls:
            cell_x = x * self.cell_size
            cell_y = (self.height - 1 - y) * self.cell_size
            self.canvas.create_rectangle(
                cell_x + 2, cell_y + 2,
                cell_x + self.cell_size - 2,
                cell_y + self.cell_size - 2,
                fill="gray", outline="black", width=2, tags="wall"
            )
    
    def animate_movement(self, start_pos, end_pos):
        """Animate smooth movement from start to end position."""
        print(f"🎬 Starting animation from ({start_pos.x}, {start_pos.y}) to ({end_pos.x}, {end_pos.y})")
        
        if self.is_animating:
            print("⚠️ Animation already running, skipping...")
            return  # Don't start new animation if one is running
            
        self.is_animating = True
        
        # Add start position to trace before animation
        if not self.robot_trace or self.robot_trace[-1] != (start_pos.x, start_pos.y):
            self.robot_trace.append((start_pos.x, start_pos.y))
        
        # Animation parameters
        animation_steps = 15  # Number of frames for smooth movement
        step_delay = 0.03     # Delay between frames 
        
        start_x, start_y = float(start_pos.x), float(start_pos.y)
        end_x, end_y = float(end_pos.x), float(end_pos.y)
        
        # Calculate step increments
        dx = (end_x - start_x) / animation_steps
        dy = (end_y - start_y) / animation_steps
        
        print(f"📊 Animation steps: {animation_steps}, dx: {dx}, dy: {dy}")
        
        def animate_step(step):
            # Calculate intermediate position
            old_x, old_y = self.robot_display_x, self.robot_display_y
            self.robot_display_x = start_x + (dx * step)
            self.robot_display_y = start_y + (dy * step)
            
            if step % 5 == 0:  # Print every 5th frame
                print(f"🎬 Frame {step}: ({old_x:.1f}, {old_y:.1f}) → ({self.robot_display_x:.1f}, {self.robot_display_y:.1f})")
            
            # Redraw robot at new position
            self._draw_trace()  # Update trace
            self._draw_robot()  # Draw robot at new position
            self.root.update()
            
            # Continue animation or finish
            if step < animation_steps:
                # Schedule next frame with explicit step value
                next_step = step + 1
                self.root.after(int(step_delay * 1000), lambda s=next_step: animate_step(s))
            else:
                # Animation complete - ensure final position is exact
                self.robot_display_x = end_x
                self.robot_display_y = end_y
                self.robot_trace.append((end_pos.x, end_pos.y))
                self.is_animating = False
                print(f"✅ Animation complete: final position ({self.robot_display_x}, {self.robot_display_y})")
                # Final redraw with complete trace
                self._draw_trace()
                self._draw_robot()
                self.root.update()
        
        # Start animation
        animate_step(0)
    
    def update(self):
        """Update the display for movements and rotations."""
        # Sync display position with actual position (no animation)
        robot_pos = self.robot.get_position()
        self.robot_display_x = float(robot_pos[0])
        self.robot_display_y = float(robot_pos[1])
        
        # Add current position to trace if it's a new position
        if not self.robot_trace or self.robot_trace[-1] != (robot_pos[0], robot_pos[1]):
            self.robot_trace.append((robot_pos[0], robot_pos[1]))
        
        # Redraw everything
        self._draw_trace()  # Draw trace first (behind robot)
        self._draw_robot()  # Draw robot on top
        self.root.update()
        time.sleep(0.25)  # Standard timing for non-movement updates
    
    def run(self):
        """Start the simulation."""
        self.root.mainloop()
    
    def close(self):
        """Close the simulator window."""
        self.root.destroy()
