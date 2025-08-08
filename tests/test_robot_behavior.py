#!/usr/bin/env python3
"""
Basic tests for robot-behavior-simulator package.
"""

import pytest
import sys
import os

# Add parent directory to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from robot_behavior.minimal_api import create_robot_program
from robot_behavior.core.robot import Robot, Position, Direction


class TestRobotBasics:
    """Test basic robot functionality."""
    
    def test_robot_creation(self):
        """Test that robot can be created."""
        robot = Robot(0, 0)
        assert robot.get_position().x == 0
        assert robot.get_position().y == 0
    
    def test_robot_movement(self):
        """Test basic robot movement."""
        robot = Robot(1, 1)
        robot.set_grid_size(5, 5)
        
        # Test successful movement
        success = robot.move('right')
        assert success == True
        assert robot.get_position().x == 2
        assert robot.get_position().y == 1
        
        # Test another movement
        success = robot.move('up')
        assert success == True
        assert robot.get_position().x == 2
        assert robot.get_position().y == 2
    
    def test_robot_boundaries(self):
        """Test robot boundary detection."""
        robot = Robot(0, 0)
        robot.set_grid_size(3, 3)
        
        # Test boundary hit
        success = robot.move('left')  # Should fail at boundary
        assert success == False
        assert robot.get_position().x == 0  # Should not move
        
        success = robot.move('down')  # Should fail at boundary
        assert success == False
        assert robot.get_position().y == 0  # Should not move
    
    def test_wall_detection(self):
        """Test wall collision detection."""
        robot = Robot(1, 1)
        robot.set_grid_size(5, 5)
        robot.add_wall(2, 1)  # Add wall to the right
        
        # Test wall collision
        success = robot.move('right')  # Should hit wall
        assert success == False
        assert robot.get_position().x == 1  # Should not move
    
    def test_backward_movement(self):
        """Test backward movement functionality."""
        robot = Robot(2, 2)
        robot.set_grid_size(5, 5)
        
        # Test backward movement (should move west/left)
        success = robot.move('backward')
        assert success == True
        assert robot.get_position().x == 1  # Moved left
        assert robot.get_position().y == 2  # Y unchanged


class TestRobotProgram:
    """Test the RobotProgram wrapper."""
    
    def test_program_creation(self):
        """Test that robot program can be created."""
        program = create_robot_program(5, 5, 1, 1)
        assert program.robot.get_position().x == 1
        assert program.robot.get_position().y == 1
    
    def test_add_wall(self):
        """Test adding walls through program interface."""
        program = create_robot_program(5, 5, 0, 0)
        program.add_wall(2, 2)
        
        # Move to wall position and test collision
        program.robot.move('right')  # (0,0) -> (1,0)
        program.robot.move('right')  # (1,0) -> (2,0)
        program.robot.move('up')     # (2,0) -> (2,1)
        success = program.robot.move('up')  # (2,1) -> (2,2) should hit wall
        assert success == False


class TestDirections:
    """Test direction enumeration."""
    
    def test_direction_values(self):
        """Test that all directions have correct values."""
        assert Direction.UP.value == "up"
        assert Direction.DOWN.value == "down"
        assert Direction.LEFT.value == "left"
        assert Direction.RIGHT.value == "right"
        assert Direction.BACKWARD.value == "backward"


if __name__ == '__main__':
    # Run tests
    pytest.main([__file__, '-v'])
