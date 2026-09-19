@echo off
echo ============================================
echo  Privacy-Preserving CDP - One-Click Setup
echo ============================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    echo Download from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during install
    pause
    exit /b 1
)
echo [OK] Python found

REM Install dependencies
echo.
echo Installing dependencies...
pip install fastapi uvicorn sqlalchemy python-dotenv python-multipart pydantic httpx
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed

REM Delete old databases
echo.
echo Cleaning old data...
del /q source.db 2>nul
del /q protected.db 2>nul
del /q vault.db 2>nul
echo [OK] Clean

REM Build dashboard
echo.
echo Building dashboard...
python build_dashboard.py
if %errorlevel% neq 0 (
    echo ERROR: Failed to build dashboard
    pause
    exit /b 1
)
echo [OK] Dashboard built

REM Start server
echo.
echo ============================================
echo  Starting Privacy-Preserving CDP...
echo  Open browser: http://localhost:8000
echo  Login: admin / admin123
echo ============================================
echo.
start http://localhost:8000
uvicorn app.main:app --host 127.0.0.1 --port 8000
