#!/bin/sh
test -f ../dist/uBITX_Settings_Editor.zip && rm ../dist/uBITX_Settings_Editor.zip
ditto -c -k --keepParent ../dist/uBITX_SETTINGS_EDITOR.app ../dist/uBITX_Settings_Editor.zip
xcrun notarytool submit ../dist/uBITX_Settings_Editor.zip --keychain-profile "ubitxmac" --wait
