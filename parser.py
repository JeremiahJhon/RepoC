import sys
import csv
import re

def parse_log(input_file, output_file):
    pattern = re.compile(r'(.+):(\d+):\s+warning:\s+(.*)')

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Line', 'File', 'Message'])

        for line in infile:
            match = pattern.match(line)
            if match:
                file, line_no, message = match.groups()
                writer.writerow([line_no, file, message])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser.py <warnings.log>")
        sys.exit(1)

    parse_log(sys.argv[1], 'output.csv')