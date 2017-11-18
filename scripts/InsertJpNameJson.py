#!/usr/bin/env python
# -*- coding: utf_8 -*-

def InsertNameJp(r):

    read_hero = None
    read_skill = None

    write_hero = None
    write_skill = None

    read_hero = open("../../FEH-Mass-Simulator/json/hero.json", 'r')
    read_skill = open("../../FEH-Mass-Simulator/json/skill.json", 'r')

    write_hero = open("hero.json", 'w')
    write_skill = open("skill.json", 'w')

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
            i += 1

    Sheet = r["name_skills"]
    for Item in tqdm(Sheet):
     	if Item["db_jp"] is not None:
            en_skills[k] = u'\t\t' + Item["db_en"]
            jp_skills[k] = u'\t\t' + Item["db_en"] + u'\n\t\t' + Item["db_jp"]
            k += 1

    for line in tqdm(read_hero):
        line = line.replace("name", "name_en")
        for j in range(len(jp_heroes)):
            if line.find(en_heroes[j]) != -1:
                line = line.replace(en_heroes[j], jp_heroes[j])
        write_hero.write(line.encode('utf-8'))

    for line in tqdm(read_skill):
        for l in range(len(jp_skills)):
            if line.find(en_skills[l]) != -1:
                line = line.replace(en_skills[l], jp_skills[l])
        write_skill.write(line.encode('utf-8'))

    read_hero.close()
    read_skill.close()
    write_hero.close()
    write_skill.close()



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
