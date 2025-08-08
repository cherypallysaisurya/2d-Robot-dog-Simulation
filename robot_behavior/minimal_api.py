"""
Minimal Robot API for Educational Programming

This module provides the core robot movement API with strict obstacle detection.
Students must implement all complex behaviors using only these basic commands:

- robot.move(direction) - Move one cell in specified direction  
- robot.get_position() - Get current position
- robot.load_maze(layout) - Load instructor-defined maze
- robot.reset_simulation() - Reset after hitting obstacle

The simulation stops immediately on illegal moves, requiring students
to handle error cases and implement proper movement logic.
"""

from robot_behavior.core.robot import Robot, Position
from robot_behavior.simulator.enhanced_simulator import RobotProgram

# Simple maze layouts for educational use
SIMPLE_MAZE = [
    ['.', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'], 
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.']
]

STUDENT_MAZE = [
    ['S', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.', '.'], 
    ['.', '.', '.', '#', '#', '#', '.', '.'],
    ['#', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '#', '.', '#', '#', '.'],
    ['.', '#', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.']
]

def create_robot_program(width=10, height=10, start_x=0, start_y=0):
    """
    Create a new robot program for student exercises.
    
    Args:
        width: Grid width
        height: Grid height
        start_x: Starting X position
        start_y: Starting Y position
        
    Returns:
        RobotProgram: Program instance with robot and simulator
    """
    return RobotProgram(width, height, start_x, start_y)

def load_maze_from_file(filename):
    """
    Load a maze layout from a text file.
    
    File format:
    - '.' for empty space
    - '#' for wall
    - 'S' for start position
    
    Args:
        filename: Path to maze file
        
    Returns:
        List[List[str]]: 2D maze layout
    """
    try:
        with open(filename, 'r') as f:
            return [list(line.strip()) for line in f.readlines()]
    except FileNotFoundError:
        print(f"❌ Maze file not found: {filename}")
        return None
    except Exception as e:
        print(f"❌ Error loading maze: {e}")
        return None

# Export main classes and functions
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

def run_demo_example():
    """
    Demo function that runs when users type 'robot-demo' command.
    Shows off the robot simulator capabilities.
    """
    import time
    
    print("🤖 Robot Behavior Simulator Demo")
    print("=" * 40)
    print("Welcome to the Robot Behavior Simulator!")
    print("Watch the robot move around and leave a red trail...")
    print()
    
    # Create demo program
    program = create_robot_program(8, 8, 0, 0)
    
    # Add some walls for interesting navigation
    walls = [(3, 1), (3, 2), (3, 3), (5, 4), (5, 5), (2, 6)]
    for x, y in walls:
        program.add_wall(x, y)
    
    # Start the visual display
    import threading
    gui_thread = threading.Thread(target=program.start)
    gui_thread.daemon = True
    gui_thread.start()
    time.sleep(1)
    
    # Demo movement sequence
    movements = [
        'right', 'right', 'up', 'up', 'up', 'right', 
        'right', 'up', 'up', 'left', 'left', 'down'
    ]
    
    print("🚀 Starting demo movement sequence...")
    for i, direction in enumerate(movements, 1):
        print(f"Step {i}: Moving {direction}")
        program.move_with_delay(direction)
    
    print("✅ Demo complete! The window will stay open for 10 seconds.")
    print("   You can see:")
    print("   • Blue triangle robot pointing east")
    print("   • Red trail showing movement path") 
    print("   • Black squares showing walls")
    
    time.sleep(10)
    print("🎓 Try creating your own robot programs!")
    print("   Check out: https://github.com/cherypallysaisurya/2d-Robot-dog-Simulation")
