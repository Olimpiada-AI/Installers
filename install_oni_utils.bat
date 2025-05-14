@echo off
setlocal EnableDelayedExpansion

@echo off
setlocal
set PYTHON_VERSION=3.11.5
set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%
set VSCODE_INSTALLER=VSCodeUserSetup-x64.exe
set VSCODE_URL=https://update.code.visualstudio.com/latest/win32-x64-user/stable

echo ==================================================
echo Installing Python %PYTHON_VERSION% and Visual Studio Code
echo ==================================================

:: Download Python installer if not exists
if not exist %PYTHON_INSTALLER% (
    echo [INFO] Downloading Python %PYTHON_VERSION%...
    powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'"
)

:: Install Python silently
echo [INFO] Installing Python...
start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 SimpleInstall=1

:: Verify Python
echo [INFO] Verifying Python installation...
python --version

:: Download VSCode installer if not exists
if not exist %VSCODE_INSTALLER% (
    echo [INFO] Downloading Visual Studio Code...
    powershell -Command "Invoke-WebRequest -Uri '%VSCODE_URL%' -OutFile '%VSCODE_INSTALLER%'"
)

:: Install VSCode silently
echo [INFO] Installing Visual Studio Code...
start /wait %VSCODE_INSTALLER% /silent /mergetasks=!runcode

:: Done
echo [SUCCESS] Python %PYTHON_VERSION% and VS Code installed.
pause
