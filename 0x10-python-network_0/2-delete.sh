#!/bin/bash
# script that sends DELETE request to URL passed as first argument and displays body of response
curl -s "$1" -X DELETE
