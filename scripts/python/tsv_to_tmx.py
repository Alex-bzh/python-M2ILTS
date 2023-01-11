#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# modules to import
#

import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import csv

#
# user functions
#

def pretty_print(xml, path):
	"""Pretty print XML tree into a TMX file

	xml_tree -- an ElementTree object
	"""
	xmlstr = minidom.parseString(ET.tostring(xml)).toprettyxml()

	with open(path, "w") as xmlfile:
		xmlfile.write(xmlstr)

# main function
def main(filename):

	# <root> element
	root = ET.Element("tmx")

	# <header> element
	header = ET.SubElement(root, "header", {
		"creationtool": str(),
		"creationtoolversion": str(),
		"segtype": str(),
		"o-tmf": str(),
		"adminlang": str(),
		"srclang": str(),
		"datatype": str()
	})

	# <body> element
	body = ET.SubElement(root, "body")

	# data is in TSV file
	with open(filename) as csvfile:
		# reading data with appropriate module
		reader = csv.DictReader(csvfile, delimiter="\t")

		# for each row in TSV file
		for idx, row in enumerate(reader):
			# create a <tu> element
			tu = ET.SubElement(body, "tu", { "tuid": f"s{ idx }"})

			# for each column (a variant in a particular language)
			for lang, segment in row.items():
				# create <tuv> and <seg> elements
				tuv = ET.SubElement(tu, "tuv", { "xml:lang": lang })
				seg = ET.SubElement(tuv, "seg")
				seg.text = segment

	# XML tree into a TMX file
	pretty_print(root, filename.replace('.tsv', '.tmx'))

# program
if __name__ == "__main__":

	# filename
	filename = "../../data/CSV/ftb_N+A.tsv"

	# execute main procedure
	main(filename)
