#!/usr/bin/python

import glob
import csv
import sys
import os

# Check args
if len(sys.argv) < 2:
    sys.exit('Usage: keeper2lastpass.py /path/to/dir')

# Create glob pattern, fetch filenames
pattern = sys.argv[1].rstrip('/') + '/*keeper.txt'
filenames = glob.glob(pattern)
fieldnames = ['grouping', 'name', 'username', 'password', 'url', 'extra']

# Loop through, and convert
for i, source_file in enumerate(filenames):
    dest_file = source_file.rstrip('.txt') + '.lastpass.csv'
    csv.field_size_limit(sys.maxsize)
    writer = csv.writer(file(dest_file, 'w+'))
    writer.writerow(fieldnames)
    writer.writerows(csv.reader(open(source_file), delimiter="\t"))

    print 'Created: ' + os.path.basename(dest_file)

