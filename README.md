# BOM Comparison Script

This Python script compares two Bill of Materials (BOMs) in Excel format and identifies any differences between them. It uses the `pandas` library for data manipulation and `openpyxl` for handling Excel files.

## Setup

### Prerequisites

- Python 3.x installed on your system
- `pandas` and `openpyxl` Python libraries installed. You can install them using pip:

  
### Files Required

- `bom1.xlsx`: First BOM file to compare.
- `bom2.xlsx`: Second BOM file to compare.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine or download the `CompareBOM.py` script.

2. **Place BOM Files**: Ensure `bom1.xlsx` and `bom2.xlsx` are placed in the same directory as `CompareBOM.py` or specify their full paths in the script.

3. **Run the Script**:


4. **Output**:
- The script will compare the BOMs based on the 'Part Number' column.
- It will identify mismatches in 'Revision', 'Part Description', and 'Quantity' between the two BOMs.
- Differences will be saved to `bom_differences.xlsx` in the same directory.

## Example

Assuming `bom1.xlsx` and `bom2.xlsx` contain different data for some parts, running the script will generate `bom_differences.xlsx` with detailed comparison results.

## Notes

- Ensure `bom1.xlsx` and `bom2.xlsx` have consistent column names ('Part Number', 'Revision', 'Part Description', 'Quantity') for accurate comparison.
- This script assumes that both BOMs have a common 'Part Number' column for merging and comparison.
