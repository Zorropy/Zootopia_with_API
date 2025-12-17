import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")



def load_data(user_input):
    BASE_URL = "https://api.api-ninjas.com/v1/animals"

    params = {"name": user_input}

    headers = {"X-Api-Key": API_KEY}

    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()
    return data

