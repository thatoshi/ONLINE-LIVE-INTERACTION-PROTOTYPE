#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import cv2
import time
#import webbrowser

if __name__ == '__main__':
    # parse options
    parser = argparse.ArgumentParser(description='tf-pi.')
    parser.add_argument('-m', '--model', default='./my_model_aug.h5')
    parser.add_argument('-l', '--labels', default='./labels.txt')

    args = parser.parse_args()

    labels = []
    with open(args.labels, 'r') as f:
        for line in f:
            labels.append(line.rstrip())
    print(labels)

    print('before')
 
    model_pred = tf.keras.models.load_model(args.model)
    # model_pred.summary()

    print('after')

    cam = cv2.VideoCapture(0)

    max_count = 0
    count = 0
    xCounter = 0
    while True:
        ret, capture = cam.read()
        if not ret:
            print('error')
            break
        
        key = cv2.waitKey(1)
        if key == 27:  # when ESC key is pressed break
            break

        count += 1
        if count > max_count:
            X = []
            img = capture.copy()
            img = cv2.resize(img, (64, 64))
            img = img_to_array(img)
            X.append(img)
            X = np.asarray(X)
            X = X/255.0
            start = time.time()
            preds = model_pred.predict(X)
            elapsed_time = time.time() - start

            pred_label = ''

            label_num = 0
            tmp_max_pred = 0
            print(preds)
            for i in preds[0]:
                if i > tmp_max_pred:
                    pred_label = labels[label_num]
                    tmp_max_pred = i
                label_num += 1

            if pred_label == "x":
                xCounter +=1
                if xCounter > 5:
                    break

            # Put speed
            speed_info = '%s: %f' % ('speed=', elapsed_time)
            # print(speed_info)
            cv2.putText(capture, speed_info, (10, 50),
                  cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

            # Put label
            cv2.putText(capture, pred_label, (10, 100),
                  cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

            #cv2.imshow('tf-pi inspector', img_org)
            cv2.imshow('ONLINE-LIVE-INTERACTION-PROTOTYPE', capture)
            count = 0

    cam.release()
    cv2.destroyAllWindows()

    #webbrowser.open_new("https://www.youtube.com/embed/dcpQYafcvCg?autoplay=1")
