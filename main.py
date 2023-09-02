# I TRIED USING ENVIRONMENT VARIABLE BUT IT CONFUSINGG
import requests
# from requests.auth import HTTPBasicAuth
from datetime import datetime
import os

NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# SHETTY_ENDPOINT = os.environ.get("ENV_SHETTY")
SHETTY_ENDPOINT = "https://api.sheety.co/91615104cfe72ed2688ac0b97cc238f4/withoutTracking/sheet1"
BEARER_AUTHENTICATION = "Bearer gfdse5r6788oi9plkgfrr768ijngt8hgfy7"
# BASIC_AUTH_ENDPOINT ="https://httpbin.org/basic-auth/user/pass"

auth_username = "abyzola"
auth_password = "Abyzolami01*"

USERNAME = "Abyzola"
APP_ID = "c266a587"
API_KEY =  "242fbee16d6f6141a50ec49e1ea30e35"
# os.environ["APP_ID"] = "c266a587"
# os.environ["APP_KEY"] = "242fbee16d6f6141a50ec49e1ea30e35"
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
# print(result)

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
# print(result)
# print(result["exercises"])

for item in result["exercises"]:
    # ran 5k and cycled 20 minutes
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

    # # BASIC AUTHENTICATION
    # # I swam for 10 minutes then walked 2 miles
    heading = {
        "Authorization": BEARER_AUTHENTICATION
    }
    sheet_response = requests.post(url=SHETTY_ENDPOINT, json=data, headers=heading)
    print(sheet_response.text)

    # Bearer Token Authentication

    # bearer_headers = {
    # "Authorization": "Bearer gfdse5r6788oi9plkgfrr768ijngt8hgfy7"
    # }
    # sheet_response = requests.post(url=SHETTY_ENDPOINT, json=data, headers=bearer_headers
    # }