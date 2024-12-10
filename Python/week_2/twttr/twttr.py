def main():
    
    subject = input('Input: ').strip()
    output = ''

    for char in subject:
        if not is_vowel(char):
            output += char

    print(f'Output: {output}')


def is_vowel(char):
    return char.lower() in 'aeiou'


main()
