#!/bin/bash

# Check if a directory argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory_with_cpp_files>"
  exit 1
fi

CPP_DIR="$1"

# Set the output directory for executables (optional)
OUTPUT_DIR="./bin"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Check if there are any .cpp files in the specified directory
if ! ls "$CPP_DIR"/*.cpp 1> /dev/null 2>&1; then
  echo "No .cpp files found in the specified directory: $CPP_DIR"
  exit 1
fi

# Loop through all .cpp files
for file in "$CPP_DIR"/*.cpp; do
  # Extract the filename without the extension
  base_name="$(basename "$file" .cpp)"

  # Compile the file
  g++ "$file" -O3 -o "$OUTPUT_DIR/$base_name" 2> /dev/null

  # Check for compilation errors
  if [ $? -eq 0 ]; then
    echo "Compiled: $file -> $OUTPUT_DIR/$base_name"
  else
    echo "Error compiling: $file"
  fi

done