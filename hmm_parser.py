#!/usr/bin/env python
import sys, os, re, shlex, subprocess, pandas, argparse
from collections import defaultdict

input = "test/ERX288947.23.dc.fltr.hmmout" #sys.argv[1]
output = "test.out" #sys.argv[2]

def col_count(hmmout):
    input = open(hmmout, "r")
    lin2 = input.readlines()[1]
    lin2 = ''.join(lin2)
    header = lin2.replace('# ', '', 1)
    header = header.replace(' name', '_name')
    header = header.replace(' of target', '_of_target')
    split = re.split(r"\s+", header)
    split = [i for i in split if i]
    return len(split)

print(col_count(input))

def parse_hmmout(hmmout, len):
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
            if len == 19:
                split = re.split(r"\s+", line, maxsplit=18) # change number for different files
                row = "\t".join(split)
            elif len == 23:
                split = re.split(r"\s+", line, maxsplit=22) # change number for different files
                row = "\t".join(split)
            #print(row)
            
            allrows.append(row)
    return allrows 
#print(newline)

def prodigal_header(hmmout, len):
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
            if len == 19:
                split = re.split(r"\s+", line, maxsplit=18) # change number for different files
                row = "\t".join(split)
                desc = split[18]
            elif len == 23:
                split = re.split(r"\s+", line, maxsplit=22) # change number for different files
                row = "\t".join(split)
                desc = split[22]
            split = split[:-1]
                
            locat = re.split("# ", desc)
            locat = [x.strip(' ') for x in locat]
            locat = [x for x in locat if x]
            split.extend(locat)
                #print(split)
            row = "\t".join(split)
            
            allrows.append(row)
    return allrows 



def run_program(if_prod, hmmout):
    len = col_count(hmmout)
    if len == 19:
        if if_prod == True:
            prod_cols = ['target_name', 'target_accession', 'query_name', 'query_accession', 'evalue', 'score', 'bias', 'dom_evalue', 'dom_score', 'dom_bias', 'exp', 'reg', 'clu', 'ov', 'env', 'dom', 'rep', 'inc', 'start', 'end', 'strand', 'misc']
            cols = ["\t".join(prod_cols)]
            df1 = pandas.DataFrame(cols)
            df2 = pandas.DataFrame(prodigal_header(input, len))
        else:
            tbl_cols = ['target_name', 'target_accession', 'query_name', 'query_accession', 'evalue', 'score', 'bias', 'dom_evalue', 'dom_score', 'dom_bias', 'exp', 'reg', 'clu', 'ov', 'env', 'dom', 'rep', 'inc', 'description_of_target']
            cols = ["\t".join(tbl_cols)]
            df1 = pandas.DataFrame(cols)
            df2 = pandas.DataFrame(parse_hmmout(input, len))
        
        df = pandas.concat([df1, df2])
        df.to_csv(output, index=False, header=False)
    elif len == 23 :
        if if_prod == True:
            prod_cols = ['target_name', 'target_accession', 'target_len', 'query_name', 'query_accession', 'query_len', 'E-value', 'score', 'bias', 'dom_#', 'dom_of', 'c_E-value', 'I_E-value', 'dom_score', 'dom_bias', 'hmm_from', 'hmm_to', 'align_from', 'align_to', 'env_from', 'env_to', 'acc','start', 'end', 'strand', 'misc']
            cols = ["\t".join(prod_cols)]
            df1 = pandas.DataFrame(cols)
            df2 = pandas.DataFrame(prodigal_header(input, len))
        else:
            tbl_cols = ['target_name', 'target_accession', 'target_len', 'query_name', 'query_accession', 'query_len', 'E-value', 'score', 'bias', 'dom_#', 'dom_of', 'c_E-value', 'I_E-value', 'dom_score', 'dom_bias', 'hmm_from', 'hmm_to', 'align_from', 'align_to', 'env_from', 'env_to', 'acc', 'description_of_target']
            cols = ["\t".join(tbl_cols)]
            df1 = pandas.DataFrame(cols)
            df2 = pandas.DataFrame(parse_hmmout(input, len))
        
        df = pandas.concat([df1, df2])
        df.to_csv(output, index=False, header=False)
    
#print(colnames)

#parse_hmmout(file)
#print(parse_hmmout(file))

#print(df)



def main(arg=None) :
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="HMM Output parser: To parse the space delimited HMM output to a tab-delimited file but keeping all information in file\nAbdeali Jivaji, Virginia Tech Department of Biological Sciences <abdeali@vt.edu>", epilog='*******************************************************************\n\n*******************************************************************')
    parser.add_argument('-p', '--prodigal', type=bool, required=False, default=False, const=True, nargs='?', help= 'To parse prodigal header in the final column')
    #parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')
    parser = parser.parse_args()

    if_prod = parser.prodigal

    run_program(if_prod, input)
    
    return 0

    # Directories

if __name__ == '__main__':
	status = main()
	sys.exit(status)

# end





