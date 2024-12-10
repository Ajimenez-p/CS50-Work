def main():
    answer = input('What is the answer to the Great Question of Life, the Universe, and Everything? ').lower()
    match answer:
        case "42" | "forty-two" | "forty two":
            return print("Yes")
        case _:
            return print("No")


main()
