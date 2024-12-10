def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if plate starts with at least two letters
    start_letters = False
    character_length = False
    punctuation = True
    numbers = True

    if s[:2].isalpha():
        start_letters = True

    # Check if length is between 2 and 6 characters
    if 2 <= len(s) <= 6:
        character_length = True

    # Check if numbers follow rules (no leading 0, no letters after numbers)
    numbers_started = False
    for index, char in enumerate(s):
        if char.isdigit():
            if not numbers_started:
                if char == '0':
                    numbers = False
                    break
                numbers_started = True
        else:
            if numbers_started:
                numbers = False
                break

    # Check if plate is alphanumeric (no punctuation)
    for char in s:
        if not char.isalnum():
            punctuation = False
            break

    return start_letters and character_length and punctuation and numbers


if __name__ == "__main__":
    main()
