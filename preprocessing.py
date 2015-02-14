#!/usr/bin/env python

import os
from skimage import io, exposure

def preprocess(imgpath, UPLOAD_FOLDER, filename):
    '''
    Takes an image name or url path as input, and returns a preprocessed
    image suitable for the mallampati score detection algorithm to work on.
    '''       
    # read & convert to grayscale
    image = io.imread(imgpath, as_grey = True)
    #image = color.rgb2gray(image)
    
    # Adaptive Equalization
    image = exposure.equalize_hist(image)
    
    # save to disk
    io.imsave(os.path.join(UPLOAD_FOLDER, "gray_" + filename), image)
    
if __name__ == '__main__':
    img = preprocess('./source_test_images/example.jpg')
    io.imshow(img)
    io.show()
