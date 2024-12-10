def main():
    greeting = input('Greeting: ').strip().lower()
    if greeting.count('hello', 0,  6) == 1:
        print('$0')
    elif greeting.count('h', 0, 1) == 1:
        print('$20')
    else:
        print('$100')


main()
