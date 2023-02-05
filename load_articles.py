import requests
from os import path
from bs4 import BeautifulSoup
import sys


def fetch_page(link, m_cookie_value, s_cookie_value):
    cookies = {"lmd_a_m": m_cookie_value, "lmd_a_s": s_cookie_value}
    content = requests.get(link, cookies=cookies)
    return content.text


def fetch_selected_articles(m_cookie_value, s_cookie_value):
    SELECTED_ARTICLES_URL = "https://www.lemonde.fr/selections"
    ARTICLE_LINK_CLASS = "teaser__link"

    page_content = fetch_page(SELECTED_ARTICLES_URL,
                              m_cookie_value, s_cookie_value)
    soup = BeautifulSoup(page_content, 'html.parser')

    return [link["href"] for link in soup.find_all(class_=ARTICLE_LINK_CLASS)]


def extract_article_name(article_url):
    file_name = article_url.split("/")[-1]
    # Remove the extension if there is one
    return file_name.split(".")[0]


def get_text_content_from_content(content):
    FORBIDDEN_TAGS = {
        "div": ["dfp-slot", "dfp__slot"],
        "section": ["catcher", "catcher--inline", "inread", "article__reactions", "capping"],
        "blockquote": ["article__catchphrase"],
        "footer": ["article__footer-single", "old__article-footer"],
        "aside": ["aside__iso", "old__aside"],
        "ul": ["breadcrumb", "meta"],
        "figure": ["article__media"],
    }
    for tag in content.findChildren():
        # Remove tags that don't have an allowed name and have the correct class
        if tag.name not in FORBIDDEN_TAGS or not tag.has_attr('class'):
            continue
        for class_name in tag["class"]:
            if class_name in FORBIDDEN_TAGS[tag.name]:
                tag.decompose()
                break

    return str(content.prettify())


def download_article(article_url, out_dir, m_cookie_value, s_cookie_value):
    article_content = fetch_page(article_url, m_cookie_value, s_cookie_value)
    file_name = extract_article_name(article_url) + ".html"
    relative_file_path = path.join(out_dir, file_name)
    soup = BeautifulSoup(article_content, 'html.parser')

    with open(relative_file_path, "w") as file:
        file.write(get_text_content_from_content(soup.main))

    return file_name, soup.title.text


def build_html_link(href, text):
    return "<a href={}>{}</a>".format(href, text)


def build_directory_from_urls(urls, out_dir, index_file_name, m_cookie_value, s_cookie_value):
    index_file_path = path.join(out_dir, index_file_name)
    with open(index_file_path, "w") as file:
        file.write("<ul>")
    with open(index_file_path, "a") as file:
        for article_url in urls:
            file_name, article_title = download_article(
                article_url, out_dir, m_cookie_value, s_cookie_value)
            list_item_html = "<li>{}</li>".format(
                build_html_link(file_name, article_title))
            file.write(list_item_html)
        file.write("</ul>")


if len(sys.argv) <= 1:
    raise Exception("Expected output directory name as argument")

if len(sys.argv) <= 2:
    raise Exception("Expected output index file name as argument")

if len(sys.argv) <= 3:
    raise Exception("Expected M cookie for lemonde.fr")

if len(sys.argv) <= 4:
    raise Exception("Expected S cookie for lemonde.fr")

[out_dir, index_file_name, m_cookie, s_cookie] = sys.argv[1:]

urls = fetch_selected_articles(m_cookie, s_cookie)
print("Loading {} articles".format(len(urls)))
build_directory_from_urls(urls, out_dir, index_file_name, m_cookie, s_cookie)
