#!/usr/bin/env python3
"""
Minimal API Examples - Educational Robot Programming

This file demonstrates the basic usage of the minimal robot API.
Perfect for students learning robot movement concepts.
"""

from robot_behavior.minimal_api import create_robot_program
import time

def simple_example():
    print("🤖 Simple Robot Example")
    print("Moving robot right 2 times, then up 1 time")
    print()
    
    # Create robot world (5x5 grid, start at 0,0)
    program = create_robot_program(5, 5, 0, 1)
    
    # Add a few walls
    program.add_wall(2, 0)
    program.add_wall(3, 1)

    
    # Start the display
    import threading
    gui_thread = threading.Thread(target=program.start)
    gui_thread.daemon = True
    gui_thread.start()
    time.sleep(1)
    
    
    '''for i in range(10):
        if i%2 == 0:
            print(f"Step {i+1}: Moving right")
            program.move_with_delay('right')
        else:
            print(f"Step {i+1}: Moving up")
            program.move_with_delay('up')'''

    # Move the robot
    print("Step 1: Moving right")
    program.move_with_delay('right')
    
    print("Step 2: Moving right")
    program.move_with_delay('right')
    
    print("Step 3: Moving up")
    program.move_with_delay('up')
    
    print("Step 4: Moving up")
    program.move_with_delay('up')
    
    
    time.sleep(5)

if __name__ == "__main__":
    simple_example()