import requests 
import json
URL = "http://127.0.0.1:8000/student-delete/"

data = {
    'id': 2,
}
json_data = json.dumps(data)
res = requests.delete(url=URL, data= json_data)
data = res.json()
print(data)
