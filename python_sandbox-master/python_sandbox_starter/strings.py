# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Abbas"
age = 44

#concatenate we have to cast everything into string

print('Hello my name is ' + name + ' and I am ' + str(age))



# String Formatting

# Arguments Formatting
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-String only available in Python version 3.6 above
print(f'Hello, My name is {name} again and I am {age}')

# String Methods

s = 'hello World'

#Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# make all lower
print(s.lower())

# Swap case 
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('World', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with / returns True or False
print(s.startswith('hello'))


# Ends with / same as above just check the other end
print(s.endswith('d'))

# split into a list / returns an array 
print(s.split())

# Find Position
print(s.find('h'))


# Is all alphanumeric -- in this example it gives False because there is space between hello and world
print(s.isalpha())

# Is all alphabetic -- in this example it gives False because there is space between hello and world
print(s.isalpha())

# Is all numeric 
print(s.isnumeric())