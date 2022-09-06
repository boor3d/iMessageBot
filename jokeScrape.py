import requests


URL = "https://parade.com/1040121/marynliles/one-liners/"

page = requests.get(URL)


print(page.text)
