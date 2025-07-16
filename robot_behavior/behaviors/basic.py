from ..core.robot import Robot
from typing import Callable
import math
import logging
import sys

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
    else:
        robot.turn_left()

def spiral_movement(robot: Robot, steps: int):
    """Make the robot move in a spiral pattern with visual updates and obstacle avoidance."""
    for i in range(steps):
        for _ in range(i + 1):
            robot.move_forward()
        robot.turn_right()

def square_movement(robot: Robot, size: int):
    """Make the robot move in a square pattern with visual updates and obstacle avoidance."""
    for _ in range(4):
        for _ in range(size):
            robot.move_forward()
        robot.turn_right()
