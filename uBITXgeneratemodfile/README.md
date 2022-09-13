# uBITXgeneratemodfile

This program will be written using Python 3.10.4 on Windows. It requires the pySerial and the lxml libraries. Let me know if you find any other unusual dependencies.

This program will work by reading from your EEPROM and merging the resulting values into an XML template file that will provide you with a "MOD File. You can then use your favorite ediotr (preferably one with support for XML) and modify/change values (see the <value></value> tage) 

At this point, I just have the template file available (see usermodfiletemplate.xml in this directory) for your reference. This is still a work in progress and this file is in no way final. I am aware of several inconsistencies (e.g. how I  use all three of "true", "yes" and "1"). If you spot other areas of improvements, I would be happy to hear from you.

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
