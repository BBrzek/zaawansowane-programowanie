import os
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
import tensorflow_hub as hub
from person_detection import show_detected_people


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MODEL = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Images:
    def __init__(self, image: str, num_of_people):
        self.image = image
        self.num_of_people = num_of_people

    def __str__(self):
        print(f'Image: {self.image} | num of people: {self.num_of_people}')


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/person_detection/', methods=['GET', 'POST'])
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
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], ip_addr)
            if not os.path.exists(path):
                os.mkdir(path)
            image_path = os.path.join(path, filename)
            counter = show_detected_people(image_path, file.read(), MODEL)
            img_obj = Images(image_path, counter)

            return jsonify(img_obj.__dict__)

    return jsonify({
        'message': 'No file uploaded'
    })


@app.route('/person_detection/manual', methods=['GET', 'POST'])
def manual():
    if request.method == 'POST':
        data = person_detection()
        path = os.path.join('..', data.json['image'])
        return render_template('index.html', filepath=path)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
