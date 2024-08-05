# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apple', 'Oranges', 'Grapes')

# We can also use a constructor
fruits2 = tuple(('Apples', '`oranges', 'Grapes'))

# If there is without comma Python treats it as string

fruits3 = ('Banana')

# Single Value needs  trailing comma 
fruits4 = ('Berry',)


print(fruits3, type(fruits3), fruits4, type(fruits4))

# Get Value 
print(fruits[0])

# Can't change value -  following command returns an error
#fruits[0] = 'Pears'

# Delete tuple
del fruits2

# this will come with error
#print(fruits2)

# Get Length

print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.


# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if something is in set - this will return True or Flase

print('Apples' in fruits_set)


# Add to set
fruits_set.add('Grape')

print(fruits_set)

# Remove from set
fruits_set.remove('Mango')

print(fruits_set)

# Clear set entirely 
fruits_set.clear()

print(fruits_set)

# Delete set

del fruits_set

# Once deleted print will come up with error
print(fruits_set) 