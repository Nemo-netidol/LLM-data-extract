import os
from bs4 import BeautifulSoup
import requests
import sys

from chat import extract_information, test


url = requests.get("https://freelinuxtutorials.com/linux-timeline/")
soup = BeautifulSoup(url.content, "html.parser")
data = soup.find("article")
# print(data.find_all("br"))

p_tags = data.find_all("p")

text = "\n\n\n".join(p.get_text() for p in p_tags)

information = extract_information(text)

with open("./linux/information.txt", "w") as f:
    f.write(information)


