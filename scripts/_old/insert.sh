#! /bin/bash

# perl -pe 's/\[\{/\[\n\t\{\n\t\t/g; s/\}\]/\n\t\}\n\]/g; s/\},\{/\n\t\},\{\n\t\t/g; s/data\./window\.data\./g' db.jss > db.js
IFS=$'\t'

while read LINE; do
	tsvList=(`echo "$LINE"`)
#	rename -s ${tsvList[0]} ${tsvList[1]} ../skills/*.png
	sed -i -e s/\t\t${tsvList[0]}/\r\t\t${tsvList[1]}/g db.js
done < rename.tsv

while read LINE; do
	tsvList=(`echo "$LINE"`)
	sed -i -e s/\t\t${tsvList[0]}/\r\t\t${tsvList[1]}/g db.js
done < rename-skill.tsv
