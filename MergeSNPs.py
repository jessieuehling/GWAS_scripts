#!/usr/bin/env python
# Time-stamp: <MergeSNPs.py 2018-05-24 12:25:46 Mark Voorhies>

import sys

def merge_SNPs(vcf_files):
    """Return dict of dicts mapping variable positions to strain-specific
    choices for simple SNP positions.
    """

    weird_positions = 0
    
    # Dict of dicts: {pos => {strain => base}}
    pos2snps = {}

    bases = frozenset("ATGC")

    # List of strain names, matching column order of output file
    strains = ["ref"]

    for vcf_file in vcf_files:
        # derive strain name from file name
        strain = vcf_file.replace("_SNPoutput","")
        strains.append(strain)

        for line in open(vcf_file):
            # skip comments
            if(line.startswith("#")):
                continue
            # parse the columns we care about
            w = line.split("\t")
            chrom,position,ref,alt = (w[0],w[1],w[3],w[4])
            pos = "%s.%08d" % (chrom,int(position))
            # TODO: understand case convention in vcf files
            ref = ref.upper()
            alt = alt.upper()
            if((ref == alt) or (ref not in bases) or (alt not in bases)):
                weird_positions += 1
                continue
            if(pos2snps.has_key(pos)):
                d = pos2snps[pos]
                assert(d["ref"] == ref)
                d[strain] = alt
            else:
                pos2snps[pos] = {"ref":ref,strain:alt}

    sys.stderr.write("Skipped %d weird positions\n" % weird_positions)

    return strains, pos2snps

def write_SNP_table(strains, pos2snps, out):
    # Write header line
    out.write("\t".join(["pos"]+strains)+"\n")
    
    for pos in sorted(pos2snps):
        d = pos2snps[pos]
        ref = d["ref"]
        row = [pos,ref]

        for strain in strains[1:]:
            if(d.has_key(strain)):
                row.append(d[strain])
            else:
                row.append(ref)

        out.write("\t".join(row)+"\n")

if(__name__ == "__main__"):
    if(len(sys.argv) < 2):
        sys.stderr.write("Usage: %s strain1.vcf [strain2.vcf ...] > SNPs.tdt\n" % sys.argv[0])
        sys.exit(1)

    vcf_files = sys.argv[1:]

    strains, pos2snps = merge_SNPs(vcf_files)

    write_SNP_table(strains, pos2snps, sys.stdout)

    
