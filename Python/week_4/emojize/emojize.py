import emoji

def main():
    v = input('Input: ')
    output = emoji.emojize(v, language='alias')
    print(output)


main()
