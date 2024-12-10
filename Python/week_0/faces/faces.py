def main():
    convert()

def convert():
    replace = input()

    if ":)" in replace or ":(" in replace:
        replace = replace.replace(":)", "🙂").replace(":(", "🙁")

    print(replace)

main()
