# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Gavin', 'Sara', 'Fresia']

# Simple for loop
for person in people:
    print(f'Current person: {person}')

# Break in this example we stopped as soon as we hit Sara
for person in people:
    if person == 'Sara':
        break
    print(f'current person: {person}')

# contniue  in this example we just didn't print Sara
for person in people:
    if person == 'Sara':
        continue
    print(f'Current person: {person}')

# range
for i in range(len(people)):
    print(people[i])


for i in range(1, 8):   # in this example it won't count the last number in range
    print(f'Number is: {i}')

# While loops execute a set of statements as long as a condition is true.


count = 0
while count <= 5:
    print(f'Count: {count}')
    count += 1
    