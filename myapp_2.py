# 3rd party API
import requests
import json
URL  =""
data = {
    'name': 'sadik',
    'roll': '119624',
    'city': 'Dhaka',
}
json_data = json.dumps(data)

res = requests.post(url=URL, data=json_data)
data = r.json()
print(data)