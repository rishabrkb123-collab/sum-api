@echo off
setlocal EnableExtensions EnableDelayedExpansion

set PORT=5000

:find_port
netstat -ano | findstr /R /C:":!PORT! .*LISTENING" >nul
if not errorlevel 1 (
    set /a PORT+=1
    goto find_port
)

echo Starting server on port !PORT!...
set PORT=!PORT!
python app.py
