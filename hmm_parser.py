#!/usr/bin/env python
import sys, os, re, shlex, subprocess, pandas, argparse
from collections import defaultdict

#print(sys.path)
file = "test/ERX288947.23.dc.fltr.hmmout"

def parse_hmmout(hmmout):
	input = open(hmmout, "r")

	for i in input.readlines():
		line = i.rstrip()
		if line.startswith("#"):
			pass
		else:
			newline = re.sub(r"\s+", "\t", line)
			#print(newline)
			
    #return newline


parse_hmmout(file)