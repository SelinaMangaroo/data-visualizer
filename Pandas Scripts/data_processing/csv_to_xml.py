import csv
import xml.etree.ElementTree as ET

csv_file = 'xml_data/winona_data/2_processed_csv/processed_winona_photos.csv'
xml_file = 'processed_winona_photos.xml'

# create XML tree
root = ET.Element('data')

# open CSV file and read data
with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # create XML element for each row
        item = ET.SubElement(root, 'item')
        for key, value in row.items():
            # create XML subelement for each column
            subitem = ET.SubElement(item, key)
            subitem.text = value

# write XML tree to file
tree = ET.ElementTree(root)
tree.write(xml_file)