@echo off
setlocal

:: Set cache directory
set "CACHE_DIR=pip_cache_tfcpu"

echo.
echo Uninstalling existing tensorflow-cpu...
pip uninstall -y tensorflow-cpu

echo.
echo Installing tensorflow-cpu==2.15.0...

:: Check if cache folder exists
if exist "%CACHE_DIR%" (
    echo Using local cache folder: %CACHE_DIR%
    pip install tensorflow-cpu==2.15.0 --find-links="%CACHE_DIR%" --no-index
) else (
    echo Cache folder not found. Downloading and caching into: %CACHE_DIR%
    mkdir "%CACHE_DIR%"
    pip download tensorflow-cpu==2.15.0 -d "%CACHE_DIR%"
    pip install tensorflow-cpu==2.15.0 --find-links="%CACHE_DIR%" --no-index
)

echo.
echo Done.
endlocal
pause
