import os
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
import tensorflow_hub as hub
from base64 import b64encode
from person_detection import show_detected_people


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MODEL = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

'''
class Person_detection_image:
    def __init__(self, image: str, person_count: int, filename: str):
        self.image = image
        self.person_count = person_count
        self.filename = filename

'''


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
        ip_addr = request.remote_addr
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):

            '''filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))'''

            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], ip_addr)
            if not os.path.exists(path):
                os.mkdir(path)
            image_path = os.path.join(path, filename)
            counter = show_detected_people(image_path, file.read(), MODEL)


            return f'{counter}' #jsonify({'image': )}) #render_template("index.html", filepath=os.path.join(app.config['UPLOAD_FOLDER'], filename))#send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), mimetype='image/png')   #render_template("index.html", filepath=os.path.join(app.config['UPLOAD_FOLDER'], filename))


    return jsonify({
        'message': 'No file uploaded'
    })
'''
@app.route('/interface', methods=['GET', 'POST'])
def interface():
    data = person_detection()


To do
-create upload interface
-save file driection as lists and person
'''
if __name__ == '__main__':
    app.run()
