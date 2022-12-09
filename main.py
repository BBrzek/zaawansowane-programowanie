import os
from flask import Flask, flash, request, redirect, render_template, send_file
from werkzeug.utils import secure_filename
import cv2 as cv
from PIL import Image
import tensorflow_hub as hub
import json

#MODEL = hub.load()
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def person_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        #print(f'Pillow image{Image.open(file)}')

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            #print(type(file.read()))
            #filename = secure_filename(file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return file.read()#send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), mimetype='image/png')   #render_template("index.html", filepath=os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template("index.html")

'''
To do
-create function that load file to openCv from file storage
through numpy.
-create class with str of image from file.read() and 2nd
parametr with person counter
-return it as json

??? to do
make it possible for multiple files and add function to manually
upload files. With view redirection
'''
if __name__ == '__main__':
    app.run()
