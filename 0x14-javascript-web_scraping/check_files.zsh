#!/bin/zsh

# Check if semistandard is installed
if ! command -v semistandard &> /dev/null; then
    echo "Error: semistandard is not installed. Please run 'npm install -g semistandard' to install it."
    exit 1
fi

# Check all JS files in the current directory
for file in *.js; do
    if [ -f "$file" ]; then
        echo "Checking $file..."
        semistandard --fix "$file"
    fi
done

echo "Finished checking JavaScript files."
