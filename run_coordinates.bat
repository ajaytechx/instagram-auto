@echo off
echo ============================================
echo    COORDINATE FINDER
echo ============================================
echo.

if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Run setup.bat first!
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
python find_coordinates.py
deactivate

pause
```

