from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
import numpy as np
import facenet
import os
import math
import pickle
from sklearn.svm import SVC
import sys
        

class training:
    def __init__(self, modeldir, scale_reshape_img):
        #self.datadir = datadir
        self.modeldir = modeldir
        self.scale_reshape_img = scale_reshape_img
  
        #self.classifier_filename = classifier_filename

    def main_train(self):
        with tf.Graph().as_default():
            with tf.Session() as sess:
                #img_data = facenet.get_dataset_all(self.datadir)
                #path, label = facenet.get_image_paths_and_labels(img_data)
                #print('Classes: %d' % len(img_data))
                image = self.scale_reshape_img

                facenet.load_model(self.modeldir)
                images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
                embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
                phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
                embedding_size = embeddings.get_shape()[1]

                print('Extracting features of images for model')
                
                image_size = 182
                emb_array = np.zeros((1, embedding_size))
                
                #image = np.expand_dims(image,axis=0)
                
                feed_dict = {images_placeholder: image, phase_train_placeholder: False}
                emb_array[0, : ] = sess.run(embeddings, feed_dict=feed_dict)
                
                
        return emb_array

