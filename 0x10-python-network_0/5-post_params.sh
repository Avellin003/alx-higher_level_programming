#!/bin/bash
#this is a script that allows the transfer of data
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
