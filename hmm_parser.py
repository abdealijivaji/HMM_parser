#!/usr/bin/env python
import sys, os, re, shlex, subprocess, pandas, argparse
from collections import defaultdict

input = "/home/abdeali/packages/HMM_parser/test/ERX288947.23.dc.fltr.hmmout" #sys.argv[1]
output = "test.out" #sys.argv[2]

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

def prodigal_header(hmmout):
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
            desc = split[18]
            split = split[:-1]
            locat = re.split("# ", desc)
            locat = [x.strip(' ') for x in locat]
            locat = [x for x in locat if x]
            split.extend(locat)
            #print(split)
            row = "\t".join(split)
            
            allrows.append(row)
    return allrows 



def run_program(if_prod):

    if if_prod == True:
        prod_cols = ['target_name', 'target_accession', 'query_name', 'query_accession',
                            'evalue', 'score', 'bias',
                            'dom_evalue', 'dom_score', 'dom_bias',
                            'exp', 'reg', 'clu', 'ov', 'env', 'dom', 'rep', 'inc', 'start', 'end', 'strand', 'misc']
        cols = ["\t".join(prod_cols)]
        df1 = pandas.DataFrame(cols)
        df2 = pandas.DataFrame(prodigal_header(input))
    else:
        tbl_cols = ['target_name', 'target_accession', 'query_name', 'query_accession',
                            'evalue', 'score', 'bias',
                            'dom_evalue', 'dom_score', 'dom_bias',
                            'exp', 'reg', 'clu', 'ov', 'env', 'dom', 'rep', 'inc', 'description_of_target']
        cols = ["\t".join(tbl_cols)]
        df1 = pandas.DataFrame(cols)
        df2 = pandas.DataFrame(parse_hmmout(input))
    
    df = pandas.concat([df1, df2])
    df.to_csv(output, index=False, header=False)
    
#print(colnames)

#parse_hmmout(file)
#print(parse_hmmout(file))

#print(df)



def main(arg=None) :
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="HMM Output parser: To parse the space delimited HMM output to a tab-delimited file but keeping all information in file\nAbdeali Jivaji, Virginia Tech Department of Biological Sciences <abdeali@vt.edu>", epilog='*******************************************************************\n\n*******************************************************************')
    parser.add_argument('-p', '--prodigal', type=bool, required=False, default=False, const=True, nargs='?', help= 'To parse prodigal header in the final column')
    parser = parser.parse_args()

    if_prod = parser.prodigal

    run_program(if_prod)
    
    return 0

    # Directories

if __name__ == '__main__':
	status = main()
	sys.exit(status)

# end





