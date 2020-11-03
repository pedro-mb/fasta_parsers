# python_parsers
General python scripts usefull in any workflow involving analysis of fasta files (nucleotides/aminoacids) or Blast outputs, 

### gff2promoter.py

Get promoter coordinates for all genes in a given gff file

USAGE:
```
usage: gff2promoter.py [-h] --gff tab [--size INT] [--out STR] [--feature STR]

Get promoter coordinates for genes based on gff

optional arguments:
  -h, --help     show this help message and exit
  --gff tab      gff file to analyse
  --size INT     size in bp to fetch the promoters. Default: 1000
  --out STR      Output file name
  --feature STR  feature name from gff (3rd column) to be considered as
                 promoter parent (default: gene)
```


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
## getSJ_coordinates.py

Get the coordinates flanking "donor" (D) or "acceptor" (A) site splicing junctions (SJ), based on a list of intron coordinates


```
usage: getSJ_coordinates.py [-h] --featCoord STR --SJtype STR [--window INT]
                            [--out STR]

Get splicing junction flanking coordinates based on intron coordinates

optional arguments:
  -h, --help       show this help message and exit
  --featCoord STR  [REQUIRED] file name, containing the coordinates to the
                   feature to be considered. - File(s) with coordinates should
                   have the following format <chr> <feature> <stt> <end>
                   <strand> <id> <product> (e.g. output of gff2tab.pl [-I]
                   script
  --SJtype STR     Type of splicing junction to analyse. Use: A (for acceptor)
                   or D (donor)
  --window INT     window to get upstream and downstream coordinates. Default
                   60.
  --out STR        Output file name
  
  ```
