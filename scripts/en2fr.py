#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# modules to import
#
import argparse
from googletrans import Translator


# main function
def main(text):

	# config Translator
	translator = Translator()

	# get a 'translated' object
	translated = translator.translate(text, src="en", dest="fr")

	print(translated.text)


if __name__ == "__main__":

  # parse arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--text", type=str, help="text to translate", required=True)
  args = parser.parse_args()

  #
  # program
  #
  main(args.text)
