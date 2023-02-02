#!/bin/bash

OUT_DIR="out"
ARTICLE_URLS_FILE="links"
OUT_DIR_BASE_FILE="index.html"

CUSTOM_WEBSITE="YOUR-CUSTOM-WEBSITE" # Can be powered by surge
LMD_COOKIE="YOUR-LE-MONDE-COOKIE"
ACCESS_TOKEN="YOUR-POCKET-ACCOUNT-ACCESS-TOKEN"
CONSUMER_KEY="YOUR-POCKET-APP-CONSUMER-KEY"

rm -r $OUT_DIR
mkdir $OUT_DIR

echo "Loading articles from selections"
python load_articles.py $OUT_DIR $OUT_DIR_BASE_FILE $LMD_COOKIE

echo "Uploading articles to custom server"
surge $OUT_DIR $CUSTOM_WEBSITE

echo "Uploading articles to Pocket"
echo "" > $ARTICLE_URLS_FILE
for f in $(ls $OUT_DIR)
do
    if [ $f != $OUT_DIR_BASE_FILE ]
    then
        echo $f >> $ARTICLE_URLS_FILE
    fi
done
python pocket_upload.py $CUSTOM_WEBSITE $ARTICLE_URLS_FILE $ACCESS_TOKEN $CONSUMER_KEY

echo "Done!"
read