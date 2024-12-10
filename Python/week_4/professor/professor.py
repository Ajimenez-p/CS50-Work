#prompt for a level, n. if user does not input 1, 2, or 3, prompt again

#randomly generate 10 math problems formatted as X + Y =, where X & Y > 0 w/ n digits. optional support for other operations

#prompts user to solve each problem. if answer is not correct (or not int()), output 'EEE' and prompt again, allowing up to three tries for that problem.
#if the user still hasn't answered correctly after 3 tries, output correct answer and move on

#last output = score, number of correct answers / 10

#structure needed:

import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        if solve_problem(x, y, correct_answer):
            score += 1
    print(f"Score: {score}/10")


def get_level():
    while True:
        try:
            n = int(input('Level: '))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)


def solve_problem(x, y, correct_answer):
    attempts = 0

    while attempts < 3:
        try:
            guess = int(input(f"{x} + {y} = "))
            if guess == correct_answer:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")

        attempts += 1

    print(f"The correct answer is {correct_answer}")
    return False


if __name__ == "__main__":
    main()
