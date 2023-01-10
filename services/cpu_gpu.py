import tensorflow as tf


def cpu(image_rgb, model):
    with tf.device('/cpu:0'):
        img_tf = tf.convert_to_tensor(image_rgb, dtype=tf.uint8)
        img_tf = tf.expand_dims(img_tf, 0)
        boxes, scores, classes, num_detections = model(img_tf)
        return [boxes, scores, classes, num_detections]


def gpu(image_rgb, model):
    with tf.device('/device:GPU:0'):
        img_tf = tf.convert_to_tensor(image_rgb, dtype=tf.uint8)
        img_tf = tf.expand_dims(img_tf, 0)
        boxes, scores, classes, num_detections = model(img_tf)
        return [boxes, scores, classes, num_detections]