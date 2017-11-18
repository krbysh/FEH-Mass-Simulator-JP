#!/usr/bin/env python
# -*- coding: utf_8 -*-

def InsertNameJp(r):

    read_file = None
    write_file = None
    temp_db = "temp_db"
    read_file = open("db.js", 'r')
    write_file = open(temp_db, 'w')
    i = 0;
    j = 0;
    k = 0;
    l = 0;
    en_heroes = {};
    jp_heroes = {};
    en_skills = {};
    jp_skills = {};

    Sheet = r["name_heroes"]
    for Item in tqdm(Sheet):
     	if Item["db_jp"] is not None:
            en_heroes[i] = u'\t\t' + Item["db_en"]
    	    jp_heroes[i] = u'\t\t' + Item["db_en"] + u'\n\t\t' + Item["db_jp"]
#   	    en_heroes[i] = Item["db_en"]
#    	    jp_heroes[i] = Item["db_en"] + Item["db_jp"]
            i += 1

    Sheet = r["name_skills"]
    for Item in tqdm(Sheet):
     	if Item["db_jp"] is not None:
            en_skills[k] = u'\t\t' + Item["db_en"]
            jp_skills[k] = u'\t\t' + Item["db_en"] + u'\n\t\t' + Item["db_jp"]
#            en_skills[k] = Item["db_en"]
#    	    jp_skills[k] = Item["db_en"] + Item["db_jp"]
            k += 1

    for line in tqdm(read_file):
	for j in range(len(jp_heroes)):
            if line.find(en_heroes[j]) != -1:
	        line = line.replace(en_heroes[j], jp_heroes[j])
	for l in range(len(jp_skills)):
            if line.find(en_skills[l]) != -1:
	        line = line.replace(en_skills[l], jp_skills[l])
        write_file.write(line.encode('utf-8'))

    read_file.close()
    write_file.close()

#    if os.path.isfile(db.js) and os.path.isfile(temp_db):
#        os.remove(db.js)
#        os.rename(temp_db, db.js)

if __name__ == '__main__':

    import json
    import os
    import sys
    import LoadParameters
    import argparse
    import re
    import codecs
    from tqdm import tqdm
    import time
    reload(sys)
    sys.setdefaultencoding('utf-8')

    parser = argparse.ArgumentParser('InsertNameJp.py')
    parser.add_argument('-f', '--filein', help='Excel file', required=True)
    args = parser.parse_args()
    r = LoadParameters.ReadXl(args.filein)

    InsertNameJp(r)
