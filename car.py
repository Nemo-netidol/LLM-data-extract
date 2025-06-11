import requests
from bs4 import BeautifulSoup
from chat import extract_information
import re


headers = {"User-Agent":"Mozilla/5.0"}
url = requests.get("https://www.history.com/articles/car-history-timeline")
soup = BeautifulSoup(url.content, "html.parser")

divs = soup.find_all("div", id=re.compile('^main-content'))


text = '\n\n\n'.join(div.get_text() for div in divs)
# print(text)

extract_information(text, "car")

