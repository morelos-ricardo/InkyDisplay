#!/usr/bin/env bash
set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_PATH="$PROJECT_DIR/src"
INSTALL_PATH="/usr/local/inkypi"

# Create install directory
mkdir -p "$INSTALL_PATH"

# Copy source files
cp -r "$SRC_PATH" "$INSTALL_PATH/src"

# Set executable permissions for scripts
chmod +x "$INSTALL_PATH/src/main.py"

echo "[INFO] Installation complete. You can run the startup display with:"
echo "       python3 $INSTALL_PATH/src/main.py"
