#!/usr/bin/env python3
"""
Build and upload script for robot-behavior-simulator

Usage:
    python build_and_upload.py          # Build only
    python build_and_upload.py --test   # Upload to TestPyPI
    python build_and_upload.py --prod   # Upload to PyPI
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔨 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} successful")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)

def clean_build():
    """Clean previous build artifacts."""
    print("🧹 Cleaning previous builds...")
    dirs_to_clean = ['build', 'dist', '*.egg-info']
    for dir_pattern in dirs_to_clean:
        if '*' in dir_pattern:
            # Handle glob patterns
            import glob
            for path in glob.glob(dir_pattern):
                if os.path.exists(path):
                    import shutil
                    shutil.rmtree(path)
                    print(f"   Removed {path}")
        else:
            if os.path.exists(dir_pattern):
                import shutil
                shutil.rmtree(dir_pattern)
                print(f"   Removed {dir_pattern}")

def build_package():
    """Build the package."""
    clean_build()
    run_command("python -m build", "Building package")

def upload_to_testpypi():
    """Upload to TestPyPI."""
    run_command("python -m twine upload --repository testpypi dist/*", "Uploading to TestPyPI")
    print("\n🎉 Package uploaded to TestPyPI!")
    print("📦 Install with: pip install --index-url https://test.pypi.org/simple/ robot-behavior-simulator")

def upload_to_pypi():
    """Upload to PyPI."""
    response = input("⚠️  Are you sure you want to upload to PyPI (production)? (y/N): ")
    if response.lower() != 'y':
        print("Upload cancelled.")
        return
    
    run_command("python -m twine upload dist/*", "Uploading to PyPI")
    print("\n🎉 Package uploaded to PyPI!")
    print("📦 Install with: pip install robot-behavior-simulator")

def main():
    """Main function."""
    print("🤖 Robot Behavior Simulator - Build & Upload Script")
    print("=" * 50)
    
    # Check if required tools are installed
    try:
        subprocess.run(["python", "-m", "build", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ 'build' package not found. Install with: pip install build")
        sys.exit(1)
    
    try:
        subprocess.run(["python", "-m", "twine", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ 'twine' package not found. Install with: pip install twine")
        sys.exit(1)
    
    # Build the package
    build_package()
    
    # Handle upload options
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            upload_to_testpypi()
        elif sys.argv[1] == "--prod":
            upload_to_pypi()
        else:
            print(f"❌ Unknown option: {sys.argv[1]}")
            print("Use --test for TestPyPI or --prod for PyPI")
            sys.exit(1)
    else:
        print("\n✅ Build complete! Files are in 'dist/' directory")
        print("💡 Next steps:")
        print("   - Test upload: python build_and_upload.py --test")
        print("   - Production:  python build_and_upload.py --prod")

if __name__ == "__main__":
    main()
