
#new
#akn amra data ke update korbo
import requests
import json
URL = "http://127.0.0.1:8000/student_update/"
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url = URL, data =json_data)
    data = res.json()
    print(data)
get_data()

# amra get rquest send korbo jate amader database ar table teke data paite pari
# def get_data(id = None):
#     data = {}
#     if id is not None: #jodi id te kono value take tobe databaser id nicher id te asbe
#         data = {'id':id}
#     json_data = json.dumps(data)
#     res = requests.get(url = URL, data=json_data)
#     data =res.json()
#     print(data)
# get_data()


#amra toh age GET request ar jnno likhci akn amara POST method dekhbo 
# def post_data():
#     if id is not None:
#         data = {
#             'name':'mike',
#             'roll':'1321',
#             'city':'ctg',
#         } 
#         json_data = json.dumps(data)
#         resp = requests.post(url = URL, data =json_data)
#         data = resp.json()
#         print(data)

# post_data()