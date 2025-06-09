from openai import OpenAI
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests


load_dotenv()
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)


url = requests.get("https://freelinuxtutorials.com/linux-timeline/")
soup = BeautifulSoup(url.content, "html.parser")
data = soup.find("article")
# print(data.find_all("br"))

p_tags = data.find_all("p")

text = "\n\n\n".join(p.get_text() for p in p_tags)

# print(text)

# with open("data.txt", "w") as f:
#     f.write(text)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Your task is to extract and summarize a useful timeline information about the technology from the given text."
        },
        {
            "role": "user",
            "content": text
        }
    ]
)

print(completion.choices[0].message.content)

with open("information.txt", "w") as f:
    f.write(completion.choices[0].message.content)