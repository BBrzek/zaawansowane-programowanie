import cv2 as cv
import tensorflow as tf
import numpy


def process_image(image: str):
    img = numpy.fromstring(image, numpy.uint8)
    img = cv.imdecode(img, cv.IMREAD_UNCHANGED)
    img_resize_1028 = cv.resize(img, (1028, 1028))
    img_rgb = cv.cvtColor(img_resize_1028, cv.COLOR_BGR2RGB)
    img_tf = tf.convert_to_tensor(img_rgb, dtype=tf.uint8)
    return tf.expand_dims(img_tf, 0), img_resize_1028


def person_bool(classes):
    is_person = classes.numpy().astype('int')[0]
    is_person[is_person > 1] = False
    return is_person


def person_detection(model, image_tf):

    boxes, scores, classes, num_detections = model(image_tf)

    boxes = boxes.numpy()[0].astype('int')
    scores = scores.numpy()[0]
    classes = person_bool(classes)

    if len(boxes) == len(scores) == len(classes):
        detection_pack = zip(boxes, scores, classes)
        return detection_pack
    else:
        return "Smth wrong with len. boxes, scores, classes"


def show_detected_people(upload_dir: str, image: str, model):
    image_tf, image_resized = process_image(image)
    detection_pack = person_detection(model, image_tf)
    counter = 0
    for (a, b, c, d), score, person in detection_pack:
        if score < 0.35 or person != 1:
            continue
        image_resized = cv.rectangle(image_resized, (b, c), (d, a), (0, 255, 0), 5)
        counter += 1

    cv.imwrite(upload_dir, image_resized)
    return counter




'''
import os
import cv2 as cv
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

def get_images_path(dir_path: str) -> list:
    return [f'{dir_path}/{file}' for file in os.listdir(dir_path)]

def image_processing(images: list) -> list:
    list_images_str = [cv.imread(img) for img in images]  #read img to str
    list_images_resize = [ cv.resize(img,(1028, 1028)) for img in list_images_str] #input shape
    list_images_rgb = [cv.cvtColor(img, cv.COLOR_BGR2RGB) for img in list_images_resize] #img to RGB
    list_images_tf = [tf.convert_to_tensor(img, dtype=tf.uint8) for img in list_images_rgb] #convert to uint8 max=255
    list_images_tf = [tf.expand_dims(img, 0) for img in list_images_tf]
    return list_images_tf

#def model_preparation(list_images: list):
    #detector = hub.Module("https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1")
    #list_detector_output = [detector(img, as_dict=True) for img in list_images]
    #list_class_names = [detector_output["detection_class_names"] for detector_output in list_detector_output]





    #gray_pic = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #cv2.imshow('image', str_images[0])
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

images_dir = r'./images'
list_images = get_images_path(images_dir)
list_processed_images = image_processing(list_images)
#print(len(tf.config.list_physical_devices('GPU'))) 
'''