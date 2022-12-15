#!/usr/bin/env python
#-*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('../data/library.xml')
root = tree.getroot()

for book in tree.iter('book'):

    print('=' * 50)

    ref_author = book.attrib['ref_author']

    for author in tree.iter('author'):
        if author.attrib['id_author'] == ref_author:
            firstname = author.find('firstName').text
            lastname = author.find('lastName').text

    title = book.find('title').text
    pub_date = book.find('publication').text
    
    print(f"Author: {firstname} {lastname}\nTitle: {title}\nPublication date: {pub_date}")
