#!/bin/bash

ls *.xml | while read FILE; do
	NewName=`grep 'identifier' $FILE | cut -d'>' -f 2 | cut -d'.' -f1 | cut -d'<' -f1 |awk '{print $0 ".xml";}'`
	if [ "$NewName" != "" ] ; then
		mv $FILE $NewName
	else 
		echo "$FILE doesn't have identifier"
	fi
done