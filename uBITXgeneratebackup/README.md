# uBITXgeneratebackup

This program was written using Python 3.10.4 on Windows. It requires the pySerial library to be included. Let me know if you find any other unusal dependencies.

You should only need to modify two variables to run this:

COM_PORT = "COM14"

BACKUPFILE= "binarybackupdump.btx"

You should replace COM14 with the COM port that your uBITX comes up at when connected to your computer via USB. Your choice on the backupfile name. Just remember to maintain compatibility with the original uBITX Memory Manager, you need to keep the ".btx" extension. Also don't go messing with the file in a binary editor. Yes, I know that the second 1024 bytes (of the 2048 byte length file) are just zeros. But the uBITX Memory Manager likes it that way and I wanted to maint compatibility.

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
