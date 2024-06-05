import requests

# res = requests.get("https://google.com").text
# print(res)

r = requests.get("https://dog.ceo/api/breeds/list/all")
all_breeds = r.json()
print(all_breeds)