import cv2 as cv
import numpy
import timeit
from services.cpu_gpu import cpu, gpu


def process_image(image: str, model):
    img = numpy.fromstring(image, numpy.uint8)
    img = cv.imdecode(img, cv.IMREAD_UNCHANGED)
    img_resize_1028 = cv.resize(img, (1028, 1028))
    img_rgb = cv.cvtColor(img_resize_1028, cv.COLOR_BGR2RGB)

    cpu(img_rgb, model)
    gpu(img_rgb, model)

    cpu_time = timeit.timeit('lambda: cpu(img_rgb,model)', number=10, setup="from services.cpu_gpu import cpu")
    gpu_time = timeit.timeit('lambda: gpu(img_rgb,model)', number=10, setup="from services.cpu_gpu import gpu")
    return [[cpu(img_rgb, model), cpu_time], [gpu(img_rgb, model), gpu_time], img_resize_1028]


def person_bool(classes):
    is_person = classes.numpy().astype('int')[0]
    is_person[is_person > 1] = False
    return is_person


def person_detection(detection_score: list):
    boxes, scores, classes, num_detections = detection_score[0], detection_score[1], detection_score[2], detection_score[3]
    boxes = boxes.numpy()[0].astype('int')
    scores = scores.numpy()[0]
    classes = person_bool(classes)

    if len(boxes) == len(scores) == len(classes):
        detection_pack = zip(boxes, scores, classes)
        return detection_pack

    else:
        return "Incorrect len of [boxes, scores, classes]"


def show_detected_people(upload_dir: list, image: str, model) -> list:
    info_list = []
    image_data = process_image(image, model)
    for i in range(2):
        detection_pack = person_detection(image_data[i][0])
        time = image_data[i][1]
        counter = 0
        image = image_data[2]
        for (a, b, c, d), score, person in detection_pack:
            if score < 0.22 or person != 1:
                continue

            image = cv.rectangle(image, (b, c), (d, a), (0, 255, 0), 5)
            counter += 1

        image = cv.resize(image, (512, 512))
        cv.imwrite(upload_dir[i], image)

        if i == 0:
            info_list.append(['CPU', counter, time])
        else:
            info_list.append(['GPU', counter, time])
    return info_list
