#!/usr/bin/python

import argparse

def fasta_screen(fasta_file, out_file, max_length):
    ## creating output file
    outfile = open(out_file, 'w')
    ## open fasta file
    fasta = open(fasta_file, 'r')
    seq = ''

    for line in fasta:
        if line[0] == '>' and seq == '':
            header = line.strip().split()
            #print header
            #AC = header[0][1:]
        elif line[0] != '>':
            seq += line
        elif line[0] == '>' and seq != '':
            #if AC in queryList:
            start = seq[:max_length]
            end = seq[len(seq)-max_length:len(seq)-1]
            #print end
            if len(seq) > (max_length * 2):
                outfile.write(header[0] + '\n' + start + "..."+ end + '\n')
            seq = ''
            header = line.strip().split(' ')
            #AC = header[0][1:]
    start = seq[:max_length]
    end = seq[len(seq)-max_length:len(seq)-1]
    if len(seq) > (max_length * 2):
        outfile.write(header[0] + '\n' + start + "..."+ end)

    fasta.close()
    outfile.close()


def main():
    parser = argparse.ArgumentParser(description='Retrieve start and end sequence,\
    of length defined by user (-n)')
    parser.add_argument('--fasta', required=True, metavar='fasta',
                        help='[REQUIRED] fasta file to filter')
    parser.add_argument('-o', metavar='output', type=str,
                        help='[optional] extension of output file(s). if not specified,\
                         the output file(s) name(s) will be the same as query file(s) \
                         with "_ends.fa" extension')
    parser.add_argument('-n', metavar='length', type=int, default = 10,
                        help='Define the length in bp of start and end sequences\
                        (default 10)')
    args = parser.parse_args()



    if args.o:
        outFileName = args.fasta + args.o
    else:
        outFileName = args.fasta + '_seq.fa'

        fasta_screen(args.fasta, outFileName, args.n)

        #if len(noHit_list) > 0:
        #    nf = '\n >> Genes from ' + query + ' not found in fasta file: \n'
        #    for ID in noHit_list:
        #        nf += ID + ', '
        #    print nf[:-2] + '\n'

if __name__ == "__main__":
    main()
