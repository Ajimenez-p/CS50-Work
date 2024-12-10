import random
import sys

def main():

    x = get_level()

    while True:
        try:
            guess = int(input('Guess: '))
            if guess <= 0:
                continue
        except ValueError:
            continue

        if guess < x:
            print('Too small!')
            continue
        elif guess > x:
            print('Too large!')
            continue
        elif guess == x:
            print('Just right!')
            sys.exit()

    #if guess < x, output 'Too small!' and prompt again

    #if guess > x, output 'Too large!' and prompt again

    #if guess == x, output 'Just right!' and exit


def get_level():
    #prompt for level, n
    while True:
        try:
            n = int(input('Level: '))
        except:
            continue

  #if input not +
        if n < 0:
            continue #prompt again
        else:
    #randomly generate int 1 < x < n INCLUSIVE using random module
            x = random.randint(1, n)
            return x


if __name__ == '__main__':
    main()
