#!/usr/bin/env python
import sys, os, re, pandas, argparse

def col_count(hmmout):
    """TO count number of columns in the input file to determine if tblout or domtblout"""
    input = open(hmmout, "r")
    lin2 = input.readlines()[1]
    lin2 = ''.join(lin2)
    header = lin2.replace('# ', '', 1) # Only replace first instance of #
    header = header.replace(' name', '_name')
    header = header.replace(' of target', '_of_target')
    split = re.split(r"\s+", header)
    split = [i for i in split if i]
    return len(split)


def parse_hmmout(hmmout, len):
    """Parse HMM tblout and domtblout without prodigal header"""
    input = open(hmmout, "r")
    allrows = []
    for i in input.readlines():
        line = i.rstrip()
        if line.startswith("#"):
            pass
        else:
            if len == 19: 
                split = re.split(r"\s+", line, maxsplit=18) # for tblout
                row = "\t".join(split)
            elif len == 23:
                split = re.split(r"\s+", line, maxsplit=22) # for domtblout
                row = "\t".join(split)
            
            allrows.append(row)
    return allrows 

def prodigal_header(hmmout, len):
    """Parse HMM tblout and domtblout with prodigal header"""
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
                split = re.split(r"\s+", line, maxsplit=18) # for tblout
                row = "\t".join(split)
                desc = split[18]
            elif len == 23:
                split = re.split(r"\s+", line, maxsplit=22) # for domtblout
                row = "\t".join(split)
                desc = split[22]
            split = split[:-1]
                
            locat = re.split("# ", desc)
            locat = [x.strip(' ') for x in locat] # Remove whitespace
            locat = [x for x in locat if x] # Remove empty string in list
            split.extend(locat)
            row = "\t".join(split)
            
            allrows.append(row)
    return allrows 



def run_program(if_prod, input, output):
    len = col_count(input)
    if len == 19:
        if if_prod == True:
            prod_cols = ['Query_name', 'Query_accession', 'Target_name', 'Target_accession', 'Evalue', 'score', 'bias', 'dom_Evalue', 'dom_score', 'dom_bias', 'exp', 'reg', 'clu', 'ov', 'env', 'dom', 'rep', 'inc', 'start', 'end', 'strand', 'misc']
            cols = ["\t".join(prod_cols)]
            df1 = pandas.DataFrame(cols)
            df2 = pandas.DataFrame(prodigal_header(input, len))
        else:
            tbl_cols = ['Query_name', 'Query_accession', 'Target_name', 'Target_accession', 'Evalue', 'score', 'bias', 'dom_Evalue', 'dom_score', 'dom_bias', 'exp', 'reg', 'clu', 'ov', 'env', 'dom', 'rep', 'inc', 'description_of_target']
            cols = ["\t".join(tbl_cols)]
            df1 = pandas.DataFrame(cols)
            df2 = pandas.DataFrame(parse_hmmout(input, len))
        
    elif len == 23 :
        if if_prod == True:
            prod_cols = ['Query_name', 'Query_accession', 'Query_len', 'Target_name', 'Target_accession', 'Target_len',  'Evalue', 'score', 'bias', 'dom_#', 'dom_of', 'c_Evalue', 'i_Evalue', 'dom_score', 'dom_bias', 'hmm_from', 'hmm_to', 'align_from', 'align_to', 'env_from', 'env_to', 'acc','start', 'end', 'strand', 'misc']
            cols = ["\t".join(prod_cols)]
            df1 = pandas.DataFrame(cols)
            df2 = pandas.DataFrame(prodigal_header(input, len))
        else:
            tbl_cols = ['Query_name', 'Query_accession', 'Query_len', 'Target_name', 'Target_accession', 'Target_len', 'Evalue', 'score', 'bias', 'dom_#', 'dom_of', 'c_Evalue', 'i_Evalue', 'dom_score', 'dom_bias', 'hmm_from', 'hmm_to', 'align_from', 'align_to', 'env_from', 'env_to', 'acc', 'description_of_target']
            cols = ["\t".join(tbl_cols)]
            df1 = pandas.DataFrame(cols)
            df2 = pandas.DataFrame(parse_hmmout(input, len))
        
    df = pandas.concat([df1, df2])
    df.to_csv(output, index=False, header=False)


def main(arg=None) :
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="HMM Output parser: To parse the space delimited HMM output to a tab-delimited file but keeping all information in file\nAbdeali Jivaji, Virginia Tech Department of Biological Sciences <abdeali@vt.edu>", epilog='*******************************************************************\n\n*******************************************************************')
    #parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')
    parser.add_argument('-i', '--input', type=str, required=True, help='HMMer output file in table format for parsing, can be domtblout or tblout')
    parser.add_argument('-o', '--output', required=True, help='Name of parsed output table in tsv format')
    parser.add_argument('-p', '--prodigal', type=bool, required=False, default=False, const=True, nargs='?', help= 'To parse prodigal header in the final column for start and end and strandedness of gene')
    parser = parser.parse_args()

    inputfile = parser.input
    output = parser.output
    if_prod = parser.prodigal

    # Create output directory
    foldername = os.path.split(output)[0]
    if os.path.isdir(foldername):
        pass
    else:
        os.mkdir(foldername)
    
    # Run script
    run_program(if_prod, inputfile, output)
    
    return 0

    

if __name__ == '__main__':
	status = main()
	sys.exit(status)

# end





