#/bin/bash
#script that takes URL and sends request to the URL
curl -s "$1" | wc -c
