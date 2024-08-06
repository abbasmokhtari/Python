def oddEven():
    while True:
        try:
            userInput = int(input('Type a number:'))
        except ValueError:
            print('Sorry wrong input.')
        else:
            break
    if userInput % 2 == 0:
        print(f'{userInput} is even.')
    else:
        print(f'{userInput} is odd.')


oddEven()