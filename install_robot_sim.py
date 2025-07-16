# Quick Install Script for Robot Simulation
# Save this as: install_robot_sim.py
# Students can run: python install_robot_sim.py

import subprocess
import sys
import os

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Error: Python 3.7+ required")
        print(f"   Your version: {version.major}.{version.minor}")
        print("   Please upgrade Python")
        return False
    else:
        print(f"✅ Python {version.major}.{version.minor} - Compatible!")
        return True

def check_tkinter():
    """Check if Tkinter is available"""
    try:
        import tkinter
        print("✅ Tkinter - Available!")
        return True
    except ImportError:
        print("❌ Tkinter not found")
        print("   Install with: sudo apt-get install python3-tk (Linux)")
        print("   Or reinstall Python with Tkinter support")
        return False

def install_package():
    """Install the robot behavior package"""
    try:
        print("📦 Installing robot_behavior package...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])
        print("✅ Package installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Installation failed")
        print("   Try: pip install -e . --user")
        return False

def run_example():
    """Run the example to test installation"""
    try:
        print("🤖 Testing installation...")
        os.chdir("examples")
        subprocess.check_call([sys.executable, "student_example.py"])
        print("✅ Installation test successful!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Test failed")
        return False
    except FileNotFoundError:
        print("❌ Examples folder not found")
        print("   Make sure you're in the Robot-behavior directory")
        return False

def main():
    print("🚀 Robot Simulation Setup")
    print("=" * 30)
    
    # Check requirements
    if not check_python_version():
        return
    
    if not check_tkinter():
        return
    
    # Install package
    if not install_package():
        return
    
    # Run test
    print("\n🧪 Running test...")
    print("   (Robot windows should appear)")
    run_example()
    
    print("\n🎉 Setup complete!")
    print("   Run 'python examples/student_example.py' to start")

if __name__ == "__main__":
    main()
