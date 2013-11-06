#! /usr/bin/env python
# field_notes_kml.py by Marek Borowiec

# This program takes AntWeb format flat files as input and annotates them as a KML file 
# It assumes the file has a header. 
# If there is none, change the line "if LineNumber >= 1:" to "if LineNumber >= 0:"

import sys
from sys import argv
import re
import string

if len(sys.argv) < 2:
        print "Use: field_notes_kml.py your_filename.txt"
        sys.exit()
else: 
        script, InFileName = argv

# Open the input file for reading
InFile = open(InFileName, 'r')


# Initialize the counter used to keep track of line numbers
LineNumber = 0

OutFileName = InFileName + '.kml'
OutFile = open(OutFileName, 'w') # You can append instead with 'a'

Headstring = '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<kml xmlns=\"http://earth.google.com/kml/2.2\">
<Document>
'''

OutFile.write(Headstring)

# Loop through each line in the file
for Line in InFile:
	if LineNumber	>= 1:
		# Remove the line-ending characters
		Line = Line.strip('\n')
		# Translating characters such as <>& that cannot 
		#be interpreted correctly by a KML reader		
		Line = re.sub(r'<', 'under', Line)
		Line = re.sub(r'>', 'over', Line)
		Line = re.sub(r'&', 'and', Line)
		ElementList = Line.split('\t')	
		#print ElementList
		Specimen_code = ElementList[0]
		Subfamily = ElementList[1]
		Genus = ElementList[2]
		Species = ElementList[3]
		Life_stage_sex = ElementList[4]
		Medium = ElementList[5]
		Specimen_notes = ElementList[6]
		DNA_notes = ElementList[7]
		Located_at = ElementList[8]
		Owned_by = ElementList[9]
		Type_status = ElementList[10]
		Determined_by = ElementList[11]
		Date_determined = ElementList[12]
		Coll_code = ElementList[13]
		Collector = ElementList[14]
		Date = ElementList[15]
		Coll_date_end = ElementList[16]
		Coll_method = ElementList[17]
		Habitat = ElementList[18]
		Localization_microhabitat = ElementList[19]
		Coll_notes = ElementList[20]
		Locality_proper = ElementList[21]
		Adm1 = ElementList[22]
		Adm2 = ElementList[23]
		Country = ElementList[24]
		Elevation = ElementList[25]
		Elev_error = ElementList[26]
		Loc_lat = float(ElementList[27])
		Loc_long = float(ElementList[28])
		Lat_long_error = ElementList[29]
		Biogeo_region = ElementList[30]
		Additional_habitat_notes = ElementList[31]
		Loc_code = ElementList[32]

		PlacemarkString = '''
<Placemark>
 <name>%s %s - %s</name>
 <description>%s</description>
 <Point>
  <altitudeMode>absolute</altitudeMode>
  <coordinates>%.6f, %.6f, %s</coordinates>
 </Point>
</Placemark>''' % (Genus, Species, Coll_code, Line, Loc_long, Loc_lat, Elevation)
		#OutString = "%s\t%4s\t%.5f\t%10.6f\t%9s\t%s" % (Dive, Depth, LatDegrees, LonDegrees, Date, Comment)
		#print OutString
		#OutFile.write(OutString + "\n")
		OutFile.write(PlacemarkString)
		#Index the counter used to keep track of line numbers
	LineNumber += 1

# After the loop is completed, close the file
InFile.close()

OutFile.write('\n</Document>\n</kml>\n')
OutFile.close()
 
print """
Your KML file has been saved as %r
""" % OutFileName

