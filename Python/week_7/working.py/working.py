import re
import sys

def main():
    print(convert(input('Hours: ')))

def convert(s):
    
    pattern = r'^(1[0-2]|0?[1-9])(:([0-5][0-9]))? (AM|PM) to (1[0-2]|0?[1-9])(:([0-5][0-9]))? (AM|PM)$'
    match = re.match(pattern, s, re.IGNORECASE)
    if not match:
        raise ValueError('Invalid time format')

    start_hour, _, start_minute, start_period, end_hour, _, end_minute, end_period = match.groups()


    start_minute = start_minute or '00'
    end_minute = end_minute or '00'

    start_hour = int(start_hour)
    end_hour = int(end_hour)

    if start_period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    elif start_period.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    if end_period.upper() == 'PM' and end_hour != 12:
        end_hour += 12
    elif end_period.upper() == 'AM' and end_hour == 12:
        end_hour = 0

    start_time_24 = f'{start_hour:02}:{start_minute}'
    end_time_24 = f'{end_hour:02}:{end_minute}'

    return f'{start_time_24} to {end_time_24}'

if __name__ == "__main__":
    main()
