#!/usr/bin/env python
# -*- coding: utf_8 -*- 

def InsertNameJp(r):

    read_file = None
    write_file = None
    temp_code = "temp_code"
    read_file = open("code.js", 'r')
    write_file = open(temp_code, 'w')
    i = 0;
    j = 0;
    k = 0;
    l = 0;
    en_heroes = {};
    jp_heroes = {};
    en_skills = {};
    jp_skills = {};

    Sheet = r["base_heroes"]
    for Item in tqdm(Sheet):
     	if Item["base_jp"] is not None:
	    en_heroes[i] = Item["base_en"]
    	    jp_heroes[i] = Item["base_jp"]
            i += 1
    	
    Sheet = r["base_skills"]
    for Item in tqdm(Sheet):
     	if Item["base_jp"] is not None:
	    en_skills[k] = Item["base_en"]
    	    jp_skills[k] = Item["base_jp"]
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
	
#    if os.path.isfile(db.js) and os.path.isfile(temp_code):
#        os.remove(db.js)
#        os.rename(temp_code, db.js)

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
