from openai import OpenAI
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)

def extract_information(text: str, topic: str):

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

    result = completion.choices[0].message.content

    folder_path = f'./{topic}'

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    with open(f"{folder_path}/data.txt", "w") as f:
        f.write(text)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    with open(f"{folder_path}/extract-information.txt", "w") as f:
        f.write(result)