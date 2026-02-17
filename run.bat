batch@echo off
echo ============================================
echo    INSTAGRAM AUTO POST
echo ============================================
echo.

if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Run setup.bat first!
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
python instagram_auto_post.py
deactivate

pause
```