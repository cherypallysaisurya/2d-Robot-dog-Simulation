#!/usr/bin/env python3
"""
Robot Movement Test - Cross-Platform Compatible

Simple example that works on Windows, macOS, and Linux.
"""

from robot_behavior.minimal_api import create_robot_program
import time

def simple_example():
    print("🤖 Simple Robot Example")
    print("Moving robot right 2 times, then up 2 times")
    print()
    
    # Create robot world (5x5 grid, start at 0,1)
    program = create_robot_program(5, 5, 0, 1)
    
    # Add a few walls
    program.add_wall(2, 0)
    program.add_wall(3, 1)

    # Schedule the robot movements to happen after GUI starts
    def run_robot_moves():
        time.sleep(2)  # Wait for GUI to initialize
        
        print("Step 1: Moving right")
        program.move_with_delay('right')
        
        print("Step 2: Moving right")
        program.move_with_delay('right')
        
        print("Step 3: Moving up")
        program.move_with_delay('up')
        
        print("Step 4: Moving up")
        program.move_with_delay('up')
        
        time.sleep(3)  # Keep the GUI open for a bit
        # The GUI will close automatically after this
    
    # Start robot movements in background while GUI runs on main thread
    import threading
    movement_thread = threading.Thread(target=run_robot_moves)
    movement_thread.daemon = True
    movement_thread.start()
    
    # Start the GUI on the main thread (required for macOS)
    program.start()

if __name__ == "__main__":
    simple_example()