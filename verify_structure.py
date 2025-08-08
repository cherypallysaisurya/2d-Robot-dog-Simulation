"""
Quick structure verification for robot-behavior-simulator package
"""

import sys
import os
from pathlib import Path

def check_structure():
    """Check that all required files are present."""
    print("🔍 Checking package structure...")
    
    required_files = [
        "pyproject.toml",
        "README.md", 
        "LICENSE",
        ".gitignore",
        "robot_behavior/__init__.py",
        "robot_behavior/minimal_api.py",
        "robot_behavior/core/__init__.py",
        "robot_behavior/core/robot.py",
        "robot_behavior/simulator/__init__.py",
        "robot_behavior/simulator/enhanced_simulator.py",
        "robot_behavior/simulator/minimal_simulator.py",
        "examples/minimal_api_examples.py",
        "examples/student_template.py",
        "tests/test_robot_behavior.py"
    ]
    
    missing_files = []
    present_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            present_files.append(file_path)
            print(f"✅ {file_path}")
        else:
            missing_files.append(file_path)
            print(f"❌ {file_path}")
    
    print(f"\n📊 Structure Check Results:")
    print(f"✅ Present: {len(present_files)}")
    print(f"❌ Missing: {len(missing_files)}")
    
    if missing_files:
        print(f"\n⚠️  Missing files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print(f"\n🎉 All required files present! Package structure is ready.")
        return True

def check_imports():
    """Test that main imports work."""
    print(f"\n🔍 Testing imports...")
    
    try:
        # Add current directory to path
        sys.path.insert(0, os.getcwd())
        
        from robot_behavior import create_robot_program, Robot, Position
        print("✅ Main imports successful")
        
        # Test basic functionality
        program = create_robot_program(3, 3, 0, 0)
        print("✅ Package creation successful")
        
        pos = program.robot.get_position()
        print(f"✅ Robot position: {pos}")
        
        return True
    except Exception as e:
        print(f"❌ Import test failed: {e}")
        return False

def main():
    print("🤖 Robot Behavior Simulator - Structure Verification")
    print("=" * 55)
    
    structure_ok = check_structure()
    imports_ok = check_imports()
    
    if structure_ok and imports_ok:
        print(f"\n🎉 Package is ready for TestPyPI!")
        print(f"📦 Next steps:")
        print(f"   1. Install build tools: pip install build twine")
        print(f"   2. Build package: python -m build")
        print(f"   3. Upload to TestPyPI: python -m twine upload --repository testpypi dist/*")
        print(f"   4. Test install: pip install --index-url https://test.pypi.org/simple/ robot-behavior-simulator")
    else:
        print(f"\n❌ Package needs fixes before upload")

if __name__ == "__main__":
    main()
