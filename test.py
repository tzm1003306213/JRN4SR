# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:25:36 2017

@author: tang
"""

import tensorflow as tf
import argparse
import os
import cv2
import time

parser = argparse.ArgumentParser()
parser.add_argument("--LR_path")
parser.add_argument("--save_path")
parser.add_argument("--model_path")
args = parser.parse_args()
LR_path = args.LR_path
save_path = args.save_path
model_path = args.model_path

graph = model_path + '.meta'
variables = model_path

def main():

    path = LR_path
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    names = os.listdir(path)
    name_pathes = [path + names[i] for i in range(len(names)) ]

    sess = tf.Session()
    new_saver = tf.train.import_meta_graph(graph)
    new_saver.restore(sess, variables)

    ex_time = []
    for i in range(len(name_pathes)):
        im = cv2.imread(name_pathes[i], cv2.IMREAD_GRAYSCALE)
        im = im / 255.0
        im = im.reshape([1,im.shape[0],im.shape[1],1])

        start = time.clock()
        out = sess.run('output/add_1:0', feed_dict={'input/im_input:0': im})
        end = time.clock()
        ex_time.append(end - start)
        out = out * 255
        out = out.reshape([out.shape[1],out.shape[2]])
        cv2.imwrite(save_path + names[i], out)
    print('Average excutive time per image:')
    print(sum(ex_time)/len(ex_time))
#    cv2.imwrite(save_path + names[i], output, [cv2.IMWRITE_PNG_COMPRESSION, 0])
if __name__ == '__main__':
    main()

