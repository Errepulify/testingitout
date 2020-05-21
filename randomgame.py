from random import randint
import sys
# you will need to run this on your machine and not this website for the sys.argv to work!
# Testing git out


answer = randint(sys.argv[1], sys.argv[2])

while True:
    try:
        print(answer)
        guess = int(input('Guess a number between 1 ~ 10:  '))

        if 0 < guess < 11:
            if guess == answer:
                print('You are a genius')
                break
        else:
            print('Hey smartass, I said 1~10')
    except ValueError:
        print('Please enter a number')
        continue


