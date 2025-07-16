from robot_behavior.behaviors.api import (
    run_prime_bot,
    run_even_odd_bot,
    run_spiral_bot,
    run_square_bot,
    RobotProgram
)
from robot_behavior.behaviors.basic import move_if_prime, turn_if_even

# Example 1: Run a prime number robot
print("Running prime number robot...")
run_prime_bot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# Example 2: Run an even/odd turning robot
print("Running even/odd turning robot...")
run_even_odd_bot([1, 2, 3, 4, 5,6,7,8,9,10,11,12])

# Example 3: Run a spiral pattern
print("Running spiral pattern...")
run_spiral_bot(6)

# Example 4: Run a square pattern
print("Running square pattern...")
run_square_bot(4)

# Example 5: Custom behavior with more movement
print("Running custom behavior...")
program = RobotProgram(width=12, height=12)

# Add a maze-like wall pattern
program.add_wall(2, 2)
program.add_wall(2, 3)
program.add_wall(3, 2)
program.add_wall(4, 4)
program.add_wall(5, 3)
program.add_wall(6, 5)

# Custom sequence of movements - create a more complex pattern
for i in range(8):
    program.robot.move_forward()
    if i % 2 == 0:
        program.robot.turn_right()
    else:
        program.robot.turn_left()

# Add some more forward moves
for _ in range(5):
    program.robot.move_forward()

# Schedule window close after 4 seconds
program.simulator.root.after(4000, lambda: program.simulator.close())
program.start()
