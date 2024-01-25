#!/bin/bash
# Bash script that takes in URL, sends GET request and displays only  body of 200 status code response
curl -Ls "$1"
