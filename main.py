import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import tensorflow_hub as hub
from person_detection import show_detected_people
from classes.Images import Images
import flask

#UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MODEL = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_PATH')


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/person_detection', methods=['GET', 'POST'])
def person_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({
                'message': 'No file part'
            })

        files = request.files.getlist('file')
        ip_addr = request.remote_addr
        list_of_files = []

        for file in files:
            if file.filename == '':
                return jsonify({
                    'message': 'No selected file'
                })

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], ip_addr)
                if not os.path.exists(path):
                    os.mkdir(path)
                image_path = os.path.join(path, filename)
                counter = show_detected_people(image_path, file.read(), MODEL)
                img_obj = Images(image_path, counter)
                list_of_files.append(img_obj.__dict__)

        return jsonify(list_of_files)

    return jsonify({
        'message': 'Send method need to be POST.'
    })


@app.route('/person_detection/manual', methods=['GET', 'POST'])
def manual():
    if request.method == 'POST':
        data = person_detection()
        paths = []
        number_of_people = []
        for obj_json in data.json:
            paths.append(os.path.join('..', obj_json['image']))
            number_of_people.append(obj_json['num_of_people'])
        return render_template('index.html', images_wih_numbers=zip(paths, number_of_people))

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
