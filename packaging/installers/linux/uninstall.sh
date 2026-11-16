#!/usr/bin/env bash
# Removes uBITX Settings Editor installed by install.sh. Your backup and
# settings files are not touched.
set -u
rm -rf "$HOME/.local/share/ubitx-settings-editor"
rm -f "$HOME/.local/bin/ubitx-settings-editor" "$HOME/.local/share/applications/ubitx-settings-editor.desktop"
command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$HOME/.local/share/applications" >/dev/null 2>&1
printf '\nuBITX Settings Editor removed. Your backup and settings files are not touched.\n'
