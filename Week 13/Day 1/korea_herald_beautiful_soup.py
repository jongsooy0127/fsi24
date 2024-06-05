# Using Python and what you've learned so far, repeat the previous exercise and
# retrieve the "Most Popular" article headlines from the Korea Herald website.
# This time, use the BeautifulSoup package. Like before, list the headlines in
# the following format:
# [1]: Headline 1
# [2]: Headline 2
# [n]: Headline n

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.koreaherald.com/")
soup = BeautifulSoup(r.text, 'html.parser')

title_container = soup.select('p.news_title')
# print(title_container)

for i,title in enumerate(title_container):
    title_text = title.select_one('span.ellipsis2').text
    print(f"[{i+1}]: {title_text}")