#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage import io, exposure

def preprocess(imgfile):
    '''
    Takes an image name or url path as input, and returns a preprocessed
    image suitable for the mallampati score detection algorithm to work on.
    '''       
    # read & convert to grayscale
    image = io.imread(imgfile, as_grey = True)
    
    # Adaptive Equalization
    image = exposure.equalize_adapthist(image)
    
    return image
    
if __name__ == '__main__':
    img = preprocess('./source_test_images/example.jpg')
    io.imshow(img)
    io.show()
