#!/bin/bash

echo "[*] Updating proXXy..."

REPO_URL="https://github.com/Atropa-Solanaceae/proXXy"
REPO_DIR="proXXy"
REQUIREMENTS_FILE="requirements.txt"

check_dependencies() {
    command -v git &>/dev/null || { echo >&2 "[-] git is required but not installed. Aborting."; exit 1; }
    command -v pip &>/dev/null || { echo >&2 "[-] pip is required but not installed. Aborting."; exit 1; }
}

update_repository() {
    if [ -d "$REPO_DIR" ]; then
        echo "[*] Updating existing repository..."
        cd "$REPO_DIR" || exit
        git pull origin
    else
        echo "[*] Cloning repository..."
        git clone "$REPO_URL" "$REPO_DIR"
        cd "$REPO_DIR" || exit
    fi
}

install_requirements() {
    echo "[*] Installing required packages..."
    pip install -r "$REQUIREMENTS_FILE"
}

copy_files() {
    echo "[*] Copying files..."
    cp -R ./* ..
}

clean_up() {
    echo "[*] Cleaning up..."
    cd ..
    rm -rf "$REPO_DIR"
}

main() {
    check_dependencies
    update_repository
    install_requirements
    copy_files
    clean_up
    echo "[+] Update completed."
}

main