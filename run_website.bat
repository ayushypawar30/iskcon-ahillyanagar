@echo off
echo Starting ISKCON Website Server...
echo.
echo Please wait...
echo.
echo Once started, you can access the website at:
echo Local:   http://localhost:5000
echo Network: http://192.168.1.108:5000
echo.
echo DO NOT CLOSE THIS WINDOW while the website is in use.
echo.
python backend/app.py
pause
