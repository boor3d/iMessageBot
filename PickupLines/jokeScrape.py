import requests
from bs4 import BeautifulSoup
import re

base_url = "https://parade.com/1039985/marynliles/pick-up-lines/"

html_content = requests.get(base_url).text

soup = BeautifulSoup(html_content, "html.parser")

texts = soup.find_all('p')

pickup_lines = []

for text in texts:
    pickup_lines.append(text.get_text())


del pickup_lines[:3]
del pickup_lines[-3:]
with open ("PickupLines.txt", "w", encoding='utf-8') as f:
    pattern = r'[\d.]'
    for line in pickup_lines:
        edit_line = re.sub(pattern, '', line)
        f.write(edit_line + "\n")
