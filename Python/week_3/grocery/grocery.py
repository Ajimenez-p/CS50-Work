def main():
    grocery_list = {}
    while True:
        try:
            item = input().strip().lower()
            if item in grocery_list:
                grocery_list[item] += 1
                continue
            else:
                grocery_list[item] = 1
                continue
        except EOFError:
            for item in sorted(grocery_list):
                print(f'{grocery_list[item]} {item.upper()}')
            break


main()
