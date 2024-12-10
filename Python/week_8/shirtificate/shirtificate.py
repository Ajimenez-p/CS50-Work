from fpdf import FPDF
from PIL import Image

class ShirtificatePDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 24)
        self.cell(0, 10, 'CS50 Shirtificate', align='C', ln=True)

    def add_shirt_image(self, name):
        self.image('shirtificate.png', x=10, y=40, w=190)
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", 'B', 36)
        self.text(55, 140, f"{name} took CS50")

def main():
    name = input("What's your name? ")
    pdf = ShirtificatePDF()
    pdf.add_page()
    pdf.add_shirt_image(name)
    pdf.output('shirtificate.pdf')
    print(f"done for {name}!")

if __name__ == "__main__":
    main()
