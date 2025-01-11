#!/bin/bash
# This script recursively traverses the current directory and truncates the size of each .tif file
# to 14 bytes.  This is useful when doing practice script operations on a huge set of .tif files

# Store the provided directory path
dir_path=`pwd`

# Function to process .tif files
process_tif_files() {
    local current_dir="$1"
    
    # Find all .tif files in the current directory and its subdirectories
    find "$current_dir" -type f -name "*.tif" | while read -r file; do
        echo "Processing: $file"
        
        # Change the contents of the file to "Fake-Tif-File"
        echo "Fake-Tif-File" > "$file"
        
        echo "Modified: $file"
    done
}

# Start processing from the provided directory
process_tif_files "$dir_path"

echo "All .tif files have been processed."
