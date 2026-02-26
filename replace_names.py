#!/usr/bin/python3

"""
Replace names in any readable text file based on a two-column, tab-delimited mapping file.

Column 1: original string (query)
Column 2: replacement string

Example mapping.tsv:
A1\tA2
B1\tB2
C1\tC2

Usage:
    python3 replace_names.py -m mapping.tsv -i input.txt -o output.txt

Notes:
- Replacements are exact string matches (not regex).
- All replacements are applied globally, line by line.
- Mapping is applied in the order given in the mapping file.
"""

import argparse


def load_mapping(mapping_file):
    mapping = []
    with open(mapping_file) as fh:
        for line in fh:
            line = line.rstrip('\n')
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) != 2:
                raise ValueError(f"Invalid mapping line (expected 2 columns): {line}")
            mapping.append((parts[0], parts[1]))
    return mapping


def replace_in_file(mapping, infile, outfile):
    with open(infile) as fin, open(outfile, 'w') as fout:
        for line in fin:
            for old, new in mapping:
                line = line.replace(old, new)
            fout.write(line)


def main():
    parser = argparse.ArgumentParser(
        description="Replace strings in a text file using a two-column, tab-delimited mapping file."
    )

    parser.add_argument(
        '-m', '--mapping',
        required=True,
        help='Tab-delimited file with original and replacement strings (2 columns).'
    )

    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Input text file to process.'
    )

    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output file with replacements applied.'
    )

    args = parser.parse_args()

    mapping = load_mapping(args.mapping)
    replace_in_file(mapping, args.input, args.output)


if __name__ == '__main__':
    main()
