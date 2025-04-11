#!/bin/bash

export OUT_DIR="out"
export ARTICLE_URLS_FILE="links"
export OUT_DIR_BASE_FILE="index.html"
export ARTICLE_NAMES_FILE="article_names"

export CUSTOM_WEBSITE="YOUR_CUSTOM_WEBSITE"
export LMD_M_COOKIE="YOUR_LMD_M_COOKIE"
export LMD_S_COOKIE="YOUR_LMD_S_COOKIE"
export ACCESS_TOKEN="YOUR_POCKET_ACCESS_TOKEN"
export CONSUMER_KEY="YOUR_POCKET_CONSUMER_KEY"
export SURGE_LOGIN="YOUR_SURGE_LOGIN"
export SURGE_TOKEN="YOUR_SURGE_TOKEN"

./download_articles.sh
./upload_online.sh
./upload_to_pocket.sh
