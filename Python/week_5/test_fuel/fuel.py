def main():
    # prompt for input and make sure fraction is good
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

# Convert fraction to percent
def convert(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return round((x / y) * 100)

# Determine fuel based on percent
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
