import requests
import sys
import json
from helpers import slugify


def build_pocket_add_action(url, title):
    return {
        "action": "add",
        "url": url,
        "title": title
    }


def upload_pages_to_pocket(urls, access_token, consumer_key):
    POCKET_MODIFY_URL = "https://getpocket.com/v3/send"
    actions = [build_pocket_add_action(url, name) for (url, name) in urls]
    data = {
        "access_token": access_token,
        "consumer_key": consumer_key,
        "actions": actions
    }
    headers = {"Content-Type": "application/json; charset=UTF-8",
               "X-Accept": "application/json"}
    response = requests.post(POCKET_MODIFY_URL, json=data, headers=headers)
    if response.status_code != 200:
        raise Exception(response)


if len(sys.argv) <= 1:
    raise Exception("Expected argument for the custom domain")

if len(sys.argv) <= 2:
    raise Exception(
        "Expected argument with the name of the file containing article URLs")

if len(sys.argv) <= 3:
    raise Exception("Expected argument for access_token")

if len(sys.argv) <= 4:
    raise Exception("Expected argument for consumer_key")

if len(sys.argv) <= 5:
    raise Exception("Expected argument for article_names file name")


[custom_website, links_file_name, access_token,
    consumer_key, article_names_file] = sys.argv[1:]

urls = []
article_names = json.load(open(article_names_file))
with open(links_file_name, "r") as f:
    for line in f.readlines():
        article_url = slugify(line[:-1].strip())
        if len(article_url) > 1:
            urls.append(("{}/{}".format(custom_website, article_url),
                        article_names[article_url]))
upload_pages_to_pocket(urls, access_token, consumer_key)
