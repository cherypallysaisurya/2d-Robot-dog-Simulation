from ..core.robot import Robot
from ..simulator.simulator import RobotSimulator
from typing import Callable, Any
import time

def _wait_for_animation(program: 'RobotProgram', max_wait_seconds: float = 2.0):
    """Helper function to wait for animations to complete."""
    start_time = time.time()
    while program.simulator.is_animating and (time.time() - start_time) < max_wait_seconds:
        program.simulator.root.update()
        time.sleep(0.01)

class RobotProgram:
    def __init__(self, width: int = 10, height: int = 10, random_robot: bool = False):
        """Initialize a new robot program with specified grid size."""
        self.simulator = RobotSimulator(width, height, random_robot=random_robot)
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

def run_prime_bot(numbers: list[int], random_start: bool = True):
    """Run a robot that moves based on prime numbers. Closes window after completion."""
    from ..behaviors.basic import move_if_prime
    
    program = RobotProgram(10, 10, random_robot=random_start)  # Random by default now
    # Add strategic wall clusters for better visual demonstration
    program.add_wall(3, 3)
    program.add_wall(4, 2)
    program.add_wall(2, 4)
    program.add_wall(7, 7)
    program.add_wall(8, 6)
    
    start_msg = "🤖 Prime Bot: Starting with numbers " + str(numbers)
    if random_start:
        start_msg += " (Random start)"
    else:
        start_msg += " (Center start)"
    print(start_msg)
    print(f"🎯 Robot starts at: {program.robot.get_position()}")
    
    for num in numbers:
        program.run_behavior(move_if_prime, num)
    
    print("✅ Prime Bot: Movement sequence completed!")
    program.simulator.root.after(5000, lambda: program.simulator.close())
    program.start()

def run_even_odd_bot(numbers: list[int], random_start: bool = True):
    """Run a robot that turns based on even/odd numbers. Closes window after completion."""
    from ..behaviors.basic import turn_if_even
    
    program = RobotProgram(10, 10, random_robot=random_start)  # Random by default now
    # Add walls to create interesting navigation
    program.add_wall(2, 1)
    program.add_wall(3, 2)
    program.add_wall(1, 3)
    program.add_wall(6, 6)
    program.add_wall(7, 5)
    
    start_msg = "🤖 Even/Odd Bot: Starting with numbers " + str(numbers)
    if random_start:
        start_msg += " (Random start)"
    else:
        start_msg += " (Center start)"
    print(start_msg)
    print(f"🎯 Robot starts at: {program.robot.get_position()}")
    
    for num in numbers:
        program.run_behavior(turn_if_even, num)
        program.robot.move_forward()
    
    print("✅ Even/Odd Bot: Movement sequence completed!")
    program.simulator.root.after(5000, lambda: program.simulator.close())
    program.start()

def run_spiral_bot(steps: int, random_start: bool = True):
    """Run a robot that moves in a spiral pattern. Closes window after completion."""
    from ..behaviors.basic import spiral_movement
    
    program = RobotProgram(10, 10, random_robot=random_start)  # Random by default now
    # Add walls that create interesting spiral obstacles
    program.add_wall(3, 3)
    program.add_wall(6, 6)
    program.add_wall(7, 2)
    program.add_wall(2, 7)
    
    start_msg = f"🤖 Spiral Bot: Starting spiral pattern with {steps} steps"
    if random_start:
        start_msg += " (Random start)"
    else:
        start_msg += " (Center start)"
    print(start_msg)
    print(f"🎯 Robot starts at: {program.robot.get_position()}")
    
    program.run_behavior(spiral_movement, steps)
    
    print("✅ Spiral Bot: Spiral pattern completed!")
    program.simulator.root.after(6000, lambda: program.simulator.close())
    program.start()

def run_square_bot(size: int):
    """Run a robot that moves in a square pattern. Closes window after completion."""
    from ..behaviors.basic import square_movement
    
    program = RobotProgram(10, 10)  # Consistent 10x10 grid for square
    # Add walls that create square pattern obstacles
    program.add_wall(2, 2)
    program.add_wall(7, 2)
    program.add_wall(7, 7)
    program.add_wall(2, 7)
    
    print(f"🤖 Square Bot: Starting square pattern with size {size}")
    print(f"🎯 Robot starts at center: {program.robot.get_position()}")
    
    program.run_behavior(square_movement, size)
    
    print("✅ Square Bot: Square pattern completed!")
    program.simulator.root.after(6000, lambda: program.simulator.close())
    program.start()

def run_random_prime_bot(numbers: list[int]):
    """Run a robot with RANDOM starting position that moves based on prime numbers."""
    run_prime_bot(numbers, random_start=True)

def run_center_prime_bot(numbers: list[int]):
    """Run a robot with CENTER starting position that moves based on prime numbers."""
    run_prime_bot(numbers, random_start=False)

def run_center_even_odd_bot(numbers: list[int]):
    """Run a robot with CENTER starting position that turns based on even/odd numbers."""
    run_even_odd_bot(numbers, random_start=False)

def run_center_spiral_bot(steps: int):
    """Run a robot with CENTER starting position that moves in a spiral pattern."""
    run_spiral_bot(steps, random_start=False)

def run_random_explorer(steps: int = 20):
    """Run a robot that starts at a random position and explores randomly."""
    import random
    
    program = RobotProgram(12, 12, random_robot=True)  # Larger grid for exploration
    
    # Add some random walls
    for _ in range(8):
        wall_x, wall_y = random.randint(1, 10), random.randint(1, 10)
        if (wall_x, wall_y) != program.robot.get_position():  # Don't put wall on robot
            program.add_wall(wall_x, wall_y)
    
    print(f"🗺️ Random Explorer: Starting from {program.robot.get_position()}")
    print(f"🚀 Will explore for {steps} steps with random decisions")
    
    for step in range(steps):
        # Random decision: 70% move, 30% turn
        if random.random() < 0.7:
            moved = program.robot.move_forward()
            if not moved:  # Hit wall, make a random turn
                if random.random() < 0.5:
                    program.robot.turn_left()
                else:
                    program.robot.turn_right()
        else:
            # Random turn
            if random.random() < 0.5:
                program.robot.turn_left()
            else:
                program.robot.turn_right()
        
        time.sleep(0.3)  # Slow down to see exploration
    
    print("✅ Random Explorer: Exploration completed!")
    program.simulator.root.after(4000, lambda: program.simulator.close())
    program.start()
