@echo off

set REPO_URL="https://github.com/Atropa-Solanaceae/proXXy"

REM Check if Git is installed
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is required but not installed. Aborting.
    exit /b 1
)

REM Clone or update the repository
if exist "proXXy" (
    echo Updating existing repository...
    cd proXXy || exit /b
    git pull origin master
    
) else (

    echo Cloning repository...
    git clone %REPO_URL% proXXy
    cd proXXy || exit /b
)

REM Copy the updated files to the current directory
echo Copying files...
xcopy /E /Y .\* ..

REM Clean up
echo Cleaning up...
pushd ..
rmdir /S /Q proXXy
popd

echo Update completed.
