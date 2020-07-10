# python_parsers
General python scripts usefull in any workflow involving analysis of fasta files (nucleotides/aminoacids) or Blast outputs, 


### filter_fasta.py 
Used to filter a large fasta file based on a list of query IDs 

USAGE:

```
usage: filter_fasta.py [-h] --query ID files) [ID file(s ...] --fasta fasta
                       [-o output]
                       
Filter fasta file with a list of IDs (one perline)

optional arguments:
  -h, --help            show this help message and exit
  --query ID file(s) [ID file(s) ...]
                        [REQUIRED] text file(s) containing a list of sequence
                        IDs, one per line
  --fasta fasta         [REQUIRED] fasta file to filter
  -o output             [optional] extension of output file(s). if not
                        specified, the output file(s) name(s) willbe the same
                        as query file(s) with "_seq.fa" extension
```

### parseIntrons.py
Get the star and end sequences with length n, for all sequences present in a fasta file. Used for example to get the start and end of a list if introns, to analyse Splicing Junctions

```
usage: parseIntrons.py [-h] --fasta fasta [-o output] [-n length]

Retrieve start and end sequence, of length defined by user (-n)

optional arguments:
  -h, --help     show this help message and exit
  --fasta fasta  [REQUIRED] fasta file to filter
  -o output      [optional] extension of output file(s). if not specified, the
                 output file(s) name(s) will be the same as query file(s) with
                 "_ends.fa" extension
  -n length      Define the length in bp of start and end sequences (default
                 10)

```

## getBestBlastHit.py

Get the best hit for every query from a Blast output file in tabular format

```
usage: getBestBlastHit.py [-h] --query tab [tab ...] [-o output]

Get Best Blast Hit using ncbi-blast output in tabular format (6)

optional arguments:
  -h, --help            show this help message and exit
  --query tab [tab ...]
                        [REQUIRED] Blast output file in tab format (6)
  -o output             [optional] extension of output file(s). if not
                        specified, the output file(s) name(s) will be the same
                        as query file(s) with "_BestHit.txt" extension
                       
```
