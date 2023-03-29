# uBITX Settings Editor Project

## Purpose
This project is to provide a platform independent, open-source replacement for the KD8CEC uBITX Memory Manager (see http://hamskey.com). The uBITX Memory Manager provides the means to manage the system parameters that the KD8CEC software maintains in EEPROM (on chip for the Arduino Nano, off chip for future other MCU's).  

Unfortunately, and unlike all the rest of the KD8CEC family of software, the source code to the uBITX Memory manager was never released nor was it natively ported to platforms other than Windows. 

The last release of uBITX Memeory Manager is hosted at:
https://github.com/phdlee/ubitx/releases/download/v1.11/uBITX_Manager_V1.11.zip

I had originally not planned to tackle this task. However, in porting KD8CEC v1.2 to new hardware platforms, the uBITX Memory Manager started to show what looked like incompatibilities (e.g., works with the Arduino IoT, fails with the Arduino BLE and RP Connect). So I was left with no choice but to take this detour...

## IMPLEMENTATION
The code is being written in Python. Eventually, using standard Python tools. I have released a beta 1 for Windows, MacOS(Intel),  and Linux (Arm and Intel). download it here:

https://github.com/AJ6CU/uBITX-EEPROM-Manager/releases/tag/V2-beta-1


![afterloading](https://user-images.githubusercontent.com/70183884/228396270-d2e30b42-a545-4171-846f-5ddc9a842f30.JPG)


There are additional screenshots in the uBITXmodeeditor/screenshots directory.

## Obsolete Programs
Only the software in the uBITX_Settings_Editor directory is under active development. 

## Contact Me

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
