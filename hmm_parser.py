#!/usr/bin/env python
import sys, os, re, shlex, subprocess, pandas, argparse
from collections import defaultdict

file = "test/ERX288947.23.dc.fltr.hmmout"

def parse_hmmout(hmmout):
    input = open(hmmout, "r")
    allrows = []
    for i in input.readlines():
        line = i.rstrip()
        if line.startswith("#"):
            pass
        else:
            #newline = re.sub(r"\s+", "\t", line)
            #split = []
            #split = line.split(" ", maxsplit= 19)
            
            split = re.split(r"\s+", line, maxsplit=18) # change number for different files
            row = "\t".join(split)
            #print(row)
            
            allrows.append(row)
    return allrows 
#print(newline)
colnames = ['target_name', 'target_accession', 'query_name', 'query_accession',
                       'evalue', 'score', 'bias',
                       'dom_evalue', 'dom_score', 'dom_bias',
                       'exp', 'reg', 'clu', 'ov', 'env', 'dom', 'rep', 'inc', 'description_of_target']
cols = ["\t".join(colnames)]
#print(colnames)

#parse_hmmout(file)
#print(parse_hmmout(file))
df1 = pandas.DataFrame(cols)
df2 = pandas.DataFrame(parse_hmmout(file))
#print(df)
df = pandas.concat([df1, df2])
df.to_csv("./test.txt", index=False, header=False)