#!/usr/bin/env bash
set -e

INSTALL_PATH="/usr/local/inkypi"

if [[ -d "$INSTALL_PATH" ]]; then
    echo "[INFO] Removing installation at $INSTALL_PATH..."
    sudo rm -rf "$INSTALL_PATH"
    echo "[INFO] Uninstallation complete."
else
    echo "[INFO] Nothing to uninstall. $INSTALL_PATH does not exist."
fi
