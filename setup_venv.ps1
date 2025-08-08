# Robot Behavior Simulator - Virtual Environment Setup (PowerShell)
Write-Host "🐍 Robot Behavior Simulator - Virtual Environment Setup" -ForegroundColor Green
Write-Host "====================================================="

Write-Host ""
Write-Host "📋 Step 1: Creating virtual environment..." -ForegroundColor Yellow

try {
    & py -m venv venv 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "🔄 Trying with 'python' command..." -ForegroundColor Yellow
        & python -m venv venv
        if ($LASTEXITCODE -ne 0) {
            throw "Failed to create virtual environment"
        }
    }
    Write-Host "✅ Virtual environment created successfully!" -ForegroundColor Green
}
catch {
    Write-Host "❌ Failed to create virtual environment" -ForegroundColor Red
    Write-Host "💡 Please install Python from https://python.org/downloads/" -ForegroundColor Yellow
    Write-Host "   Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Read-Host "Press Enter to continue"
    exit 1
}

Write-Host ""
Write-Host "📋 Step 2: Activating virtual environment..." -ForegroundColor Yellow

try {
    & .\venv\Scripts\Activate.ps1
    Write-Host "✅ Virtual environment activated!" -ForegroundColor Green
}
catch {
    Write-Host "❌ Failed to activate virtual environment" -ForegroundColor Red
    Write-Host "💡 You may need to run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Yellow
    Read-Host "Press Enter to continue"
    exit 1
}

Write-Host ""
Write-Host "📋 Step 3: Upgrading pip..." -ForegroundColor Yellow
& python -m pip install --upgrade pip
Write-Host "✅ Pip upgraded!" -ForegroundColor Green

Write-Host ""
Write-Host "📋 Step 4: Installing build tools..." -ForegroundColor Yellow
& pip install build twine pytest
Write-Host "✅ Build tools installed!" -ForegroundColor Green

Write-Host ""
Write-Host "📋 Step 5: Installing package in development mode..." -ForegroundColor Yellow
& pip install -e .
Write-Host "✅ Package installed!" -ForegroundColor Green

Write-Host ""
Write-Host "📋 Step 6: Testing package..." -ForegroundColor Yellow
try {
    & python -c "from robot_behavior import create_robot_program; print('✅ Package import successful!')"
    if ($LASTEXITCODE -ne 0) {
        throw "Package test failed"
    }
}
catch {
    Write-Host "❌ Package test failed" -ForegroundColor Red
    Read-Host "Press Enter to continue"
    exit 1
}

Write-Host ""
Write-Host "🎉 Setup complete! Your virtual environment is ready." -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Next steps:" -ForegroundColor Cyan
Write-Host "   1. To activate: .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "   2. To build: python -m build" -ForegroundColor White
Write-Host "   3. To upload to TestPyPI: python -m twine upload --repository testpypi dist/*" -ForegroundColor White
Write-Host ""
Write-Host "📖 For detailed instructions, see PYTHON_SETUP_GUIDE.md" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to continue"
