#!/bin/bash
# Send a GET request to a given URL and get the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
