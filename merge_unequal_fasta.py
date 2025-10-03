#!/usr/bin/python3

import sys
import fileinput

def extract_fasta_names(fasta_files):
    unique_headers = set()
    
    for line in fileinput.input(fasta_files):
        if line.startswith('>'):
            header = line.strip()
            unique_headers.add(header)
    
    return sorted(unique_headers)

def concatenate_fasta_sequences(fasta_files, output_file, names):
    fas_dict = {key: '' for key in names}
    
    print(f"{fasta_files}")
    print(f"{len(fasta_files)} fasta files")
    
    for fasta in fasta_files:
        temp_dict = {}
        header = ''
        seq = ''
        
        with open(fasta) as file:
            all_lines = file.readlines()
            seqlength = max(len(line.strip()) for line in all_lines[1:] if line.strip()) if len(all_lines) > 1 else 0
            emptyseq = '?' * seqlength  # Replace missing sequences with '?'
            print(f"{fasta} {seqlength} bp in length")
        
        for line in fileinput.input(fasta):
            if line.startswith('>'):
                header = line.strip()
            else:
                seq = line.strip()
                temp_dict[header] = seq
        fileinput.close()
        
        for name in names:
            fas_dict[name] += temp_dict.get(name, emptyseq)
    
    with open(output_file + '.fasta', 'w') as fullfas:
        for name, sequence in fas_dict.items():
            fullfas.write(name + '\n' + sequence + '\n')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 script.py <output_prefix> <fasta1> <fasta2> ...")
        sys.exit(1)
    
    output_prefix = sys.argv[1]
    fasta_files = sys.argv[2:]
    
    fasta_names = extract_fasta_names(fasta_files)
    concatenate_fasta_sequences(fasta_files, output_prefix, fasta_names)
