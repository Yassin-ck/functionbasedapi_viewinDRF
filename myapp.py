import requests
import json

URL = 'http://127.0.0.1:8000/stuapi/'

def get_data(id = None ):
    data = {}
    if id is not None:
        data = {'id':id}
        
    headers = {'content-Type':'application/json'}
    
    json_data = json.dumps(data)
    response = requests.get(url=URL, headers=headers ,data=json_data)
    data = response.json()
    print(data)
    

# get_data()

def post_data():
    data = {
        'name':'sugiyan',
        'roll':300,
        'city':'calicut'
    }
    
    headers = {'content-Type':'application/json'}
    
    json_data = json.dumps(data)
    r = requests.post(url=URL , headers=headers, data = json_data)
    data = r.json()
    print(data)
    
post_data()


def update_data():
    data = {
        'id':4,
        'name':'anroop',
        'city':'kozhikode'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data = json_data)
    data = r.json()
    print(data)
    
# update_data()
    
    
def delete_data():
    data = {'id':1}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data = json_data)
    data = json.loads(r.content)
    print(data)


# delete_data()