# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary


import json

# Sample JSON
userJSON = '{"first_name": "Abbas", "last_name": "Mokhtari", "age": 44}'

# Parse JSON to Dictionary 
user = json.loads(userJSON)

print(user)
print(user['first_name'])


# Turn a dict to JSON

car = {
    'make': 'Mercedes',
    'model': 'E200',
    'year': 2020
}

carJSON = json.dumps(car)

print(carJSON)