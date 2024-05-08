import random
playing=input('dou you want to play number guessing game? ')
if playing.lower() != 'yes':
    quit()
upper_range=input('type a number so you can guess a number from 1 to that number ' )
if upper_range.isdigit():
    if upper_range > '0':
        upper_range=int(upper_range)
    else:
        print('enter a number larger than 0 next time ')
        quit()
else:
    print('enter a number next time')
    quit()
random_number=random.randint(1,upper_range)
count=0
while True:
    count+=1
    user_guess=input('Make a guess ')
    if user_guess.isdigit():
       user_guess=int(user_guess)
    else:
       print('enter a number next time')
       continue
    if user_guess == random_number :
        print('you got it right! in ' + str(count) + ' attempts')
        break
    else:
        print('you got it wrong!')
        continue

