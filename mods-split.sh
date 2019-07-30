#!/bin/bash

cat $1 | sed  's/\(<[A-Za-z]\+.*>null<\/\)\([A-Za-z]\+\)\(>\)/<\2\/>/g' | csplit -f record - '/<mods.xmlns/' '{*}'
for file in record*
do
	mv "$file" "$1979285.xml"
done
#the above sed needs to conform to POSIX BRE (if you want to change it)
#instructions: bash mods-split.sh nameOfFileToRunOn
