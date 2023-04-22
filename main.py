from datetime import datetime
import os
import os.path
from tkinter import filedialog
from flask import Flask,redirect,render_template
from pdf2docx import Converter
from distutils.log import debug
from docx2pdf import convert
from datetime import datetime
from tkinter import filedialog
from tkinter import *
from PIL import Image
import PIL
import xlsxwriter
from win32com import client
# from asposecells import 

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/sign-up-in')
def signUpIn():
    return render_template('signup.html')



@app.route('/word-pdf')
def word_to_pdf():
    return render_template('browse1.html')

@app.route('/word-pdf/converter')
def word_to_pdf_converter():
    word = filedialog.askopenfilename()

    pathn = filedialog.askdirectory()
    date = datetime.now().strftime("%Y_%m_%d_%I_%M_%S")
    name = f'new_{date}'
    save_here = os.path.join(pathn, name+'.pdf')

    convert(word, save_here)
    return redirect('/')



@app.route('/pdf-word')
def pdf_to_word():
    return render_template('browse2.html')

@app.route('/pdf-word/converter')
def pdf_to_word_converter():
    pdf = filedialog.askopenfilename()

    pathn = filedialog.askdirectory()
    date = datetime.now().strftime("%Y_%m_%d_%I_%M_%S")
    name = f'new_{date}'
    save_here = os.path.join(pathn, name+'.docx')

    cv = Converter(pdf)
    cv.convert(save_here, start=0, end=None)
    cv.close()
    return redirect('/')



@app.route('/jpg-png')
def jpg_to_png():
    return render_template('browse3.html')

@app.route('/jpg-png/converter')
def jpg_to_png_converter():
    global im1
    jpg = filedialog.askopenfilename()

    if jpg.endswith(".jpg"):
        im1 = Image.open(jpg)
        pathn = filedialog.askdirectory()
        date = datetime.now().strftime("%Y_%m_%d_%I_%M_%S")
        name = f'new_{date}'
        save_here = os.path.join(pathn, name+'.png')
        im1.save(save_here)
    return redirect('/')



@app.route('/png-jpg')
def png_to_jpg():
    return render_template('browse4.html')

@app.route('/png-jpg/converter')
def png_to_jpg_converter():
    global im1
    png = filedialog.askopenfilename()

    if png.endswith(".png"):
        im1 = Image.open(png)
        pathn = filedialog.askdirectory()
        date = datetime.now().strftime("%Y_%m_%d_%I_%M_%S")
        name = f'new_{date}'
        save_here = os.path.join(pathn, name+'.jpg')
        im1.save(save_here)
    return redirect('/')



@app.route('/jpg-pdf')
def jpg_to_pdf():
    return render_template('browse5.html')

@app.route('/jpg-pdf/converter')
def jpg_to_pdf_converter():
    image_list = []

    image = filedialog.askopenfilenames()
    images = list(image)
    for img in images:
        im = PIL.Image.open(img)
        im = im.convert('RGB')
        image_list.append(im)
    
    pathn = filedialog.askdirectory()
    date = datetime.now().strftime("%Y_%m_%d_%I_%M_%S")
    name = f'new_{date}'
    save_here = os.path.join(pathn, name+'.pdf')
    image_list[0].save(save_here, save_all = True, append_images = image_list[1:])
    return redirect('/')



@app.route('/excel-pdf')
def excel_to_pdf():
    return render_template('browse6.html')

@app.route('/excel-pdf/converter')
def excel_to_pdf_converter():
    excel = filedialog.askopenfile()

    excl = client.Dispatch("Excel.Application")

    sheets = excl.Workbooks.Open(excel.name)
    work_sheets =  sheets.Worksheets[0]
    pathn = filedialog.askdirectory()
    date = datetime.now().strftime("%Y_%m_%d_%I_%M_%S")
    name = f'new_{date}'
    save_here = os.path.join(pathn, name+'.pdf')

    work_sheets.ExportAsFixedFormat(0, save_here)
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)



