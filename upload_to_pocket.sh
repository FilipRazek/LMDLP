#!/bin/bash

> "$ARTICLE_URLS_FILE"  # Truncate or create the file

for file in "$OUT_DIR"/*; do
    filename=$(basename "$file")
    if [[ "$filename" != "$OUT_DIR_BASE_FILE" ]]; then
        echo "$filename" >> "$ARTICLE_URLS_FILE"
    fi
done

python3 pocket_upload.py "$CUSTOM_WEBSITE" "$ARTICLE_URLS_FILE" "$ACCESS_TOKEN" "$CONSUMER_KEY" "$ARTICLE_NAMES_FILE"

exit 0
