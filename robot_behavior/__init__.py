"""
Robot Behavior Simulator - Educational Programming Framework

An engaging Python package that teaches programming concepts through visual robot simulation.
Perfect for beginners learning their first programming concepts!

🌟 Key Features:
- 🤖 Visual Robot: Triangle arrow that moves smoothly around a grid pointing east
- 🔴 Red Trail Visualization: See exactly where your robot has been
- 🧱 Obstacles & Walls: Navigate around barriers and solve maze challenges  
- ⚡ Immediate Feedback: Instant visual results help students understand their code
- 📚 Educational Focus: Designed specifically for teaching programming fundamentals

Quick Start:
    from robot_behavior import create_robot_program
    
    # Create a 5x5 grid with robot starting at (0, 0)
    program = create_robot_program(5, 5, 0, 0)
    
    # Move the robot and watch the red trail appear!
    program.robot.move('right')
    program.robot.move('up')
    program.robot.move('backward')
    
    # Start the visual display
    program.start_with_auto_close(5)

Educational Concepts Taught:
- Sequential Programming: Execute commands in order
- Conditional Logic: Handle success/failure of movements
- Loops and Patterns: Create repeating behaviors
- Problem Solving: Navigate mazes and avoid obstacles
- Debugging: Use move logs and position checking

Perfect for educators teaching Python programming to beginners!
"""

from .core.robot import Robot, Position
from .simulator.enhanced_simulator import RobotProgram 
from .simulator.minimal_simulator import MinimalSimulator
from .minimal_api import (
    create_robot_program,
    load_maze_from_file,
    run_demo_example,
    SIMPLE_MAZE,
    STUDENT_MAZE
)

__version__ = "1.0.0"
__author__ = "Robot Behavior Team"
__email__ = "cherypallysaisurya@gmail.com"

# Main exports for easy importing
__all__ = [
    'Robot',
    'Position', 
    'RobotProgram',
    'MinimalSimulator',
    'create_robot_program',
    'load_maze_from_file',
    'run_demo_example',
    'SIMPLE_MAZE',
    'STUDENT_MAZE'
]