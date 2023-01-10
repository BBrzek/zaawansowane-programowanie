import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import tensorflow_hub as hub
from person_detection import show_detected_people
from services.Images import Images
import tensorflow as tf

print(tf.test.gpu_device_name())
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
    print(
        '\n\nThis error most likely means that this notebook is not '
        'configured to use a GPU.  .\n\n')
    raise SystemError('GPU device not found')

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
                path_cpu = os.path.join(app.config['UPLOAD_FOLDER'], ip_addr, 'CPU')
                path_gpu = os.path.join(app.config['UPLOAD_FOLDER'], ip_addr, 'GPU')
                if not os.path.exists(path_cpu):
                    os.mkdir(path_cpu)
                if not os.path.exists(path_gpu):
                    os.mkdir(path_gpu)
                image_path_cpu = os.path.join(path_cpu, filename)
                image_path_gpu = os.path.join(path_gpu, filename)
                image_paths = [image_path_cpu, image_path_gpu]

                detected_people_cpu_gpu = show_detected_people(image_paths, file.read(), MODEL)
                for i in range(2):
                    img_obj = Images(detected_people_cpu_gpu[i][0], image_paths[i], detected_people_cpu_gpu[i][1], detected_people_cpu_gpu[i][2])
                    list_of_files.append(img_obj.__dict__)

        return jsonify(list_of_files)

    return jsonify({
        'message': 'Send method need to be POST.'
    })


@app.route('/person_detection/manual', methods=['GET', 'POST'])
def manual():
    if request.method == 'POST':
        data = person_detection()
        process = []
        paths = []
        number_of_people = []
        time = []

        for obj_json in data.json:
            process.append(obj_json['process_type'])
            paths.append(os.path.join('..', obj_json['image']))
            number_of_people.append(obj_json['num_of_people'])
            time.append(obj_json['time'])

        compare_list = []
        for i in range(len(paths)):
            if i % 2 == 1:
                compare_list.append(round(time[i-1] / time[i], 3))

            else:
                compare_list.append(None)

        return render_template('index.html', images_wih_numbers=zip(process, paths, number_of_people, time), count_of_images=int(len(paths)/2), compare=compare_list)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
