# import random module in python
import random

# one way of using random is to specify a range like this "random.randrange(start, stop)" random.randrage(-1, 30) end limit is never included this range is between -1 to 29 if we just go like random.randrange(11) range will be from 0 to 10. 
# there is another function called randint() this one when used stop point of range is included random.randint(2, 10) means now 10 is also included in the range

top_of_range = input('Type a number: ')

# we want to make sure input is number and it is greater than zero
if top_of_range.isdigit(): # this will check input to see if it's a number and returns true of False 
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number biger than 0.')
        quit()
else:
    print('Please make sure you type a number.')
    quit()

# for practice change it to a loop that keeps asking until correct input is provided

random_number = random.randint(0, top_of_range)

while True:
    user_guess = input('Make a guess: ')