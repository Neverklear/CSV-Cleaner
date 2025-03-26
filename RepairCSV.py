#!/usr/bin/env python3
import csv
import sys

def main(input_filename, output_filename):
    # Open the input file and read it using escapechar='\\'
    with open(input_filename, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=',', quotechar='"', escapechar='\\')
        rows = list(reader)

    # Write out the rows using the default CSV writer,
    # which doubles quotes as required for proper CSV formatting.
    with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    print(f"Converted '{input_filename}' to '{output_filename}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_csv.py input.csv output.csv")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
