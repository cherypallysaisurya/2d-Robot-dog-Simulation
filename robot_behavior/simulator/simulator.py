import tkinter as tk
from ..core.robot import Robot, Direction
from typing import List, Tuple
import time

class RobotSimulator:
    def __init__(self, width: int = 10, height: int = 10, cell_size: int = 50):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.walls: List[Tuple[int, int]] = []
        self.robot = Robot(simulator=self)  # Pass simulator reference
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Robot Behavior Simulator")
        
        # Create canvas
        canvas_width = width * cell_size
        canvas_height = height * cell_size
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height)
        self.canvas.pack()
        
        # Draw grid
        self._draw_grid()
        
        # Initial robot drawing
        self._draw_robot()
    
    def _draw_grid(self):
        """Draw the grid on the canvas."""
        for i in range(self.width + 1):
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, self.height * self.cell_size)
            
        for i in range(self.height + 1):
            y = i * self.cell_size
            self.canvas.create_line(0, y, self.width * self.cell_size, y)
    
    def _draw_robot(self):
        """Draw the robot on the canvas."""
        x, y = self.robot.get_position()
        direction = self.robot.get_direction()
        
        # Calculate center of cell
        center_x = (x + 0.5) * self.cell_size
        center_y = ((self.height - 1 - y) + 0.5) * self.cell_size
        
        # Draw robot body
        body_size = self.cell_size * 0.8
        self.canvas.delete("robot")  # Remove previous robot drawing
        
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
            
        self.canvas.create_polygon(points, fill="blue", tags="robot")
    
    def add_wall(self, x: int, y: int):
        """Add a wall at the specified coordinates."""
        self.walls.append((x, y))
        cell_x = x * self.cell_size
        cell_y = (self.height - 1 - y) * self.cell_size
        self.canvas.create_rectangle(
            cell_x, cell_y,
            cell_x + self.cell_size,
            cell_y + self.cell_size,
            fill="gray"
        )
    
    def update(self):
        """Update the display."""
        self._draw_robot()
        self.root.update()
        time.sleep(0.3)  # Slightly faster for better visual feedback
    
    def run(self):
        """Start the simulation."""
        self.root.mainloop()
    
    def close(self):
        """Close the simulator window."""
        self.root.destroy()
