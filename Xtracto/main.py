import os
import fitz
from flask import Flask, render_template, jsonify, redirect, url_for, request
from utils.script import Reader

app = Flask(__name__)

@app.route('/')
def serve():
    """Home page"""
    return render_template('home.html')

@app.route('/extracted')
def show_extracted_text():
    text = request.args.get('text')
    return render_template('extracted.html', text=text)

@app.route('/api', methods=['POST'])
def extract():
    file = request.files['file']
    r = Reader()

    if file:

        # if the file is pdf, i am checking this
        if file.mimetype == 'application/pdf':
            file.save(os.path.join('./', file.filename))

            # PyMuPDF helps me to read the . 
            doc = fitz.open(os.path.join("./", file.filename))
            page = doc.load_page(0) 
            pix = page.get_pixmap()
            output = "./outfile.png"
            pix.save(output)
            doc.close()

            # extracting with pytesseract
            text = r.extract(f"./outfile.png", 'pdf')
            os.remove(os.path.join('./', file.filename))
            os.remove("./outfile.png")
            return redirect(url_for('show_extracted_text', text=text))
        else:
            file.save(os.path.join('./', file.filename))
            text = r.extract(f"./{file.filename}", 'img')
            os.remove(os.path.join('./', file.filename))
            return redirect(url_for('show_extracted_text', text=text))
    else:
        return {"msg": "No file chosen. Go back and choose a file"}
