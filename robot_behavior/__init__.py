# Robot Behavior Framework - Main Package
# This allows students to use: from robot_behavior import *

from .behaviors.api import (
    run_prime_bot,
    run_even_odd_bot, 
    run_spiral_bot,
    run_square_bot,
    run_random_prime_bot,
    run_random_explorer,
    run_center_prime_bot,
    run_center_even_odd_bot,
    run_center_spiral_bot,
    RobotProgram
)

from .behaviors.basic import (
    move_if_prime,
    turn_if_even,
    spiral_movement,
    square_movement,
    is_prime
)

from .core.robot import Robot, Direction

# Make everything available with simple import
__all__ = [
    # High-level student functions
    'run_prime_bot',
    'run_even_odd_bot',
    'run_spiral_bot', 
    'run_square_bot',
    'RobotProgram',
    
    # Behavior functions for custom robots
    'move_if_prime',
    'turn_if_even',
    'spiral_movement',
    'square_movement',
    'is_prime',
    
    # Core classes for advanced users
    'Robot',
    'Direction'
]

# Package metadata
__version__ = "1.0.0"
__author__ = "Robot Behavior Framework"
__description__ = "Educational 2D robot simulation framework"