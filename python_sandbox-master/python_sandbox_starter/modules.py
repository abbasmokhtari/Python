# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
# We could have just imported date fro date time and change today to date.today()
from datetime import date
import time
from time import time
#today = datetime.date.today()

# pip module
#from camelcase import CamelCase

# Import custom module / it is custom made and saved as validator.py in our folder
import validator
from validator import validate_email


today = date.today()
#timestamp = time.time()
timestamp = time()

#c = CamelCase()

#print(c.hump('hello there world'))

print(today, timestamp)

email = 'test@test.com'
if validate_email(email):
    print('This email is valid')
else:
    print('This email is not valid')

# pip is similar to node 
# For example if we were to install camelcase pkg we run a command like this in terminal / pip3 install camelcase

# command to see what's installed is pip3 freeze