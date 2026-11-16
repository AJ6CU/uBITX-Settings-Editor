#!/bin/sh
xcrun notarytool submit ../dist/uBITX_Settings_Editor.dmg --keychain-profile "ubitxmac" --wait
