print('Welcome to my quiz!')

playing = input('Do you want to play? ')

if playing.lower() not in ['yes', 'y']:
    quit()

print("Ok let's play")
score = 0

answer = input('What does CPU stand for? ')

if answer.lower() == 'central processing unit':
    print('correct')
    score += 1
else:
    print('incorrect')


answer = input('What does GPU stand for? ')

if answer.lower() == 'Graphics processing unit':
    print('correct')
    score += 1
else:
    print('incorrect')


answer = input('What does RAM stand for? ')

if answer.lower() == 'random access memory':
    print('correct')
    score += 1
else:
    print('incorrect')


answer = input('What does PSU stand for? ')

if answer.lower() == 'power supply':
    print('correct')
    score += 1
else:
    print('incorrect')


print(f'You got {score} questions correct')
print(f'You got {score / 4 * 100} %')