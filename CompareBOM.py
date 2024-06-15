import pandas as pd
import os

# Get the current working directory
current_dir = os.getcwd()


# Specify the full file paths
file_path1 = os.path.join(current_dir, 'bom1.xlsx')
file_path2 = os.path.join(current_dir, 'bom2.xlsx')

# Load the BOMs
bom1 = pd.read_excel(file_path1)
bom2 = pd.read_excel(file_path2)

# Merge on 'Part Number'
merged_bom = pd.merge(bom1, bom2, on='Part Number', suffixes=('_BOM1', '_BOM2'))

# Find mismatches
differences = merged_bom[
    (merged_bom['Revision_BOM1'] != merged_bom['Revision_BOM2']) |
    (merged_bom['Part Description_BOM1'] != merged_bom['Part Description_BOM2']) |
    (merged_bom['Quantity_BOM1'] != merged_bom['Quantity_BOM2'])
]

# Save the differences to a new Excel file
differences.to_excel('bom_differences.xlsx', index=False)