# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create Finction
def sayHello(name):
    print(f'Hello {name}')


# Return Value
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3,4)

print(num)
sayHello('Abbas')

print(getSum(2,4))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


gotSum = lambda num1, num2: num1 + num2

print(gotSum(10,5))