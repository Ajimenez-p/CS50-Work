def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):
    #define all related requirements as variables
    start_letters = False
    character_length = False
    punctuation = False
    numbers = True

    #test start letters w/ 's'
    if s[:2].isalpha():
        start_letters = True

    #test character length
    if len(s) >= 2 and len(s) <=6:
        character_length = True

    #test numbers
    numbers_start = False
    for index, char in enumerate(s):
        #if char is a number
        if char.isdigit():
            if not numbers_start: #and numbers havent started yet
                if char == '0': #check if it is 0. if so, break loop and keep numbers false.
                    break
                numbers_start = True #if it's not 0, then numbers have started and it keeps checking other onees
        else: #if char is not a digit
            if numbers_start: #check if numbers have started
                numbers = False #if so, numbers is false

    #test punctuation
    for char in s:
        if not char.isalnum():
            break
        else:
            punctuation = True

    #test all conditions, return a bool
    if start_letters and character_length and punctuation and numbers:
        return True
    else:
        return False




main()
