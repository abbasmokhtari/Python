op = input("Please choose your operator: +, -, / and * ")

def cal(op):
    a= int(input("give a:"))
    b = int(input("give b:"))
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        return a / b
    elif op == "*":
        return a * b
c = op.strip() #We used strip to get rid of spaces in input
if c == "+" or c == "-" or c == "/" or c == "*" :
    print(cal(c))
else: 
    print("Please try again") #new note