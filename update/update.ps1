$latestRelease = Invoke-RestMethod -Uri "https://api.github.com/repos/Atropa-Solanaceae/proXXy/releases/latest" | Select-Object -ExpandProperty tag_name
$scriptVersion = $env:SCRIPT_VERSION

Write-Output "`n--- Update Check ---"
Write-Output "Current Version : $scriptVersion"
Write-Output "Updating to    : $latestRelease"

if ($scriptVersion -eq $latestRelease) {
    Write-Output "`nYou are already up to date!`n"
    exit 0
}

$repoUrl = "https://github.com/Atropa-Solanaceae/proXXy"

Write-Output "`n--- Checking Requirements ---"
$requirements = @("python", "git", "pip")
foreach ($requirement in $requirements) {
    if (-not (Get-Command $requirement -ErrorAction SilentlyContinue)) {
        Write-Output "$requirement is required but not installed. Aborting.`n"
        exit 1
    }
}

if (Test-Path "proXXy") {
    Write-Output "`nUpdating existing repository..."
    Set-Location "proXXy"
    git pull origin
} else {
    Write-Output "`nCloning repository..."
    git clone $repoUrl "proXXy"
    Set-Location "proXXy"
}

Write-Output "`nInstalling required packages..."
pip install -r requirements.txt --quiet

Write-Output "`nCopying files..."
Copy-Item -Path .\* -Destination .. -Recurse -Force

Write-Output "`n--- Cleanup ---"
Write-Output "Cleaning up temporary files and folders..."
Set-Location ..
Remove-Item -Path "proXXy" -Recurse -Force
Write-Output "Cleanup completed.`n"

Write-Output "`n--- Update Completed ---"
Write-Output "`nUpdate completed. $scriptVersion -> $latestRelease`n"
