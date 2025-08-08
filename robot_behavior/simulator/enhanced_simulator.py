import tkinter as tk
from tkinter import messagebox
from typing import Set, Tuple, Optional, List
from robot_behavior.core.robot import Robot, Position
import os
from PIL import Image, ImageTk, ImageDraw
import time
import threading

class EnhancedSimulator:
    """
    Enhanced educational simulator with all requested features:
    - 10x10 grid with dog.png robot image
    - Red line trail showing robot movement path
    - Smooth animated movement between cells
    - Auto-retry on wall collision with popup message
    - Proper timing for educational visualization
    """
    
    def __init__(self, robot: Robot, cell_size: int = 60):
        self.robot = robot
        self.cell_size = cell_size
        self.running = False
        self.root = None
        self.canvas = None
        self.robot_image = None
        self.robot_item = None
        self.movement_trail = []  # Store path for red line trail
        self.trail_lines = []     # Store line objects for trail
        self.animating = False
        
        # Don't create arrow yet - wait until after root window is created
        self.robot_image = None
    
    def _create_robot_arrow(self):
        """Create a solid triangle arrow pointing east for the robot."""
        try:
            # Create a solid triangle arrow image pointing east
            size = int(self.cell_size * 0.7)
            
            # Create a new image with transparent background
            arrow_image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(arrow_image)
            
            # Calculate triangle coordinates (pointing east/right)
            center_x, center_y = size // 2, size // 2
            arrow_size = size * 0.6
            
            # Triangle pointing east (right) - simple triangle shape
            triangle_points = [
                (center_x - arrow_size//2, center_y - arrow_size//2),  # Left top
                (center_x - arrow_size//2, center_y + arrow_size//2),  # Left bottom
                (center_x + arrow_size//2, center_y),                   # Right point (tip)
            ]
            
            # Draw solid blue triangle
            draw.polygon(triangle_points, fill=(0, 100, 200, 255), outline=(0, 50, 150, 255))
            
            self.robot_image = ImageTk.PhotoImage(arrow_image)
            print("▶️ Created solid east-facing triangle arrow for robot")
            
        except Exception as e:
            print(f"⚠️ Error creating triangle arrow: {e}, using simple triangle")
            self.robot_image = None
    
    def _setup_window(self):
        """Setup the main window and UI components with improved styling."""
        # Create main window
        self.root = tk.Tk()
        self.root.title("🤖 Robot Simulator")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        
        # Now that root window exists, create robot arrow
        self._create_robot_arrow()
        
        # Create title frame with better spacing
        title_frame = tk.Frame(self.root, bg="white", height=60)
        title_frame.pack(fill=tk.X, padx=10, pady=5)
        title_frame.pack_propagate(False)
        
        # Enhanced title with professional styling
        title_label = tk.Label(
            title_frame,
            text="🤖 Educational Robot Simulator",
            font=("Arial", 16, "bold"),
            fg="#2563eb",  # Professional blue
            bg="white",
            pady=15
        )
        title_label.pack()
        
        # Info frame with better styling
        info_frame = tk.Frame(self.root, bg="white")
        info_frame.pack(pady=5)
        
        self.position_label = tk.Label(
            info_frame,
            text=f"Position: {self.robot.get_position()}",
            font=("Arial", 12),
            fg="#374151",
            bg="white"
        )
        self.position_label.pack(side=tk.LEFT, padx=15)
        
        self.status_label = tk.Label(
            info_frame,
            text="Ready to move",
            font=("Arial", 12),
            fg="#059669",
            bg="white"
        )
        self.status_label.pack(side=tk.LEFT, padx=15)
        
        # Create canvas with professional styling
        canvas_width = self.robot.grid_width * self.cell_size
        canvas_height = self.robot.grid_height * self.cell_size
        
        self.canvas = tk.Canvas(
            self.root,
            width=canvas_width,
            height=canvas_height,
            bg="white",
            highlightthickness=2,
            highlightbackground="#e5e7eb",  # Professional light gray border
            relief="solid"
        )
        self.canvas.pack(padx=15, pady=10)
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg="white")
        control_frame.pack(pady=10)
        
        reset_button = tk.Button(
            control_frame,
            text="🔄 Reset & Retry",
            command=self._reset_robot,
            font=("Arial", 12, "bold"),
            bg="#3b82f6",
            fg="white",
            relief="flat",
            padx=20,
            pady=5
        )
        reset_button.pack(side=tk.LEFT, padx=10)
        
        close_button = tk.Button(
            control_frame,
            text="❌ Close",
            command=self._close,
            font=("Arial", 12),
            bg="#ef4444",
            fg="white",
            relief="flat",
            padx=20,
            pady=5
        )
        close_button.pack(side=tk.LEFT, padx=10)
        
        # Initialize trail with starting position
        start_pos = self.robot.get_position()
        self.movement_trail = [start_pos]
        
        # Draw initial state
        self._draw_complete_scene()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self._close)
    
    def _draw_complete_scene(self):
        """Draw the complete scene: grid, walls, trail, and robot."""
        # Clear everything except trail lines
        items_to_delete = self.canvas.find_all()
        for item in items_to_delete:
            tags = self.canvas.gettags(item)
            if "trail" not in tags:
                self.canvas.delete(item)
        
        # Draw grid
        self._draw_grid()
        
        # Draw walls
        self._draw_walls()
        
        # Draw movement trail (for any segments not yet drawn)
        self._draw_movement_trail()
        
        # Draw robot
        self._draw_robot()
        
        # Update status
        self._update_status()
    
    def _draw_grid(self):
        """Draw clean grid lines for the specified grid size."""
        # Vertical lines
        for i in range(self.robot.grid_width + 1):
            x = i * self.cell_size
            self.canvas.create_line(
                x, 0, x, self.robot.grid_height * self.cell_size,
                fill="#e5e7eb", width=1
            )
        
        # Horizontal lines
        for i in range(self.robot.grid_height + 1):
            y = i * self.cell_size
            self.canvas.create_line(
                0, y, self.robot.grid_width * self.cell_size, y,
                fill="#e5e7eb", width=1
            )
    
    def _draw_walls(self):
        """Draw walls/obstacles."""
        for x, y in self.robot.walls:
            # Convert to canvas coordinates (y=0 at top for tkinter)
            canvas_x = x * self.cell_size
            canvas_y = (self.robot.grid_height - 1 - y) * self.cell_size
            
            self.canvas.create_rectangle(
                canvas_x + 2, canvas_y + 2,
                canvas_x + self.cell_size - 2,
                canvas_y + self.cell_size - 2,
                fill="#374151", outline="#1f2937", width=2
            )
            
            # Add wall symbol
            center_x = canvas_x + self.cell_size // 2
            center_y = canvas_y + self.cell_size // 2
            self.canvas.create_text(
                center_x, center_y,
                text="🧱", font=("Arial", int(self.cell_size * 0.4))
            )
    
    def _draw_movement_trail(self):
        """Draw red line trail showing robot's path (for initial setup only)."""
        if len(self.movement_trail) < 2:
            return
        
        # Only draw if no trail segments exist yet
        existing_trail = self.canvas.find_withtag("trail")
        if existing_trail:
            return  # Trail already drawn in real-time
        
        # Draw lines between consecutive positions
        for i in range(len(self.movement_trail) - 1):
            start_pos = self.movement_trail[i]
            end_pos = self.movement_trail[i + 1]
            
            # Convert to canvas coordinates
            start_x = start_pos.x * self.cell_size + self.cell_size // 2
            start_y = (self.robot.grid_height - 1 - start_pos.y) * self.cell_size + self.cell_size // 2
            end_x = end_pos.x * self.cell_size + self.cell_size // 2
            end_y = (self.robot.grid_height - 1 - end_pos.y) * self.cell_size + self.cell_size // 2
            
            # Draw red line
            self.canvas.create_line(
                start_x, start_y, end_x, end_y,
                fill="#dc2626", width=4, capstyle=tk.ROUND, tags="trail"
            )
    
    def _draw_robot(self):
        """Draw the robot (solid arrow pointing east) at current position."""
        pos = self.robot.get_position()
        
        # Convert to canvas coordinates
        canvas_x = pos.x * self.cell_size
        canvas_y = (self.robot.grid_height - 1 - pos.y) * self.cell_size
        
        # Calculate center position
        center_x = canvas_x + self.cell_size // 2
        center_y = canvas_y + self.cell_size // 2
        
        if self.robot_image:
            # Use triangle arrow image
            self.robot_item = self.canvas.create_image(
                center_x, center_y,
                image=self.robot_image
            )
        else:
            # Use simple text triangle as fallback
            self.robot_item = self.canvas.create_text(
                center_x, center_y,
                text="▶", font=("Arial", int(self.cell_size * 0.8)), fill="#0064c8"
            )
    
    def _update_status(self):
        """Update position and status labels."""
        if hasattr(self, 'position_label'):
            self.position_label.config(text=f"Position: {self.robot.get_position()}")
        
        if hasattr(self, 'status_label'):
            if self.robot.is_simulation_stopped():
                self.status_label.config(text="❌ Stopped - Hit Wall!", fg="#dc2626")
            else:
                self.status_label.config(text="✅ Moving", fg="#059669")
    
    def animate_move(self, old_pos: Position, new_pos: Position):
        """Animate smooth movement from old position to new position."""
        if not self.robot_item or self.animating:
            return
        
        self.animating = True
        
        # Calculate canvas coordinates
        old_x = old_pos.x * self.cell_size + self.cell_size // 2
        old_y = (self.robot.grid_height - 1 - old_pos.y) * self.cell_size + self.cell_size // 2
        new_x = new_pos.x * self.cell_size + self.cell_size // 2
        new_y = (self.robot.grid_height - 1 - new_pos.y) * self.cell_size + self.cell_size // 2
        
        # Animation parameters
        steps = 15
        delay = 20  # milliseconds
        
        dx = (new_x - old_x) / steps
        dy = (new_y - old_y) / steps
        
        def animate_step(step):
            if step <= steps and self.robot_item:
                current_x = old_x + dx * step
                current_y = old_y + dy * step
                
                # Move robot item
                self.canvas.coords(self.robot_item, current_x, current_y)
                
                if step < steps:
                    self.root.after(delay, lambda: animate_step(step + 1))
                else:
                    self.animating = False
                    # Redraw complete scene after animation
                    self._draw_complete_scene()
        
        animate_step(0)
    
    def robot_moved(self, old_pos: Position, new_pos: Position, success: bool):
        """Called when robot attempts to move - handles animation and trail."""
        # Only proceed if canvas is initialized
        if not self.canvas:
            print("⚠️  GUI not yet initialized - skipping visual update")
            return
            
        if success:
            # Add to movement trail
            self.movement_trail.append(new_pos)
            
            # Draw the red trail line immediately (it will be under the robot)
            self._draw_trail_segment(old_pos, new_pos)
            
            # Redraw the complete scene to ensure proper layering
            self._draw_complete_scene()
            
            # Animate the movement
            self.animate_move(old_pos, new_pos)
        else:
            # Robot hit wall - show popup and auto-reset
            self._handle_wall_collision()
    
    def _draw_trail_segment(self, start_pos: Position, end_pos: Position):
        """Draw a single red trail segment between two positions."""
        # Only draw if positions are different (actual movement occurred)
        if start_pos.x == end_pos.x and start_pos.y == end_pos.y:
            print(f"⚠️  No movement - positions are identical: {start_pos}")
            return
            
        # Convert to canvas coordinates
        start_x = start_pos.x * self.cell_size + self.cell_size // 2
        start_y = (self.robot.grid_height - 1 - start_pos.y) * self.cell_size + self.cell_size // 2
        end_x = end_pos.x * self.cell_size + self.cell_size // 2
        end_y = (self.robot.grid_height - 1 - end_pos.y) * self.cell_size + self.cell_size // 2
        
        # Draw thick red line with enhanced visibility (behind other elements)
        line_item = self.canvas.create_line(
            start_x, start_y, end_x, end_y,
            fill="#ff0000", width=8, capstyle=tk.ROUND, smooth=True, tags="trail"
        )
        
        # Send trail to back so it appears under the robot
        self.canvas.tag_lower(line_item)
        
        # Force canvas update to show line immediately
        self.canvas.update_idletasks()
        
        # Debug print to verify line is being drawn
        print(f"🔴 Drew red line from ({start_x},{start_y}) to ({end_x},{end_y}) - width=8px")
    
    def _handle_wall_collision(self):
        """Handle wall collision with popup and auto-reset."""
        # Show popup message
        messagebox.showwarning(
            "Wall Hit!",
            "🚫 Robot hit a wall!\n\n🔄 Returning to starting position automatically."
        )
        
        # Auto-reset after popup is closed
        self._reset_robot()
    
    def _reset_robot(self):
        """Reset robot to starting position but preserve trail to show path covered."""
        self.robot.reset_simulation()
        
        # Add reset position to trail (to show complete path including reset)
        start_pos = self.robot.get_position()
        self.movement_trail.append(start_pos)
        
        # Redraw scene
        self._draw_complete_scene()
        
        print("🔄 Robot reset to starting position - trail preserved to show full path")
    
    def update_display(self):
        """Update the display after robot state changes."""
        if self.root and self.canvas:
            self._draw_complete_scene()
            self.root.update()
    
    def start_visualization(self, auto_close_seconds: Optional[int] = None):
        """Start the visual simulation."""
        if self.running:
            return
        
        self.running = True
        self._setup_window()
        
        # Set up auto-close if specified
        if auto_close_seconds:
            def auto_close():
                print(f"⏰ Auto-closing simulator after {auto_close_seconds} seconds")
                self._close()
            
            self.root.after(auto_close_seconds * 1000, auto_close)
            print(f"🖥️  Simulator will stay open for {auto_close_seconds} seconds...")
        
        # Start the GUI loop
        try:
            self.root.mainloop()
        except tk.TclError:
            pass
        finally:
            self.running = False
    
    def _close(self):
        """Close the simulator."""
        self.running = False
        if self.root:
            try:
                self.root.quit()
                self.root.destroy()
            except:
                pass

class RobotProgram:
    """
    Enhanced wrapper for educational robot programming with improved features.
    """
    
    def __init__(self, width: int = 10, height: int = 10, start_x: int = 0, start_y: int = 0):
        # Create robot with 10x10 default grid
        self.robot = Robot(start_x, start_y)
        self.robot.grid_width = width
        self.robot.grid_height = height
        
        # Create enhanced simulator
        self.simulator = EnhancedSimulator(self.robot)
        
        print(f"📐 Grid size set to {width} x {height}")
        print(f"🤖 Robot Program initialized: {width}x{height} grid")
        print(f"📍 Robot starting position: ({start_x}, {start_y})")
        print("📖 Available commands: robot.move('up'/'down'/'left'/'right'/'backward')")
        print("🔧 Use robot.get_position() to check current location")
        print("⚠️  Simulation stops on illegal moves - use robot.reset_simulation() to continue")
    
    def add_wall(self, x: int, y: int):
        """Add a wall at the specified position."""
        self.robot.add_wall(x, y)
        print(f"🧱 Wall added at ({x}, {y})")
        if hasattr(self, 'simulator'):
            self.simulator.update_display()
    
    def load_maze(self, layout):
        """Load a maze layout."""
        result = self.robot.load_maze(layout)
        if hasattr(self, 'simulator'):
            self.simulator.update_display()
        return result
    
    def start(self):
        """Start the visual simulator."""
        print("🚀 Starting enhanced simulator...")
        self.simulator.start_visualization()
    
    def start_with_auto_close(self, delay_seconds: int = 5):
        """Start simulator and auto-close after specified seconds."""
        print(f"🚀 Starting simulator (will auto-close in {delay_seconds}s)...")
        self.simulator.start_visualization(delay_seconds)
    
    def update_display(self):
        """Update the visual display after robot moves."""
        if hasattr(self, 'simulator'):
            self.simulator.update_display()
    
    def move_with_delay(self, direction: str):
        """Move robot with visual delay and animation (1.5 second delay)."""
        old_pos = Position(self.robot.position.x, self.robot.position.y)  # Capture before move
        success = self.robot.move(direction)
        new_pos = self.robot.get_position()  # Get after move
        
        # Notify simulator about the move
        if hasattr(self, 'simulator') and self.simulator.running:
            self.simulator.robot_moved(old_pos, new_pos, success)
        
        time.sleep(1.5)  # Fixed 1.5 second delay
        return success
