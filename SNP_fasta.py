#!/usr/bin/env python
# Time-stamp: <MergeSNPs.py 2018-05-29 2:43 PM Jessie Uehling>

#git trial comment
#open the SNP table

fp  = open("merged_SNPs.txt")

#assign isolate names 

names = fp.readline().rstrip("\n").split("\t")[2:]

#initialize seqs 
seqs = []

#write the names to a list

for i in names:  
    seqs.append("")

#chug through rows, write the base for each isolate
import sys
for row in fp: 
	cols = row.rstrip("\n").split("\t")[2:]
	for n in xrange(len(cols)):
		seqs[n]+=cols[n]
	count = len(seqs[0])
	if count%1000==0:
		sys.stderr.write("%d\n"%count)
out = open("SNPs.fasta", "w")	
for name, s in zip(names, seqs):
	out.write(">%s\n" % name)
	out.write("%s\n" % s)
out.close()


