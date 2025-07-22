from ..core.robot import Robot
from typing import Callable
import math
import logging
import sys
import time

def is_prime(n: int) -> bool:
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def move_if_prime(robot: Robot, n: int):
    """Move forward if the number is prime. Print/log result for every number."""
    if is_prime(n):
        moved = robot.move_forward()
        msg = f"{n} is prime: robot moved forward."
        # Add small delay to let animation complete
        time.sleep(0.5)  # Wait for smooth animation
    else:
        moved = False
        msg = f"{n} is not prime: robot did not move."
    print(msg)
    logging.info(msg)
    # Also log to robot's movement_log for completeness
    robot.movement_log.append((n, msg, robot.get_position(), robot.get_direction()))

def turn_if_even(robot: Robot, n: int):
    """Turn right if the number is even, left if odd."""
    if n % 2 == 0:
        robot.turn_right()
        print(f"{n} is even: robot turned right.")
    else:
        robot.turn_left()
        print(f"{n} is odd: robot turned left.")

def spiral_movement(robot: Robot, steps: int):
    """Make the robot move in a spiral pattern with visual updates and obstacle avoidance."""
    for i in range(steps):
        # Move forward (i+1) steps
        for step in range(i + 1):
            robot.move_forward()
            time.sleep(0.1)  # Small pause between moves for better visibility
        # Turn right to continue spiral
        robot.turn_right()
        print(f"Spiral layer {i+1} completed - turned right")

def square_movement(robot: Robot, size: int):
    """Make the robot move in a square pattern with visual updates and obstacle avoidance."""
    for side in range(4):
        # Move along one side of the square
        for step in range(size):
            robot.move_forward()
            time.sleep(0.1)  # Small pause between moves
        # Turn right to next side
        robot.turn_right()
        print(f"Square side {side+1} completed - turned right")
