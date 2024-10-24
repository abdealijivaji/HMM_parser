#!/usr/bin/env python
import sys, os, re, shlex, subprocess, pandas, argparse
from collections import defaultdict

#print(sys.path)
file = "test/ERX288947.23.dc.fltr.hmmout"

def parse_hmmout(hmmout):
    input = open(hmmout, "r")
    split = []
    for i in input.readlines():
        line = i.rstrip()
        if line.startswith("#"):
            pass
        else:
            #newline = re.sub(r"\s+", "\t", line)
            #split = []
            #split = line.split(" ", maxsplit= 19)
            
            split += re.split(r"\s+", line, maxsplit=18) # change number for different files
            #print(split)
        
    return split
#print(newline)

#return newline


print(parse_hmmout(file))