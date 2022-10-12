import requests
from bs4 import BeautifulSoup
import re

base_url = "https://mytreno.com/sports-facts-random-interesting/"

html_content = requests.get(base_url).text


soup = BeautifulSoup(html_content, "html.parser")



text = soup.find_all('ol')



# with open ("sportFacts.txt", "w", encoding='UTF-8') as f:
#     pattern = r'[\d.]'
#     for line in pickup_lines:
#         edit_line = re.sub(pattern, '', line)
#         f.write(edit_line + "\n")