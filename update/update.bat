@echo off

echo Updating proXXy...

set REPO_URL="https://github.com/Atropa-Solanaceae/proXXy"
echo Checking for required software...

where python >nul 2>&1
if %errorlevel% neq 0 ( 
    echo Python is required but not installed. Aborting.
    exit /b 1
)

where git >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is required but not installed. Aborting.
    exit /b 1
)

where pip >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is required but not installed. Aborting.
    exit /b 1
)

if exist "proXXy" (
    echo Updating existing repository...
    cd proXXy || exit /b
    git pull origin
) else (
    echo Cloning repository...
    git clone %REPO_URL% proXXy
    cd proXXy || exit /b
)

echo Installing required packages...
pip install -r requirements.txt

echo Copying files...
xcopy /E /Y .\* ..

echo Cleaning up...
pushd ..
rmdir /S /Q proXXy
popd

echo Update completed, enjoy your new proXXy!