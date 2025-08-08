# 🐍 Python Virtual Environment Setup Guide

## Current Issue
Your project doesn't have a virtual environment set up, and there seems to be an issue with creating one using the current Python installation.

## 🛠️ Solution: Set Up Virtual Environment Properly

### **Step 1: Install Python (if needed)**

If you're getting Python installation errors, download Python from:
- **Official Python**: https://python.org/downloads/
- **Choose**: Python 3.8+ (recommended: Python 3.11 or 3.12)
- **Important**: During installation, check "Add Python to PATH"

### **Step 2: Create Virtual Environment**

Open PowerShell in your project directory (`d:\Robot-behavior`) and run:

```powershell
# Method 1: Using python command
python -m venv venv

# Method 2: Using py launcher (Windows)
py -m venv venv

# Method 3: If above fail, try with full path
C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe -m venv venv
```

### **Step 3: Activate Virtual Environment**

```powershell
# On Windows PowerShell
.\venv\Scripts\Activate.ps1

# On Windows Command Prompt
venv\Scripts\activate.bat

# You should see (venv) in your prompt
```

### **Step 4: Install Required Packages**

```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install build tools
pip install build twine

# Install development dependencies
pip install pytest

# Install your package in development mode
pip install -e .
```

### **Step 5: Verify Installation**

```powershell
# Check Python version
python --version

# Check installed packages
pip list

# Test your package
python -c "from robot_behavior import create_robot_program; print('✅ Package works!')"
```

## 🚀 **Publishing Workflow (After Virtual Environment Setup)**

Once your virtual environment is working:

```powershell
# 1. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 2. Build package
python -m build

# 3. Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# 4. Test installation
pip install --index-url https://test.pypi.org/simple/ robot-behavior-simulator
```

## 🔧 **Alternative: Using Conda**

If you have Anaconda/Miniconda installed:

```powershell
# Create conda environment
conda create -n robot-behavior python=3.11

# Activate environment
conda activate robot-behavior

# Install packages
pip install build twine pytest

# Install your package
pip install -e .
```

## 📁 **Expected Project Structure After Setup**

```
d:\Robot-behavior\
├── venv/                    # ← Virtual environment (new)
│   ├── Scripts/
│   ├── Lib/
│   └── ...
├── .gitignore              # Already configured to ignore venv/
├── pyproject.toml          # ✅ Ready
├── README.md               # ✅ Ready  
├── robot_behavior/         # ✅ Ready
├── examples/               # ✅ Ready
├── tests/                  # ✅ Ready
└── docs/                   # ✅ Ready
```

## ⚠️ **Troubleshooting**

### Python Not Found
- Reinstall Python from python.org
- Make sure "Add Python to PATH" is checked
- Restart PowerShell after installation

### Permission Issues
- Run PowerShell as Administrator
- Or use: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Virtual Environment Creation Fails
- Try different Python versions: `py -3.11 -m venv venv`
- Use Anaconda instead: Download from anaconda.com

## 🎯 **Next Steps**

1. **Set up virtual environment** using the steps above
2. **Activate it** and install dependencies
3. **Test the package** works locally
4. **Build and upload** to TestPyPI

Your package structure is perfect - you just need the virtual environment setup! 🚀
