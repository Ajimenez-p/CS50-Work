def main():
    due = 50
    while due > 0:
        print(f'Amount Due: {due}')
        coin = int(input('Insert Coin: '))
        if coin in [25, 10, 5]:
            due -= coin

    if due < 0:
        owed = abs(due)
        print(f'Change Owed: {owed}')
    else:
        print('Change Owed: 0')

main()
