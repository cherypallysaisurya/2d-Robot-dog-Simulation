# Web-based Robot Simulator (for Google Colab / Online IDEs)
# This version uses matplotlib instead of Tkinter for web compatibility

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np
from robot_behavior.core.robot import Robot, Direction

class WebRobotSimulator:
    """Web-compatible version using matplotlib instead of Tkinter"""
    
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.walls = []
        self.robot = Robot(simulator=self)
        self.path = [(0, 0)]  # Track robot's path
        
        # Set up matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.ax.set_xlim(-0.5, width - 0.5)
        self.ax.set_ylim(-0.5, height - 0.5)
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.ax.set_title('Robot Behavior Simulator (Web Version)')
        
        # Draw initial state
        self._draw_grid()
        self._draw_robot()
        
    def _draw_grid(self):
        """Draw grid lines"""
        for i in range(self.width + 1):
            self.ax.axvline(x=i-0.5, color='gray', linewidth=0.5)
        for i in range(self.height + 1):
            self.ax.axhline(y=i-0.5, color='gray', linewidth=0.5)
    
    def _draw_robot(self):
        """Draw robot and its path"""
        self.ax.clear()
        self._draw_grid()
        
        # Draw walls
        for wall_x, wall_y in self.walls:
            wall = patches.Rectangle((wall_x-0.5, wall_y-0.5), 1, 1, 
                                   facecolor='gray', edgecolor='black')
            self.ax.add_patch(wall)
        
        # Draw robot path
        if len(self.path) > 1:
            path_x = [p[0] for p in self.path]
            path_y = [p[1] for p in self.path]
            self.ax.plot(path_x, path_y, 'b--', alpha=0.5, linewidth=2, label='Robot Path')
        
        # Draw robot
        x, y = self.robot.get_position()
        direction = self.robot.get_direction()
        
        # Robot body (circle)
        robot_circle = patches.Circle((x, y), 0.3, facecolor='blue', edgecolor='darkblue')
        self.ax.add_patch(robot_circle)
        
        # Direction indicator (arrow)
        dx, dy = 0, 0
        if direction == Direction.NORTH:
            dx, dy = 0, 0.4
        elif direction == Direction.EAST:
            dx, dy = 0.4, 0
        elif direction == Direction.SOUTH:
            dx, dy = 0, -0.4
        elif direction == Direction.WEST:
            dx, dy = -0.4, 0
        
        self.ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.1, 
                     fc='red', ec='red')
        
        # Labels and legend
        self.ax.set_xlim(-0.5, self.width - 0.5)
        self.ax.set_ylim(-0.5, self.height - 0.5)
        self.ax.set_title(f'Robot at ({x}, {y}) facing {direction.name}')
        if len(self.path) > 1:
            self.ax.legend()
        
        plt.draw()
    
    def add_wall(self, x, y):
        """Add a wall at specified coordinates"""
        self.walls.append((x, y))
    
    def update(self):
        """Update the display"""
        # Add current position to path
        pos = self.robot.get_position()
        if pos != self.path[-1]:
            self.path.append(pos)
        
        self._draw_robot()
        plt.pause(0.5)  # Pause to make movement visible
    
    def show(self):
        """Show the final result"""
        self._draw_robot()
        plt.show()
    
    def close(self):
        """Close the display"""
        plt.close()

# Example usage for web environments
def web_example():
    """Example that works in Google Colab"""
    
    print("🌐 Web Robot Simulator Example")
    print("This version works in Google Colab and Jupyter notebooks!")
    
    # Create web simulator
    sim = WebRobotSimulator(width=12, height=12)
    
    # Add some walls
    sim.add_wall(3, 3)
    sim.add_wall(4, 4)
    sim.add_wall(5, 3)
    
    # Simple movement pattern
    for i in range(10):
        if i % 3 == 0:
            sim.robot.turn_right()
        sim.robot.move_forward()
        sim.update()
    
    # Show final result
    sim.show()

if __name__ == "__main__":
    web_example()
