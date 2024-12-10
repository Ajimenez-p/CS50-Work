def main():
    time = input('What time is it? ').strip()
    time_as_float = convert(time)
    if 7 <= time_as_float <= 8:
        print('breakfast time')
    if 12 <= time_as_float <= 13:
        print('lunch time')
    if 18 <= time_as_float <= 19:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(':')
    time = float(hours) + ((float(minutes)) / 60)
    return time

if __name__ == "__main__":
    main()
