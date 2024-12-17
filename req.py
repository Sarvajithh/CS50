import requests
import json
response =requests.get("https://www.youtube.com/watch?v=nLRL_NcnK-4&list=WL")
try:
    data = json.dump(response.json())  # Attempt to parse JSON
    print(data)
except requests.exceptions.JSONDecodeError:
    print("Response is not in JSON format")

