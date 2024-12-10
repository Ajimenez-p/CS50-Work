import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        i_file = sys.argv[1]
        o_file = sys.argv[2]
        valid_extensions = ('.jpg', '.jpeg', '.png')
        if os.path.splitext(i_file)[1].lower() != os.path.splitext(o_file)[1].lower():
            sys.exit('Input and output have different extensions')
        if not os.path.isfile(i_file):
            sys.exit('Invalid input')

        try:
            input_image = Image.open(i_file)
        except Exception as e:
            sys.exit(f'Unable to open {i_file}: {e}')

        try:
            shirt_image = Image.open('shirt.png')
        except Exception as e:
            sys.exit(f'Unable to open shirt.png: {e}')

        input_image = ImageOps.fit(input_image, shirt_image.size)
        input_image.paste(shirt_image, shirt_image)

        try:
            input_image.save(o_file)
        except Exception as e:
            sys.exit(f'Unable to save {o_file}: {e}')


if __name__ == '__main__':
    main()
