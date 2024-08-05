# A List is a collection which is ordered and changeable. Allows duplicate members.


# Create list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor is another way of creating list
numbers2 = list((1,2,3,4,5))

# Get a value from list
print(fruits[1])

# Get the length of a list
print(len(fruits))  

# Append to the end of the list
fruits.append('Mangos')


# Remove from list
fruits.remove('Grapes')

# Insert into position 
fruits.insert(2, 'Strawberries')

# Change Value
fruits[0] =  'Blueberries'

# Remove with Pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse = True)

print(fruits)