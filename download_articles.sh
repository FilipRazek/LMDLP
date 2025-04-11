#!/bin/bash

rm -rf "$OUT_DIR"
mkdir "$OUT_DIR"

python3 load_articles.py "$OUT_DIR" "$OUT_DIR_BASE_FILE" "$LMD_M_COOKIE" "$LMD_S_COOKIE" "$ARTICLE_NAMES_FILE"

exit 0
