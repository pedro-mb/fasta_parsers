#!/usr/bin/python

import argparse

def get_promotor(gff, size, outname, feature):
    gff_file = open(gff, "r")
    out_file = open(outname, "w")
    for line in gff_file:
        if line[0] != "#":
            #print line.strip().split()
            chr, db, ref_feature, stt, end, fscore, strand, frame, ref_id  = line.strip().split()[:9]
            stt = int(stt)
            end = int(end)
            if ref_feature == feature:
                if strand == "+" and stt <= size:
                    prom_stt = 1
                    out_file.write(chr + "\t" + "promoter" + "\t" + str(prom_stt) + "\t" + str(stt) + "\t" + strand +
                                   "\t" + ref_id + "\n")
                elif strand == "+" and stt > size:
                    prom_stt = stt - size
                    out_file.write(chr + "\t" + "promoter" + "\t" + str(prom_stt) + "\t" + str(stt) + "\t" + strand +
                                   "\t" + ref_id + "\n")
                elif strand == "-": ## need to consider length of the scaffold... although right now I don't have this data
                    prom_stt = end + size
                    out_file.write(chr + "\t" + "promoter" + "\t" + str(end) + "\t" + str(prom_stt) + "\t" + strand +
                                   "\t" + ref_id + "\n")
                else:
                    continue
        else:
            continue
    out_file.close()
    gff_file.close()


def main():
    parser = argparse.ArgumentParser(description='Get promoter coordinates for genes based on gff')
    parser.add_argument('--gff', required=True, metavar='tab',
                        help='gff file to analyse')
    parser.add_argument('--size', metavar="INT", type=int, default=1000,
                        help='size in bp to fetch the promoters. Default: 1000 ')
    parser.add_argument('--out', metavar='STR', type=str, default="promoter_coordinates.tab",
                        help='Output file name')
    parser.add_argument('--feature', metavar='STR', type=str, default="gene",
                        help='feature name from gff (3rd column) to be considered as promoter parent (default: gene)')

    args = parser.parse_args()

    get_promotor(args.gff, args.size, args.out, args.feature)


if __name__ == "__main__":
    main()
