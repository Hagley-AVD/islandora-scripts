#!/bin/bash
sed -i 's/<\/mods>/<\/mods>\n\n\n/' *.xml
cat $1 | sed  's/\(<[A-Za-z]\+.*>null<\/\)\([A-Za-z]\+\)\(>\)/<\2\/>/g' | csplit -f record - '/<mods.xmlns/' '{*}'
for file in record*
do
	mv "$file" "$file.xml"
	sed -i '1i <?xml version="1.0" encoding="utf-8"?>' "$file.xml"
done
#the above sed needs to conform to POSIX BRE (if you want to change it)
#instructions: bash mods-split.sh nameOfFileToRunOn
