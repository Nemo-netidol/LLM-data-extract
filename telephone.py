import requests
from bs4 import BeautifulSoup
from chat import extract_information


headers = {"User-Agent":"Mozilla/5.0"}
url = requests.get("https://www.nationalitpa.com/history-of-telephone", headers=headers)
soup = BeautifulSoup(url.content, "html.parser")
data = soup.find_all("p")
# text = "\n\n\n".join(p.get_text() for p in data)

list = soup.find("ol")

text = list.get_text()

with open("./telephone/data.txt", "w") as f:
    f.write(text)

with open("./telephone/extract-information.txt", "w") as f:
    summary = extract_information(text)
    f.write(summary)
