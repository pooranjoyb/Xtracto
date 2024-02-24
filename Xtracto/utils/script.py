from pytesseract import pytesseract
from PIL import Image, ImageEnhance
import os
import fitz

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

            extractedText = pytesseract.image_to_string(img, lang='eng', config='--psm 6 --oem 1')

            return extractedText

        else:
            return {"msg": "Only PDFs and Image files allowed"}