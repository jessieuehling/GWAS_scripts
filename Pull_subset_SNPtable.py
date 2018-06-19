#!/usr/bin/env python

# Jessie Uehling 
#6 June 2018 (from Oz <3) 

import sys
#snippet to take a list of strains as input and pull that subset of strains from the SNSNP table, an output a SNP table containing only those individuals

#specify input 
strains_desired = set(i.strip() for i in 
	open('subset_strains_list.csv').readline().split())

	
#open the larger SNP table 
master_SNPs = ('merged_SNPs.txt')

fp = open(master_SNPs)

header = fp.next()

#split the header on tabs and remove the last character
fields = header.rstrip("\n").split("\t")

#set up column numbers and append matches 
#always include cols 0,1 which are the pos and ref 
columns= [0,1]
for(n,i) in enumerate(fields):
	if (i in strains_desired):
		columns.append(n)
#loop over the columns and keep track of the values youre interested in 

#write the header for the new table
sys.stdout.write("\t".join(fields[i] for i in columns) + "\n")

#loop over parsed file 
for line in fp:
	w = line.rstrip("\n").split("\t")

	sys.stdout.write("\t".join(w[i] for i in columns) + "\n")
