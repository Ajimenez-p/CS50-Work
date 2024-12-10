"""
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2,
restructuring your code per the below, wherein shorten expects a str as input and
returns that same str but with all vowels (A, E, I, O, and U) omitted, whether
 inputted in uppercase or lowercase.
"""

def main():
    while True:
        i = input('Input: ').strip()
        if not i or i.lstrip('-').replace('.', '', 1).isdigit():
            continue
        else:
            print(shorten(i))
            break


def shorten(i):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join([char for char in i if char not in vowels])


if __name__ == '__main__':
    main()
