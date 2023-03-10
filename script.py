import requests
#Import the config.py file that contains API key etc.....
from config import client_ID, client_secret

print(client_ID)
print(client_secret)

url = "https://developer.dexcom.com/docs/dexcomv2/operation/getEstimatedGlucoseValuesV2/api.dexcom.com/v2/users/self/egvs"

query = {
  "startDate": "2019-08-24T14:15:22Z",
  "endDate": "2019-08-24T14:15:22Z"
}

headers = {"Authorization": "Bearer "+client_secret}

response = requests.get(url, headers=headers, params=query)

data = response.json()
print(data)