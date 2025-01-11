#!/bin/bash
#
# This script recurseively traverses the subdirectories of the current directory
# and renames all of the tif files from the old convention to the new convention

# Get the directory path from the command line argument
dir_path=`pwd`

# Function to rename .tif files in a directory
rename_tif_files() {
    local current_dir="$1"
    local dir_basename=$(basename "$current_dir")

    # Find all .tif files in the current directory
    find "$current_dir" -maxdepth 1 -type f -name "*.tif" | while read -r file; do
        # Get the filename without the path
        filename=$(basename "$file")
        
        # Create the new filename
        new_filename="${dir_basename}-${filename}"
        
        # Rename the file
        mv "$file" "$(dirname "$file")/$new_filename"
        
        echo "Renamed: $filename -> $new_filename"
    done
}

# Traverse the directory and its subdirectories
find "$dir_path" -type d | while read -r dir; do
    rename_tif_files "$dir"
done

echo "Renaming complete."

