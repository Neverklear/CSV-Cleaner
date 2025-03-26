# CSV Converter for SQLite

This Python script converts CSV files that use backslash-escaped quotes (e.g. `\"`) into a format that is appropriate for SQLite's CSV importer. SQLite expects fields to be terminated by commas, enclosed by double quotes, and any literal double quotes within a field must be doubled (i.e. `""`).

## Overview

Some CSV files are generated with backslash-escaped quotes. For example, a field might be written as:

"And God said, "Let there be an expanse between the waters to separate water from water.""

SQLite's importer does not recognize `\"` as an escape sequence. It expects:


This script reads your CSV file with backslash escapes and outputs a corrected version that follows the CSV standard for SQLite.

## Features

- Reads CSV files using the backslash (`\`) as the escape character.
- Writes out a new CSV file with correctly doubled quotes.
- Uses Python’s built-in `csv` module for reliable parsing and writing.
- Simple command-line interface.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Neverklear/CSV-Cleaner
   cd CSV-Cleaner

2. Make sure you have Python installed on your system.

   ##Usage
Run the script from the command line by providing the input CSV file and the desired output CSV file as arguments:
   
python convert_csv.py input.csv output.csv

## Example

Suppose you have an input file data.csv with the following line:

1,1,6,"And God said, \"Let there be an expanse between the waters to separate water from water.\""

After running:
python convert_csv.py data.csv corrected_data.csv
The output in corrected_data.csv will be:
1,1,6,"And God said, ""Let there be an expanse between the waters to separate water from water."""

This correctly formatted CSV can now be imported into SQLite using:
.fields terminated by ',' enclosed by '"' lines terminated by '\n'

## Description
This script was created to automate the process of converting CSV files that use backslash-escaped quotes into a format acceptable for SQLite's CSV importer. According to the SQLite documentation, fields should be enclosed in double quotes and any literal quotes within fields should be doubled. This script reads the input CSV using escapechar='\\' and writes out a new CSV file where any literal quotes are properly doubled, ensuring that your CSV files import correctly into SQLite.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## License
This project is licensed under the MIT License.


