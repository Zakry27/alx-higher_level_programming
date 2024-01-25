#!/bin/bash
# Script that sends request to URL passed as argument, and displays only status code of response
curl -so /dev/null -w "%{http_code}" "$1"
