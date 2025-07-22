from dataclasses import dataclass
from typing import List, Tuple
import logging
from enum import Enum
import time
import random

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

@dataclass
class Position:
    x: int
    y: int
    
    def __hash__(self):
        return hash((self.x, self.y))

class Robot:
    def __init__(self, x: int = None, y: int = None, direction: Direction = None, simulator=None, random_start: bool = False):
        # Handle random starting position and direction
        if random_start and simulator:
            # Random starting position (avoid walls)
            max_attempts = 50
            for _ in range(max_attempts):
                rand_x = random.randint(1, simulator.width - 2)
                rand_y = random.randint(1, simulator.height - 2)
                if (rand_x, rand_y) not in simulator.walls:
                    x, y = rand_x, rand_y
                    break
            
            # Random starting direction
            if direction is None:
                direction = random.choice(list(Direction))
        
        # If no position specified, start from center of grid
        if x is None or y is None:
            grid_size = 10  # Default grid size
            if simulator:
                grid_size = min(simulator.width, simulator.height)
            center = grid_size // 2
            self.position = Position(center, center)
        else:
            self.position = Position(x, y)
            
        self.direction = direction if direction is not None else Direction.NORTH
        self.movement_log = []
        self.simulator = simulator  # Reference to simulator for wall info
        
        print(f"🤖 Robot spawned at ({self.position.x}, {self.position.y}) facing {self.direction.name}")
        
        logging.basicConfig(
            filename='robot_movement.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )
    
    def move_forward(self) -> bool:
        """Move the robot one step forward in its current direction."""
        new_pos = Position(self.position.x, self.position.y)
        
        if self.direction == Direction.NORTH:
            new_pos.y += 1
        elif self.direction == Direction.EAST:
            new_pos.x += 1
        elif self.direction == Direction.SOUTH:
            new_pos.y -= 1
        elif self.direction == Direction.WEST:
            new_pos.x -= 1
            
        if self._is_valid_position(new_pos):
            # Simple movement - update position and redraw
            self.position = new_pos
            if self.simulator:
                self.simulator.update()  # Simple redraw without animation
            self._log_movement("MOVE_FORWARD")
            return True
        else:
            # Hit a wall or boundary - log and turn (no recursive move)
            msg = f"Hit wall at ({new_pos.x}, {new_pos.y}) → Took diversion"
            logging.info(msg)
            self.movement_log.append((time.time(), msg, self.position, self.direction))
            print(msg)
            self.turn_right()  # Turn right when hitting obstacle
            return False
    
    def turn_left(self):
        """Turn the robot 90 degrees to the left."""
        self.direction = Direction((self.direction.value - 1) % 4)
        self._log_movement("TURN_LEFT")
        if self.simulator:
            self.simulator.update()  # Simple update for rotations
    
    def turn_right(self):
        """Turn the robot 90 degrees to the right."""
        self.direction = Direction((self.direction.value + 1) % 4)
        self._log_movement("TURN_RIGHT")
        if self.simulator:
            self.simulator.update()  # Simple update for rotations
    
    def _is_valid_position(self, pos: Position) -> bool:
        """Check if the given position is valid (no walls/obstacles)."""
        if self.simulator and (pos.x, pos.y) in self.simulator.walls:
            return False
        if pos.x < 0 or pos.x >= (self.simulator.width if self.simulator else 10):
            return False
        if pos.y < 0 or pos.y >= (self.simulator.height if self.simulator else 10):
            return False
        return True
    
    def _log_movement(self, action: str):
        """Log robot movements with timestamp."""
        message = f"Robot {action} - Position: ({self.position.x}, {self.position.y}), Direction: {self.direction.name}"
        logging.info(message)
        self.movement_log.append((time.time(), action, self.position, self.direction))
    
    def get_position(self) -> Tuple[int, int]:
        """Return the current position of the robot."""
        return (self.position.x, self.position.y)
    
    def get_direction(self) -> Direction:
        """Return the current direction of the robot."""
        return self.direction
