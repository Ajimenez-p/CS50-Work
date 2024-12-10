import pyfiglet
import sys
import random

def main():
    if len(sys.argv) == 1:
        font = random.choice(pyfiglet.FigletFont.getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font = sys.argv[2]
        if font not in pyfiglet.FigletFont.getFonts():
            sys.exit(f'{font} not found')
    else:
        sys.exit('Too many args')

    i = input('Input: ')
    figlet = pyfiglet.Figlet(font=font)
    output = figlet.renderText(i)

    print(output)

if __name__ == "__main__":
    main()
