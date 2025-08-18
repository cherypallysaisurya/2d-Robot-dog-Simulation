from robot_behavior.minimal_api import create_robot_program

def simple_example():
    """Simple robot movement example with visual feedback"""
    print("🤖 Simple Robot Example")
    print("Moving robot right 2 times, then up 2 times")
    print()
    
    # Create robot world (5x5 grid, start at position 0,1)
    program = create_robot_program(5, 5, 0, 1)
    
    # Add some walls to make it interesting
    program.add_wall(2, 0)
    program.add_wall(3, 1)
    
    # Move the robot step by step
    print("Step 1: Moving right")
    program.move_with_delay('right')
    
    print("Step 2: Moving right")
    program.move_with_delay('right')
    
    print("Step 3: Moving up")
    program.move_with_delay('up')
    
    print("Step 4: Moving up")
    program.move_with_delay('up')
    
    print("Robot movement complete! Watch the red trail.")
    
    # Start the visual display
    program.start()

if __name__ == "__main__":
    simple_example()