#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p ../dist/dmg
# Empty the dmg folder.
rm -r ../dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r ../dist/uBITX_Settings_Editor.app ../dist/dmg
# If the DMG already exists, delete it.
test -f ../dist/uBITX_Settings_Editor.dmg && rm ../dist/uBITX_Settings_Editor.dmg
#  --volicon "./settingseditor.icns" \
create-dmg \
  --volname "Settings Editor" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "uBITX_Settings_Editor.app" 175 120 \
  --hide-extension "uBITX_Settings_Editor.app" \
  --app-drop-link 425 120 \
  "../dist/uBITX_Settings_Editor.dmg" \
  "../dist/dmg/"

