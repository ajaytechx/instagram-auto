@echo off
echo ============================================
echo    INSTAGRAM AUTO POST - SETUP
echo ============================================
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not installed!
    echo Please install from python.org
    pause
    exit /b 1
)
echo [OK] Python found
echo.

echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo [OK] Virtual environment created
) else (
    echo [OK] Virtual environment exists
)
echo.

echo Activating and installing packages...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ============================================
echo    SETUP COMPLETE!
echo ============================================
echo.
echo Next steps:
echo 1. Add images to 'images' folder
echo 2. Add captions to 'captions' folder
echo 3. Run 'run_coordinates.bat'
echo 4. Update config.py with coordinates
echo 5. Run 'run.bat'
echo.
pause