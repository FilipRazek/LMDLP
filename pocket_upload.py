import requests
import sys


def build_pocket_add_action(url):
    return {
        "action": "add",
        "url": url
    }


def upload_pages_to_pocket(urls, access_token, consumer_key):
    POCKET_MODIFY_URL = "https://getpocket.com/v3/send"
    actions = [build_pocket_add_action(url) for url in urls]
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


[custom_website, links_file_name, access_token, consumer_key] = sys.argv[1:]

urls = []
with open(links_file_name, "r") as f:
    for line in f.readlines():
        article_url = line[:-1]
        if len(article_url) > 1:
            urls.append("{}/{}".format(custom_website, article_url))
upload_pages_to_pocket(urls, access_token, consumer_key)
