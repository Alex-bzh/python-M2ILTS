#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# modules to import
#
import argparse
import csv
from os import listdir
from os.path import isfile, splitext

def write_tsv(root, data):
    """Write a TSV file

    Keyword arguments:
    root -- root of a path to a file
    data -- a dictionary
    """

    # what are the languages?
    langs = data.keys()

    # write into a TSV file
    with open(f"{root}.tsv", "w") as csvfile:

        # a writer object
        writer = csv.writer(csvfile, delimiter="\t")

        # write header
        writer.writerow(langs)

        # print each row of every speeches
        for value in zip(*data.values()):
            writer.writerow(value)

# main function
def main(folder):

    # empty object to collect data
    speeches = dict()

    # scan files in directory
    for file in listdir(folder):
        path = f"{folder}/{file}"
        root, ext = splitext(path)

        # if there is at least one file
        # that is not of TSV type
        if isfile(path) and 'tsv' not in path:
            # fill dict with lines
            with open(path) as f:
                speeches[ext.replace('.', '')] = [
                    line.strip()
                    for line in f.readlines()
                ]

    # call to specific writing function
    write_tsv(root, speeches)

if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", type=str, required=True,
                        help="The folder where lie the files")
    args = parser.parse_args()

    #
    # program
    #
    main(args.folder)
