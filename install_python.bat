@echo off
setlocal EnableDelayedExpansion

:: === Config ===
set "PYTHON_VERSION=3.11.5"
set "PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe"
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%"
set "SILENT=1"

:: === Colors ===
set "RED=0C"
set "RESET=07"

:: === Parse --gui flag ===
if "%1"=="--gui" (
    set "SILENT=0"
)

echo.
echo =============================================
echo [ONIA Setup] Installing Python and VS Code...
echo =============================================

:: --- Step 1: Detect Python on PATH (skip WindowsApps shims) ---
echo [INFO] Checking Python installation...
set "PYTHON_DETECTED="
set "PYTHON_VERSION_DETECTED="

for /F "usebackq delims=" %%P in (`where python 2^>nul`) do (
    echo Found candidate: %%P
    echo %%P | find /I "WindowsApps" >nul
    if errorlevel 1 (
        set "PYTHON_DETECTED=%%P"
        goto :got_real_python
    )
)

:got_real_python
if defined PYTHON_DETECTED (
    echo [INFO] Python detected at: !PYTHON_DETECTED!
    set "CMDLINE=""!PYTHON_DETECTED!" -c "import platform; print(platform.python_version())""
    for /F "delims=" %%V in ('cmd /s /c !CMDLINE!') do (
        set "PYTHON_VERSION_DETECTED=%%V"
    )
    echo [INFO] Detected version: !PYTHON_VERSION_DETECTED!
    if "!PYTHON_VERSION_DETECTED!"=="%PYTHON_VERSION%" (
        echo [OK] Required Python version %PYTHON_VERSION% is already installed.
        goto :python_done
    ) else (
        color %RED%
        echo [ERROR] Python version !PYTHON_VERSION_DETECTED! found, but %PYTHON_VERSION% is required.
        echo         PATH may point to the wrong version. Will reinstall Python.
        color %RESET%
    )
) else (
    echo [INFO] No valid Python found on PATH. Will install Python %PYTHON_VERSION%...
)

:: --- Step 2: Download Python installer if missing ---
if not exist "%PYTHON_INSTALLER%" (
    echo [INFO] Downloading Python %PYTHON_VERSION%...
    curl -L -o "%PYTHON_INSTALLER%" "%PYTHON_URL%"
)

:: --- Step 3: Install Python (GUI or Silent) ---
if "%SILENT%"=="1" (
    echo [INFO] Installing Python silently...
    start /wait "" "%PYTHON_INSTALLER%" ^
        /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 SimpleInstall=1 InstallLauncherAllUsers=1
) else (
    echo [INFO] Launching Python GUI installer...
    start /wait "" "%PYTHON_INSTALLER%"
)

:: --- Step 4: Ask to restart if PATH not updated ---
for /F "usebackq delims=" %%P in (`where python 2^>nul`) do (
    set "PYTHON_DETECTED=%%P"
)

if not defined PYTHON_DETECTED (
    color %RED%
    echo [ERROR] Python is still not in PATH.
    echo         Please close this window and reopen a terminal to refresh your PATH.
    color %RESET%
    pause
    exit /b 1
)

:python_done


echo [OK] Setup complete. You may now use Python if it was detected or close the terminal if not to proper init paths.
