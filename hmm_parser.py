#!/usr/bin/env python
import sys, os, re, shlex, subprocess, pandas, argparse
from collections import defaultdict

#print(sys.path)


def parse_hmmout(hmmout):
	input = open(hmmout, "r")
	final_dict = defaultdict(int)
	hit_dict = defaultdict(lambda:"no_annot")
	bit_dict = defaultdict(float)

	for i in input.readlines():
		line = i.rstrip()
		if line.startswith("#"):
			pass
		else:
			newline = re.sub("\s+", "\t", line)
			tabs = newline.split("\t")
			protein = tabs[0]
			hit = tabs[2]
			eval = float(tabs[4])
			score = float(tabs[5])
			if score > 30:
				if score > bit_dict[protein]:
					bit_dict[protein] = score
					hit_dict[protein] = hit
				else:
					pass
			else:
				pass
	for i in hit_dict:
		vog = hit_dict[i]
		final_dict[vog] +=1
	return final_dict