#!/usr/bin/env python
#-*- coding: utf-8 -*-

# module to parse XML files
import xml.etree.ElementTree as ET

# which file?
tree = ET.parse('../../data/XML/library.xml')
# get root element
root = tree.getroot()

# from root, find every book elements
# and parse each one
for book in tree.iter('book'):

    # a separator between items
    print('=' * 50)

    # ref_author attribute helps find infos about author
    ref_author = book.attrib['ref_author']

    # from root, find every author elements
    # and parse each one
    for author in tree.iter('author'):
        # check if current ref_author is one of id_author
        if author.attrib['id_author'] == ref_author:
            # if so, means this author is linked to book element
            firstname = author.find('firstName').text
            lastname = author.find('lastName').text

    # inner text of title and publication elements
    title = book.find('title').text
    pub_date = book.find('publication').text
    
    # print result
    print(f"Author: {firstname} {lastname}\nTitle: {title}\nPublication date: {pub_date}")
