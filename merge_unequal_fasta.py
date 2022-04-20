#!/usr/bin/python3

import sys
import fileinput

all_names=sys.argv[1] #read in text fie with all sequence headers
output=sys.argv[2] #create new output
fastas=sys.argv[3:] #read in text fie with all sequence headers

fullfas=open(output+'.fasta', 'w')

print(all_names)
print(output)
print(fastas)
print(len(fastas),"fasta files")

t = len(fastas)
seqlist=[]
names=open(all_names).readlines()
names=[s.rstrip() for s in names]

fas_dict={}
for key in names:
	fas_dict[key]=''

for i in range(0,t): #range through each of the files
	header=''
	seq=''
	temp_dict={}

	file=open(fastas[i])
	all_lines=file.readlines()
	seqlength=len(all_lines[1])-1
	print(fastas[i],seqlength,"bp in length")
	emptyseq='-'*seqlength

	for line in fileinput.input(fastas[i]): #extract fasta headers and sequences
		if line[0:1]=='>':
			header=line.rstrip()
			next
		else:
			seq=line.rstrip()
		temp_dict[header]=seq
	fileinput.close()

	for name in names: #write sequences to dictionary, i.e. concatenate sequences
		if name in temp_dict:
			fas_dict[name]=fas_dict[name]+temp_dict[name]
		else: #if fasta file doesn't have a sequence of a particular sample, write '-' as long as the sequences
			fas_dict[name]=fas_dict[name]+emptyseq

for name in fas_dict: #write out concatenated sequences to file
	fullfas.write(name)
	fullfas.write('\n')
	fullfas.write(fas_dict[name])
	fullfas.write('\n')
fullfas.close() #closing file
