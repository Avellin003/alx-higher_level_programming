#!/bin/bash
#this is script tha display the URL methods accepted
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
