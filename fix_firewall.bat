@echo off
echo Attempting to open Port 5000 for ISKCON Website...
echo.
echo This requires Administrator privileges.
echo If asked, please click "Yes" to allow changes.
echo.
powershell -Command "New-NetFirewallRule -DisplayName 'ISKCON Website' -Direction Inbound -LocalPort 5000 -Protocol TCP -Action Allow"
echo.
echo Done! If you saw no red errors, the port is open.
pause
