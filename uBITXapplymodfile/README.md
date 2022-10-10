# uBITXapplymodfile

This program is written using Python 3.10.4 on Windows. It requires the installation of the following standard Python libraries:
- pySerial 
- lxml
- bitarray libraries. Let me know if you find any other unusual dependencies.

The user configurable settings are in "applymod_userconfig.py". 

You should only need to modify two variables to run this:

COM_PORT = "COM24"
USERMODFILE="usermodfile.xml"                       

You should replace COM24 with the COM port that your uBITX comes up at when connected to your computer via USB.
A possible MacOS com port is also provided but is commented out with a prefix of "#". 


This program will work by reading a "usermodfile" XML file and applying the contents of this file to EEPROM. The "usermodfile" should be created using the uBITXgeneratemodfile application. The usermodfile is XML based and can be edited by your favorite text editor. However, I would recommend an editor either optimized for XML or an editor with an addon XML plugin to reduce. 

The title of each setting. For example, the initial boot up frequency for VFO A is "VFO_A". Look for the following:


	<SETTING NAME="VFO_A">
        	<label>VFO A Bootup Freq</label>
        	<value>7032000</value>
        <!--A valid frequency (only numbers) that uBITX can set - e.g., 14032000-->
    	</SETTING>

- \<label\>VFO A Bootup Freq\<\\label\>:   is a brief description of the function of the setting, perhaps what you might see in a fancier UX.
- \<value\>7032000\<\\value\>:             the 7032000 is the frequency for the VFO A on boot.
- \<!--  comment --\>:                     hopefully more detail explanation of setting an options that can be used 

BTW: CASE MATTERS!

Once installed, you should only have to modify "userconfig.py" This contains the commonly modified parameters that you might need to change

COM_PORT = "COM14"  	Change this to the com port your uBTIX is attached to your computer 

BAUD = 38400		You *should* not change this unless your know what you are doing. CEC is looking for 38400 serial baud

USERMODFILE = "usermodfile.xml"		The file name where your modfile is saved. Should have an XML suffix



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
