import os
import xml.etree.ElementTree as ET
import pandas as pd
from collections import OrderedDict

# assign directory of xml files
xml_directory = 'xml_data/Data_Import/0_xml'

# assign directory to write the csv files to
# csv_directory = '/Users/selinamangaroo/Desktop/Pandas Scripts/xml_data/Data_Import/0_xml/1_csv'

# Assign directory to write the CSV files to, placed alongside the `0_xml` directory
csv_directory = os.path.join(os.path.dirname(xml_directory), '1_csv')

# Ensure the output directory exists
os.makedirs(csv_directory, exist_ok=True)

for filename in os.listdir(xml_directory):
    # Full path to the current XML file
    xml_file_path = os.path.join(xml_directory, filename)
    if os.path.isfile(xml_file_path):
        print(xml_file_path)
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        cols = []
        rows = []

        for x in root:
            d = {}
            for y in x:
                cols.append(y.tag)
                d["{0}".format(y.tag)] = y.text
            rows.append(d)

        # Remove repeated columns
        cols = list(OrderedDict.fromkeys(cols))

        # Create DataFrame
        df = pd.DataFrame(rows, columns=cols)

        # Drop first column and row
        df = df.iloc[1:]
        df = df.iloc[:, 1:]

        print(df.count())
        
        # Generate output CSV file path
        base_filename = os.path.splitext(filename)[0]  # Strip XML file extension
        csv_file_path = os.path.join(csv_directory, f'{base_filename}.csv')

        # Write DataFrame to CSV
        df.to_csv(csv_file_path, index=False)

# for filename in os.listdir(xml_directory):
#     f = os.path.join(xml_directory, filename)
#     if os.path.isfile(f):
#         print(f)
#         tree = ET.parse(f)
#         root = tree.getroot()
        
#         cols = []
#         rows = []

#         for x in root:
#             d = {}
#             for y in x:
#                 cols.append(y.tag)
#                 d["{0}".format(y.tag)] = y.text
#             rows.append(d)

#         # remove repeated cols
#         cols = list(OrderedDict.fromkeys(cols))

#         #create dataframe
#         df = pd.DataFrame(rows, columns=cols)

#         #drop first col and row
#         df = df.iloc[1:]
#         df = df.iloc[: , 1:]

#         print(df.count())
        
#         # strip xml file extension
#         tempTuple = os.path.splitext(f)
#         f = tempTuple[0]

#         # Writing dataframe to .csv file
#         df.to_csv(f'{f}.csv')

# --------------------------------------------------------------------------------- #

# If when running you receive the error: "not well-formed (invalid token)"
# Run the "zap gremlins" command in BBEdit on problematic xml file 

# to remove .DS_Store files, go to the directory containing the file
# run command:  find . -name '.DS_Store' -type f -delete