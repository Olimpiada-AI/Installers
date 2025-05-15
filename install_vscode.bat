@echo off
setlocal EnableDelayedExpansion

:: === Configuration ===
set "VSCODE_URL=https://update.code.visualstudio.com/latest/win32-x64/stable"
set "VSCODE_INSTALLER=VSCodeUserSetup-x64.exe"
set "VSCODE_PATH=%LOCALAPPDATA%\Programs\Microsoft VS Code"
set "SILENT=1"

:: === Parse optional --gui flag ===
if "%~1"=="--gui" (
    set "SILENT=0"
)

echo.
echo =============================================
echo [ONIA Setup] Installing VS Code...
echo =============================================

:: --- Step 1: Download the installer if not present ---
if not exist "%VSCODE_INSTALLER%" (
    echo [INFO] Downloading VS Code...
    curl -L -o "%VSCODE_INSTALLER%" "%VSCODE_URL%"
)

:: --- Step 2: Install silently or with GUI ---
if not exist "%VSCODE_PATH%\Code.exe" (
    if "%SILENT%"=="1" (
        echo [INFO] Installing silently...
        start "" /wait "%CD%\%VSCODE_INSTALLER%" /verysilent /mergetasks=runcode
    ) else (
        echo [INFO] Launching GUI installer...
        start "" /wait "%CD%\%VSCODE_INSTALLER%"
        echo Please complete the installation, then press any key to continue...
        pause >nul
    )
)

:: --- Step 3: Install extensions ---
set "CODE_CMD=%VSCODE_PATH%\bin\code.cmd"
echo [INFO] Installing VS Code extensions...

if exist "%CODE_CMD%" (
    call "%CODE_CMD%" --install-extension ms-python.python --force
    call "%CODE_CMD%" --install-extension ms-python.vscode-pylance --force
    call "%CODE_CMD%" --install-extension ms-toolsai.jupyter --force
) else (
    echo [WARN] VS Code not found at: %CODE_CMD%
    echo        Install extensions manually if needed.
)

echo.
echo [OK] VS Code setup complete.
pause
exit /b 0
