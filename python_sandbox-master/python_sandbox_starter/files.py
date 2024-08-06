# Python has functions for creating, reading, updating, and deleting files.


# Open a file which is the same as creating
myFile = open('myFile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I am learning Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write(' I also like C')
myFile.close()


# Read form file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)  # This means we want to read 100 character
print(text)