#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# modules to import
#
import argparse
from googletrans import Translator


# main function
def main(file, dest):

    # config Translator
    translator = Translator()

    # open a file
    with open(file, "r") as f:
        # get translations
        translations = [
            translator.translate(line, src="fr", dest=dest)
            for line in f.readlines()
        ]

    # print translated text
    [
        print(translated.text)
        for translated in translations
    ]


if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, required=True,
                        help="The file you want to translate")
    parser.add_argument("-t", "--to", type=str, required=True,
                        help="The destination language you want to translate.")
    args = parser.parse_args()

    #
    # program
    #
    main(args.file, args.to)
