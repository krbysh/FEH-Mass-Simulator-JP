#! /bin/bash

# perl -pe 's/\[\{/\[\n\t\{\n\t\t/g; s/\}\]/\n\t\}\n\]/g; s/\},\{/\n\t\},\{\n\t\t/g; s/data\./window\.data\./g' db.jss > db.js
IFS=$'\t'

while read LINE; do
	tsvList=(`echo "$LINE"`)
	rename -s ${tsvList[0]} ${tsvList[1]} ../skills/*.png
done < rename.tsv
