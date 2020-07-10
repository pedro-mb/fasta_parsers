#!/usr/bin/python
import argparse


def getIDs(file):
    query = open(file, 'r')
    id_list = []
    for line in query:
        line = line.strip()
        id_list.append(line)
    query.close()
    return id_list

def fasta_screen(queryList, fastaFile, outFile):
    ## creating output file
    outfile = open(outFile, 'w')
    ## open fasta file
    fasta = open(fastaFile, 'r')
    seq = ''

    for line in fasta:
        if line[0] == '>' and seq == '':
            header = line.strip().split(' ')
            AC = header[0][1:]
        elif line[0] != '>':
            seq += line
        elif line[0] == '>' and seq != '':
            if AC in queryList:
                outfile.write(header[0] + '\n' + seq)
                queryList.pop(queryList.index(AC))
            seq = ''
            header = line.strip().split(' ')
            AC = header[0][1:]

    if AC in queryList:
        outfile.write(header[0] + '\n' + seq)
        queryList.pop(queryList.index(AC))

    fasta.close()
    outfile.close()
    return queryList

def main():
    parser = argparse.ArgumentParser(description='Filter fasta file with a list of IDs (one perline)')
    parser.add_argument('--query', required=True, metavar='ID file(s)', nargs='+',
                        help='[REQUIRED] text file(s) containing a list of sequence IDs, one per line')
    parser.add_argument('--fasta', required=True, metavar='fasta',
                        help='[REQUIRED] fasta file to filter')
    parser.add_argument('-o', metavar='output', type=str,
                        help='[optional] extension of output file(s). if not specified, the output file(s) name(s) will'
                             'be the same as query file(s) with "_seq.fa" extension ')
    args = parser.parse_args()

    for query in args.query:
        if args.o:
            outFileName = query + args.o
        else:
            outFileName = query + '_seq.fa'

        IDs_list = getIDs(query)

        noHit_list = fasta_screen(IDs_list, args.fasta, outFileName)

        if len(noHit_list) > 0:
            nf = '\n >> Genes from ' + query + ' not found in fasta file: \n'
            for ID in noHit_list:
                nf += ID + ', '
            print nf[:-2] + '\n'

if __name__ == "__main__":
    main()
