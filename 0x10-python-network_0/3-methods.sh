#!/bin/bash
# Script that takes URL and shows Allowed OPTIONS
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
