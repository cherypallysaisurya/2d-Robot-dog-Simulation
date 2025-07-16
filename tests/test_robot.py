import unittest
from robot_behavior.core.robot import Robot, Direction, Position

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
    
    def test_initial_position(self):
        self.assertEqual(self.robot.get_position(), (0, 0))
        self.assertEqual(self.robot.get_direction(), Direction.NORTH)
    
    def test_move_forward(self):
        self.robot.move_forward()
        self.assertEqual(self.robot.get_position(), (0, 1))
    
    def test_turn_left(self):
        self.robot.turn_left()
        self.assertEqual(self.robot.get_direction(), Direction.WEST)
    
    def test_turn_right(self):
        self.robot.turn_right()
        self.assertEqual(self.robot.get_direction(), Direction.EAST)
    
    def test_movement_log(self):
        self.robot.move_forward()
        self.robot.turn_right()
        self.robot.move_forward()
        self.assertEqual(len(self.robot.movement_log), 3)

if __name__ == '__main__':
    unittest.main()
