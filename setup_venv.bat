@echo off
echo 🐍 Robot Behavior Simulator - Virtual Environment Setup
echo =====================================================

echo.
echo 📋 Step 1: Creating virtual environment...
py -m venv venv
if %ERRORLEVEL% neq 0 (
    echo ❌ Failed to create virtual environment with 'py'
    echo 🔄 Trying with 'python'...
    python -m venv venv
    if %ERRORLEVEL% neq 0 (
        echo ❌ Failed to create virtual environment
        echo 💡 Please install Python from https://python.org/downloads/
        echo    Make sure to check "Add Python to PATH" during installation
        pause
        exit /b 1
    )
)
echo ✅ Virtual environment created successfully!

echo.
echo 📋 Step 2: Activating virtual environment...
call venv\Scripts\activate.bat
if %ERRORLEVEL% neq 0 (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✅ Virtual environment activated!

echo.
echo 📋 Step 3: Upgrading pip...
python -m pip install --upgrade pip
echo ✅ Pip upgraded!

echo.
echo 📋 Step 4: Installing build tools...
pip install build twine pytest
echo ✅ Build tools installed!

echo.
echo 📋 Step 5: Installing package in development mode...
pip install -e .
echo ✅ Package installed!

echo.
echo 📋 Step 6: Testing package...
python -c "from robot_behavior import create_robot_program; print('✅ Package import successful!')"
if %ERRORLEVEL% neq 0 (
    echo ❌ Package test failed
    pause
    exit /b 1
)

echo.
echo 🎉 Setup complete! Your virtual environment is ready.
echo.
echo 🚀 Next steps:
echo    1. To activate: venv\Scripts\activate.bat
echo    2. To build: python -m build
echo    3. To upload to TestPyPI: python -m twine upload --repository testpypi dist/*
echo.
echo 📖 For detailed instructions, see PYTHON_SETUP_GUIDE.md
echo.
pause
