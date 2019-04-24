import requests
from bs4 import BeautifulSoup
import deepcut
# -*- coding: utf-8 -*-

def run(text):
    text = get_news(text)
    # text = word_segment(text)
    return text


def get_news(text):
    web_token = requests.get(text)
    html_parser = BeautifulSoup(web_token.text, 'html.parser')

    paragraphs = html_parser.find_all("p")
    content = []
    for p in paragraphs:
        content.append(p.getText())
        text = "\n".join(content)
    return text


def word_segment(text):
    text = deepcut.tokenize(text, custom_dict="custom_dict/custom_dict.txt")
    text = "|".join(text)
    return text
