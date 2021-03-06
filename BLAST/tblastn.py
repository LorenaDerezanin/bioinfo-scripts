#!/usr/bin/env python

# run multiple tblastn runs with each protein seq file in dir as a query


import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", dest="input", action="store", required=True)
parser.add_argument("-o", "--output", dest="output", action="store", required=True)
parser.add_argument("-db", "--database", dest="database", action="store", required=True)
parser.add_argument("-e", "--evalue", dest="evalue", action="store", type=float)
parser.add_argument("-word_size", dest="word_size", action="store", type=int)


args = parser.parse_args()


def prot_name(protein):
    split_name = protein.split(".fasta")
    return split_name[0]


path = args.input
protein_files = os.listdir(path)

for protein_file in protein_files:
    f_out_path = os.path.join(args.output, prot_name(protein_file) + "_blastp")
    f_in_path = os.path.join(path, protein_file)
    blast = "tblastn -query %s -out %s -db %s -evalue %s -word_size %s" % (f_in_path, f_out_path, args.database, args.evalue, args.word_size)
    os.system(blast)
