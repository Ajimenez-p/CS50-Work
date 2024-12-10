def main():
    while True:
        try:
            # Grabbing the fraction
            x, y = grab_fraction()

            # Validate inputs
            if not check_if_int(x) or not check_if_int(y):
                continue  # If invalid input, prompt again

            x = int(x)  # Convert to int
            y = int(y)

            # Check if Y is zero
            if y == 0:
                continue

            # Check if X is greater than Y
            if x > y:
                continue

            # Calculate the fuel percentage
            (fuel) = (x / y) * 100

            # Output the result
            if fuel <= 1:
                print("E")
            elif fuel >= 99:
                print("F")
            else:
                print(f"{round(fuel)}%")  # Output percentage rounded to nearest integer

            break  # Exit the loop when valid input is provided
        except ZeroDivisionError:
            continue
        except ValueError:
            continue

# Function to grab the fraction input
def grab_fraction():
    fraction = input("Fraction: ")
    x, y = fraction.split('/')  # Split into X and Y
    return x, y

# Function to check if a variable is an integer
def check_if_int(v):
    try:
        int(v)
        return True
    except ValueError:
        return False

main()
