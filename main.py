import requests
# from requests.auth import HTTPBasicAuth
from datetime import datetime
import os

# Using Enviornmental Variable
NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHETTY_ENDPOINT = os.environ.get("ENV_SHETTY")
BEARER_AUTHENTICATION = os.environ.get("BEARER_AUTH")
auth_username = os.environ.get("USERNAME")
auth_password = os.environ.get("AUTH_PASSWORD")
USERNAME = "Abyzola"
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

GENDER = "female"
WEIGHT_KG = 53.02
HEIGHT_CM = 167.64
AGE = 18

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": input("Tell me which excercise you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITION_ENDPOINT, json=params, headers=headers)
result = response.json()

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
# print(result)
# print(result["exercises"])

for item in result["exercises"]:
    data = {
        "sheet1": {
            "date": today,
            "time": time,
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"]
        }
    }
    respond = requests.post(url=SHETTY_ENDPOINT, json=data)
    print(respond.text)

    heading = {
        "Authorization": BEARER_AUTHENTICATION
    }
    sheet_response = requests.post(url=SHETTY_ENDPOINT, json=data, headers=heading)
    print(sheet_response.text)

# TRY INPUTTING THIS IN THE CONSOLE
# ran 5k and cycled 20 minutes
# I swam for 10 minutes then walked 2 miles
