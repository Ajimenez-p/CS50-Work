import inflect

def main():
    p = inflect.engine()
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
