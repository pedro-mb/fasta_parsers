#!/usr/bin/python

import argparse

def main():
    parser = argparse.ArgumentParser(description='Get splicing junction flanking '
                                       'coordinates based on intron coordinates ')
    parser.add_argument('--featCoord', required=True, metavar='STR',
                        help='[REQUIRED] file name, '
                             'containing the coordinates to the feature to be considered. \n'
                             '- File(s) with coordinates should have the following format \n '
                             '<chr>\t<feature>\t<stt>\t<end>\t<strand>\t<id>\t<product>\n '
                             '(e.g. output of gff2tab.pl [-I] script')
    parser.add_argument('--SJtype', required=True, metavar='STR', type=str,
                        help='Type of splicing junction to analyse. '
                        'Use: A (for acceptor) or D (donor) ')
    parser.add_argument('--window', metavar="INT", type=int, default=60,
                        help='window to get upstream and downstream coordinates.'
                        ' Default 60.')
    parser.add_argument('--out', metavar='STR', type=str, default="_SJcoordinates.tab",
                        help='Output file name')


    args = parser.parse_args()
    outfile = open(args.SJtype + args.out, "w")
    sample = open(args.featCoord, "r")
    for item in sample:
        item_list = item.strip().split()
        #chr,feature, sample_id = item_list
        if args.SJtype == "D":
            if item_list[4] == "+":
                SJ = int(item_list[2])
                upCoord = SJ - int(args.window)
                if upCoord < 0:
                    upCoord = 0
                downCoord = SJ + (int(args.window)-1)
                item_list[2] = str(upCoord)
                item_list[3] = str(downCoord)
                outfile.write('\t'.join(item_list) + '\n')
            elif item_list[4] == "-":
                SJ = int(item_list[3])
                upCoord = SJ - int(args.window)
                if upCoord < 0:
                    upCoord = 0
                downCoord = SJ + (int(args.window)-1)
                item_list[2] = str(upCoord)
                item_list[3] = str(downCoord)
                outfile.write('\t'.join(item_list) + '\n')
            else:
                print 'no strand information, line not saved:\n'
                print '\t'.join(item_list) + '\n'
        if args.SJtype == "A":
            if item_list[4] == "+":
                SJ = int(item_list[3])
                upCoord = SJ - int(args.window)
                #if upCoord < 0:
                #    upCoord = 0
                downCoord = SJ + (int(args.window)-1)
                item_list[2] = str(upCoord)
                item_list[3] = str(downCoord)
                outfile.write('\t'.join(item_list) + '\n')
            elif item_list[4] == "-":
                SJ = int(item_list[2])
                upCoord = SJ - int(args.window)
                if upCoord < 0:
                    upCoord = 0
                downCoord = SJ + (int(args.window)-1)
                item_list[2] = str(upCoord)
                item_list[3] = str(downCoord)
                outfile.write('\t'.join(item_list) + '\n')
            else:
                print 'no strand information, line not saved:\n'
                print '\t'.join(item_list) + '\n'
    sample.close()
    outfile.close()

main()
