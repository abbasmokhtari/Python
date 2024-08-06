# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

     # method
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    # when this is called it adds one year to age
    def has_birthday(self):
        self.age +=1 


# Extend class
class Customer(User): #this basically copies User class into Customer class
        # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
    



# Initialize user object
abbas = User('Abbas Mokhtari', 'abbas@mokhtari.com', 44)
brad = Customer('Brad Traversy', 'brad@traversy.com', 37)


abbas.has_birthday() # now my age is one year more than what initially was put

print(abbas.greeting())

brad.set_balance(500)
brad.has_birthday() # this was run from User class which we originaly put in Customer class
print(brad.greeting())