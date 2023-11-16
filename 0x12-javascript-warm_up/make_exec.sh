#!/bin/bash

# Find all JavaScript files in the current directory and its subdirectories
files=$(find . -name "*.js")

# Loop through each file and set execute permissions
for file in $files
do
  chmod +x "$file"
done