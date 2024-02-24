import csv
from pytesseract import pytesseract
from PIL import Image

class Reader:
    def __init__(self):
        path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = path

    def extract(self, path: str, datatype: str):

        if(datatype == 'pdf'):
            img = Image.open(path)

            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(3.0)

            extractedText = pytesseract.image_to_string(img, lang='eng')

            return extractedText

        elif(datatype == 'img'):
            img = Image.open(path)

            extractedText = pytesseract.image_to_string(img, lang='eng', config='--psm 6 --oem 1 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ|')

            return extractedText


if __name__ == "__main__":
    r = Reader()
    text = r.extract("sample.png", 'img')

    lines = text.split('\n')

    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['Reference', 'Designation', 'Qty', 'Unitprice', 'TotalCHF', 'Sales', 'Work'])

        for line in lines[4:]:
            if line.strip() == '':
                continue
            words = line.split()
            if len(words) == 6:
                writer.writerow(words)
            else:
                writer.writerow([''] + words)

    print('CSV file generated successfully.')
