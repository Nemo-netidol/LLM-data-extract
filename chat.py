from openai import OpenAI
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests

load_dotenv()
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

def extract_information(text: str):

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
    return result
