# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# it's like JSON in a way it has key value pair 

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 40
}


# We can also use constructor
person2 = dict(firstname='Sara', last_name='Williams', age=30)


# Get value 
print(person['first_name'])

# We can also get value using Get
print(person.get('last_name'))

# Add key/value
person['phone'] = '07777-777-777' 

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# copy dict
person3 = person.copy()
person3['city'] = 'London'

# Remove item
del(person['age'])

# We can also remove using pop
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person3))

# List of dict
people = [
    {'name': 'Martha', 'age': 23},
    {'name': 'Ben', 'age': 43}
]

# If we were to get the name of the first person in this example
print(people[0]['name'])