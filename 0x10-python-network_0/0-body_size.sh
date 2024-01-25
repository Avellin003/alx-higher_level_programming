#!/usr/bin/bash
#a bash script that takes URL and sends request to the URL
curl -s -w "%{size_download}\n" -o /dev/null ${1}
