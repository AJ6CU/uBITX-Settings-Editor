# EEPROM BACKUP/RESTORER/UPDATER FOR SYSTEMS RUNNING KD8CEC

## Purpose
This project is to provide a platform independent, open-source replacement for the KD8CEC uBITX Memory Manager (see http://hamskey.com). The uBITX Memory Manager provides the means to manage the system parameters that the KD8CEC software maintains in EEPROM (on chip for the Arduino Nano, off chip for future other MCU's). The uBITX Memory Manager also provides the critical ability to backup and restore the contents of the EEPROM. 

Unfortunately, and unlike all the rest of the KD8CEC family of software, the source code to the uBITX Memory manager was never released nor was it natively ported to platforms other than Windows. The last release of the tool (V1.110) happened about 3.5 years ago. 

The latest release of uBITX Memeory Manager is hosted at:
https://github.com/phdlee/ubitx/releases/download/v1.11/uBITX_Manager_V1.11.zip

I had originally not planned to tackle this task. However, in porting KD8CEC v1.2 to new hardware platforms, the uBITX Memory Manager started to show what looked like incompatibilities (e.g., works with the Arduino IoT, fails with the Arduino BLE and RP Connect). So I was left with no choice but to take this detour...

## IMPLEMENTATION
The code is being written in Python. Eventually, using standard Python tools, I expect to be able to generate an executable for Windows, MacOS, and Linux. This family tools is envisioned to be 3 programs:

The screenshot below shows a snapshot of the work in progress. Unfortunately, it is taking longer to reverse engineer the uBTIX Memory Manager than I hoped.


![afterloading](https://user-images.githubusercontent.com/70183884/213938796-80d7aedb-5dc3-4eef-a46d-faeb88d0f750.JPG)

There are additional screenshots in the uBITXmodeditor/screenshots directory.

## USING THE TOOLS
To use either tool at this stage, you need to know how to use an editor, install python packages, and run python. I happen to be using PyCharm, but admit my ignorance might have led me not to choose the optimal tool. Specific values that need to be changes, are identified in the README files in the appropriate directory.

I can be reached with thru my email on QRZ or thru topics on the groups.io BITX20 group. You should also be able to raise Issues on the GitHub. Let me know if you have an issue here.

73
Mark
AJ6CU  

Copyright (C) 2022,  Mark Hatch

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
