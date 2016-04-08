#!/bin/bash
URL=$1

if [ $URL ]; then
	/usr/local/bin/youtube-dl -citk $URL
else
	echo "insira a url"
	read URL
	/usr/local/bin/youtube-dl -citk $URL
fi

