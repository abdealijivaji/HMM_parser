# HMM_parser

Trying to create a tool for parsing HMMer output with all columns included

This has been as part of a pet project of mine to develop my python skills. For any issues/suggestions, please create an issue on GitHub or feel free to email me at [abdeali\@vt.edu](mailto:abdeali@vt.edu){.email}

The script takes major influence from Thomas Hackl's seq-scripts repos [hmmer-tbl2tsv](https://github.com/thackl/seq-scripts/blob/master/bin/hmmer-tbl2tsv). Check out the repo for handy scripts for bioinformatics.

## Requirements

Python (\>=3.9)

Pandas (\>=2.2)

## Usage

```{bash}
git clone https://github.com/abdealijivaji/HMM_parser.git
cd HMM_parser
```

The tool has been set up to use python directly from your environment.

```{bash}
./hmm_parser -i test/test.out -o output/test.tsv 
# For parsing prodigal header 
./hmm_parser -i test/ERX288947.23.dc.fltr.hmmout -o output/test_prod.tsv -p
```

The script counts the number of columns and recognized tblout or domtblout files.

Without specifying `-p` , the last column will be set to default.

## Acknowledgements

This project has been with great support of my advisor Dr. Frank Aylward at Virginia Tech, Department of Biological Sciences
