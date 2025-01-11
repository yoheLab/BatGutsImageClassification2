#!/bin/bash

# This script renames the folders of the Bat_guts from the old format to the new format
#

TOPDIR=$(basename "$(pwd)")
echo "TOPDIR=$TOPDIR"
STAINTYPE=
GUTTYPE=
remove_substring() {
    local string="$1"
    local substring="$2"
    
    # Use parameter expansion to remove the substring
    result="${string//$substring/}"
    
    echo "$result"
}
replace_substring() {
    local string="$1"
    local substring1="$2"
    local substring2="$3"
    
    # Use parameter expansion to replace substring1 with substring2
    result="${string//$substring1/$substring2}"
    
    echo "$result"
}
truncate_at_underscore() {
    local input_string="$1"
    
    # Count the number of underscores
    local underscore_count=$(echo "$input_string" | tr -cd '_' | wc -c)
    
    # Check if there are 1 or more underscores
    if [ "$underscore_count" -ge 1 ]; then
        # Cut the string at the first underscore
        local result="${input_string%%_*}"
        echo "$result"
    else
        # If less than 2 underscores, return the original string
        echo "$input_string"
    fi
}
# Loop through all directories in the current folder
for dir in */; do
    # Remove trailing slash from directory name
    dir=${dir%/}
        
    # Check if it's a directory
    if [ -d "$dir" ]; then
	BASENAME=$(basename "$dir")
	if [[ "$dir" == *"-AB-"* || "$dir" == *"_ab_"* ]]; then
		STAINTYPE="AB"
	else
		STAINTYPE="HE"
	fi
	if [[ "$dir" == *"NONguts"*  ]]; then
		GUTTYPE="NONguts"
	else
		GUTTYPE="guts"
	fi
	if [[ "$BASENAME" == *"_ab_"* ]]; then
		#echo "Removing _ab_ from $BASENAME"
		BASENAME=$(replace_substring "$BASENAME" "_ab_" "-")
		#echo "BASENAME is now $BASENAME"
	fi
	if [[ "$BASENAME" == *"-AB-"* ]]; then
		#echo "Removing -AB-_ from $BASENAME"
		BASENAME=$(replace_substring "$BASENAME" "_ab_" "-")
		#echo "BASENAME is now $BASENAME"
	fi
	BASENAME=$(truncate_at_underscore "$BASENAME" )
	#echo "after truncation, BASENAME is now $BASENAME"
        # Find the position of the last hyphen
        last_hyphen_pos=$(echo "$dir" | sed -e 's/[^-]//g' | awk '{ print length }')
	if [ "$last_hyphen_pos" -eq 0 ]; then
		# No hyphen found, just prepend the stain type
		new_name="${TOPDIR}-${GUTTYPE}-${STAINTYPE}-${BASENAME}"
	else
		# Insert the STAINTYPE before the last part
		new_name=${TOPDIR}-${GUTTYPE}-$(echo "$BASENAME" | sed "s/\(.*\)-/\1-${STAINTYPE}-/")
	fi
	if [[ "$new_name" == *"-AB-AB-"* ]]; then
		#echo "replace operation on $new_name"
		new_name=$(replace_substring $new_name "-AB-AB-" "-AB-")
		#echo "replaced name is now $new_name"
	fi

        # Rename the directory
        mv "$dir" "$new_name"
        
        echo "Renamed: $dir -> $new_name"
	#echo "#"
    fi
done

echo "Renaming complete."


