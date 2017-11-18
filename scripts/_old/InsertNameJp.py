#!/usr/bin/env python
# -*- coding: utf_8 -*- 

def InsertNameJp(r):
    read_file = None
    write_file = None
    temp_file = "temp_file"
    read_file = open("db.js", 'r')
    write_file = open(temp_file, 'w')

    Sheet = r["name"]
    for Item in Sheet:
#	if str(Item["db_jp"]) != "":
#	    print str(Item["db_en"])
#	    print str(Item["db_en"]) + "\n" + str(Item["db_jp"])
#	Item["db_jp"].encode('utf-8')
#	print isinstance(u'Item["db_jp"]', str)
#	print isinstance(Item["db_jp"], str)

	db_en = u'\t\t' + Item["db_en"] + u'\n'
    	db_jp = u'\t\t' + Item["db_en"] + u'\n\t\t' + Item["db_jp"] +u'\n'
#	print db_en.encode('utf-8')
#	print db_jp.encode('utf-8')
     	if Item["db_jp"].encode('utf8') is not None:
    	    for line in read_file:
	        if line.find(Item["db_en"].encode('utf-8')) >= 0:
                    line = line.replace(db_en, db_jp)
                write_file.write(line.encode('utf-8'))


    read_file.close()
    write_file.close()

#if os.path.isfile(sys.argv[1]) and os.path.isfile(temp_file):
#    os.remove(sys.argv[1])
#    os.rename(temp_file, sys.argv[1])


if __name__ == '__main__':

    import json
    import sys
    import LoadParameters
    import argparse
    import os
    import re
    import codecs

    parser = argparse.ArgumentParser('InsertNameJp.py')
    parser.add_argument('-f', '--filein', help='Excel file', required=True)
    args = parser.parse_args()
    r = LoadParameters.ReadXl(args.filein)

    InsertNameJp(r)
