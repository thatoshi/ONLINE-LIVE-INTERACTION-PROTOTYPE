#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import cv2
import webbrowser

def ReadCamera():

    ret = False

    # parse options
    parser = argparse.ArgumentParser(description='X')
    parser.add_argument('-m', '--model', default='./model/x_model.h5')
    parser.add_argument('-l', '--labels', default='./model/x_labels.txt')
    parser.add_argument('-v', '--video')
 
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
            preds = model_pred.predict(X)

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
                    ret = True
                    break

            # Put label
            cv2.putText(capture, pred_label, (10, 100),
                  cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

            #cv2.imshow('tf-pi inspector', img_org)
            cv2.imshow('ONLINE-LIVE-INTERACTION-PROTOTYPE', capture)
            count = 0

    cam.release()
    cv2.destroyAllWindows()
    return ret

if __name__ == '__main__':
    ret = ReadCamera()
    if ret == True:
        print('Launching Browser')
        parser = argparse.ArgumentParser(description='X')
        parser.add_argument('-m', '--model', default='./model/x_model.h5')
        parser.add_argument('-l', '--labels', default='./model/x_labels.txt')
        parser.add_argument('-v', '--video')
        args = parser.parse_args()
        print(args.video)
        webbrowser.open_new(args.video)
    else:
        print('Nothing to do')
