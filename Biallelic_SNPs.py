#!/usr/bin/env/ python

#JWAS
#15 June 2018 (from SF <3)

#snippet to take a SNP table and filter for bialllelic SNPs
import sys

#open table 
all_SNPs = open('merged_SNPs.txt')

#delimit header from body 
header = all_SNPs.next()

#print the header
print(header)

#count the unique characters in a parsed line with a conditional loop 
for line in all_SNPs:
        w = line.rstrip("\n").split("\t")
        unique_bases = len(set(w[2:]))
        potl_seq_errors = len(set(w[2:]))       
#If its 2, count that row and hold on to it 
	if unique_bases == 2:
	
#a way to count potential sequencing errors is to quantify the loci which differ from the reference but not within the rest of the population, use the below to counth them 	
	#if potl_seq_errors == 1: 
		print (w)

 
