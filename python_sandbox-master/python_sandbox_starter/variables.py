# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
#variable types
x = 1         #int
y = 2.5       #float
name = 'John' #str
is_cool = True  #bool T or F must be in capital


#Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

print(x, y, name, is_cool)

#I we wanted to chang the type of variable also known as Casting
x = str(x)
y = int(y)
z = float(y)



#If we wanted to check the type of a variable
print(type(x))
print(type(y) , y)
print(type(z) , z)
