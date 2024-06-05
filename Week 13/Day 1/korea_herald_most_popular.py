# Using Python and what you've learned so far, retrieve the "Most Popular"
# article headlines from the Korea Herald website. List the headlines in
# the following format:
# [1]: Headline 1
# [2]: Headline 2
# [n]: Headline n

import requests

res = requests.get("https://www.koreaherald.com/").text
res_popular_string = (res[res.find('<p class="news_title"><span class="ellipsis2">'):])
res_list = res_popular_string.split('<p class="news_title"><span class="ellipsis2">''')
res_list = ([item[:item.find('</span>')] for item in res_list if '</span>' in item])

for i,item in enumerate(res_list):
    print(f"[{i+1}]: {item}")