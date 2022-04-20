#!/usr/bin/python3

import sys
import fileinput

header=''

fas1=sys.argv[1] #read in fasta file number 1 -> original with all entries
output=sys.argv[2] #create new output

fasnames=open(output+'-names.txt', 'w')

for line in fileinput.input(fas1):
	if line[0:1]=='>':
		fasnames.write(line)
fileinput.close()

fasnames.close() #closing file