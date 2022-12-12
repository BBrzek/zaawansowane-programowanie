import cv2 as cv
import tensorflow as tf
import numpy


def process_image(image: str):
    img = numpy.fromstring(image, numpy.uint8)
    img = cv.imdecode(img, cv.IMREAD_UNCHANGED)

    img_dimensions = img.shape

    img_resize_1028 = cv.resize(img, (1028, 1028))
    img_rgb = cv.cvtColor(img_resize_1028, cv.COLOR_BGR2RGB)
    img_tf = tf.convert_to_tensor(img_rgb, dtype=tf.uint8)
    return tf.expand_dims(img_tf, 0), img_resize_1028, img_dimensions


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
        return "Incorrect len of [boxes, scores, classes]"


def show_detected_people(upload_dir: str, image: str, model):
    image_tf, image_resized, img_dimensions = process_image(image)
    detection_pack = person_detection(model, image_tf)
    counter = 0
    for (a, b, c, d), score, person in detection_pack:
        if score < 0.22 or person != 1:
            continue

        image_resized = cv.rectangle(image_resized, (b, c), (d, a), (0, 255, 0), 5)
        counter += 1

    image = cv.resize(image_resized, (img_dimensions[1], img_dimensions[0]))
    cv.imwrite(upload_dir, image)
    return counter
