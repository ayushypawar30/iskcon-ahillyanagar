@echo off
echo Generating Public Link (Attempt 2)...
echo.
echo Trying a different service (Pinggy.io) because the last one failed.
echo.
echo Look for a URL starting with "https://" in the output below.
echo.
ssh -o StrictHostKeyChecking=no -p 443 -R0:localhost:5000 a.pinggy.io
pause
