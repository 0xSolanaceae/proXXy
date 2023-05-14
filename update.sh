#!/bin/bash

REPO_URL="https://github.com/Atropa-Solanaceae/proXXy"
REPO_DIR="proXXy"

# Check if Git is installed
if ! command -v git &>/dev/null; then
    echo >&2 "Git is required but not installed. Aborting."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &>/dev/null; then
    echo >&2 "pip is required but not installed. Aborting."
    exit 1
fi

# Clone or update the repository
if [ -d "$REPO_DIR" ]; then
    echo "Updating existing repository..."
    cd "$REPO_DIR"
    git pull origin
else
    echo "Cloning repository..."
    git clone "$REPO_URL" "$REPO_DIR"
    cd "$REPO_DIR" || exit
fi

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

# Copy the updated files to the parent directory
echo "Copying files..."
cp -R ./* ..

# Clean up
echo "Cleaning up..."
cd ..
rm -rf "$REPO_DIR"

echo "Update completed."
