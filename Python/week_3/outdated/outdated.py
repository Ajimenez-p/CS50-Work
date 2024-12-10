def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        date = input('Date: ')

        # Check for numeric format
        if '/' in date:
            try:
                month, day, year = date.split('/')
                month = int(month)
                day = int(day)
                year = int(year)

                if valid_date(month, day, year):
                    print(f'{year:04}-{month:02}-{day:02}')
                    break
                else:
                    continue
            except ValueError:
                continue

        # Check for full month format
        elif any(month in date for month in months):
            try:
                parts = date.split()
                month = parts[0]
                day = int(parts[1].replace(",", ""))
                year = int(parts[2])

                month_number = get_month_number(month, months)
                if month_number and valid_date(month_number, day, year):
                    print(f"{year:04}-{month_number:02}-{day:02}")
                    break
                else:
                    continue
            except (ValueError, IndexError):
                continue

        else:
            continue


def get_month_number(month_name, months):
    if month_name in months:
        return months.index(month_name) + 1
    else:
        return None


def valid_date(month, day, year):
    if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year:
        return True
    else:
        return False


main()
