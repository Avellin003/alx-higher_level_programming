#!/bin/bash
#sends the JSON POST reques
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
