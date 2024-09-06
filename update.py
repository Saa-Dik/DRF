#akn amra data ke update korbo

import request
import json
URL = ""

# amra get rquest send korbo jate amader database ar table teke data paite pari
def get_data(id = None):
    data = {}
    if id is not None: #jodi id te kono value take tobe databaser id nicher id te asbe
        data = {'id': 'id'}
    json_data = json.dumps(data)

    res = request.get(url = URL, data=json_data)
    data =res.json()
    print(data)
get_data(1)
