from ..core.robot import Robot
from ..simulator.simulator import RobotSimulator
from typing import Callable, Any
import time

class RobotProgram:
    def __init__(self, width: int = 10, height: int = 10):
        """Initialize a new robot program with specified grid size."""
        self.simulator = RobotSimulator(width, height)
        self.robot = self.simulator.robot
    
    def add_wall(self, x: int, y: int):
        """Add a wall at the specified position."""
        self.simulator.add_wall(x, y)
    
    def run_behavior(self, behavior: Callable[[Robot, Any], None], *args):
        """Run a specific behavior function with the robot."""
        behavior(self.robot, *args)
    
    def start(self):
        """Start the simulation."""
        self.simulator.run()
    
    def stop(self):
        """Stop the simulation."""
        try:
            self.simulator.close()
        except:
            pass  # Ignore errors if window already closed

def run_prime_bot(numbers: list[int]):
    """Run a robot that moves based on prime numbers. Closes window after completion."""
    from ..behaviors.basic import move_if_prime
    
    program = RobotProgram()
    # Add some walls for obstacles
    program.add_wall(3, 3)
    program.add_wall(4, 2)
    program.add_wall(2, 4)
    for num in numbers:
        program.run_behavior(move_if_prime, num)
    program.simulator.root.after(2000, lambda: program.simulator.close())
    program.start()

def run_even_odd_bot(numbers: list[int]):
    """Run a robot that turns based on even/odd numbers. Closes window after completion."""
    from ..behaviors.basic import turn_if_even
    
    program = RobotProgram()
    # Add walls
    program.add_wall(2, 1)
    program.add_wall(3, 2)
    program.add_wall(1, 3)
    for num in numbers:
        program.run_behavior(turn_if_even, num)
        program.robot.move_forward()
    program.simulator.root.after(2000, lambda: program.simulator.close())
    program.start()

def run_spiral_bot(steps: int):
    """Run a robot that moves in a spiral pattern. Closes window after completion."""
    from ..behaviors.basic import spiral_movement
    
    program = RobotProgram(width=15, height=15)  # Larger grid for spiral
    # Add walls in spiral path
    program.add_wall(3, 3)
    program.add_wall(5, 5)
    program.add_wall(7, 2)
    program.run_behavior(spiral_movement, steps)
    program.simulator.root.after(3000, lambda: program.simulator.close())
    program.start()

def run_square_bot(size: int):
    """Run a robot that moves in a square pattern. Closes window after completion."""
    from ..behaviors.basic import square_movement
    
    program = RobotProgram(width=12, height=12)  # Larger grid for square
    # Add walls in square path
    program.add_wall(2, 2)
    program.add_wall(4, 1)
    program.add_wall(1, 4)
    program.run_behavior(square_movement, size)
    program.simulator.root.after(3000, lambda: program.simulator.close())
    program.start()
