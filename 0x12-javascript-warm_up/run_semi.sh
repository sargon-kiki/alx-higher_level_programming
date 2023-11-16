#!/bin/bash

# Find all JavaScript files in the current directory and its subdirectories
files=$(find . -name "*.js")

# Loop through each file and run semistandard --fix
for file in $files
do
  semistandard --fix "$file"
done