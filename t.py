import requests

url = "https://t.me/source_7etan"
response = requests.get(url).content
print(response.index("tgme_page_photo_image"))
