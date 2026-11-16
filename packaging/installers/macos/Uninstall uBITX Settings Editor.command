#!/bin/zsh
# Removes uBITX Settings Editor installed by "Install uBITX Settings Editor.command".
# Your backup and settings files are not touched.
APP="uBITX Settings Editor"
rm -rf "$HOME/Library/Application Support/$APP" "$HOME/Applications/$APP.app"
print; print -- "$APP removed. Your backup and settings files are not touched."
print; read -k1 "?Press a key to close."
