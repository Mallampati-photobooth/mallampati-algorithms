#!/usr/bin/env python

import os
from skimage import io, exposure
from skimage.filter import threshold_otsu
from skimage.transform import pyramid_gaussian
import numpy as np

def preprocess(imgpath, UPLOAD_FOLDER, filename):
    '''
    Takes an image name or url path as input, and returns a preprocessed
    array of 0 & 1 suitable for the mallampati score detection algorithm.
    '''       
    io.use_plugin('pil')    
    
    # read & convert to grayscale
    image = io.imread(imgpath, as_grey = True)

    # Histogram equalization
    image = exposure.equalize_adapthist(image, clip_limit = 0.03)

    # Invert colors
    #image = np.invert(image)
    
    # Binarization
    thresh = threshold_otsu(image)
    image = image > thresh

    # build image pyramid
    rows, cols = image.shape
    pyramid = tuple(pyramid_gaussian(image, downscale=2))
    composite_image = np.zeros((rows, cols + cols / 2), dtype=np.double)
    composite_image[:rows, :cols] = pyramid[0]
    i_row = 0
    for p in pyramid[1:]:
        n_rows, n_cols = p.shape
        try:
            composite_image[i_row:i_row + n_rows, cols:cols + n_cols] = p
            i_row += n_rows
        except:
            continue

    # save to disk
    np.save(os.path.join(UPLOAD_FOLDER, filename.rsplit('.', 1)[0]),
            composite_image.astype(int))
    
    # debug
    #print(image.astype(int))
    #print(color.shape)
    #return composite_image    
    
if __name__ == '__main__':
    img = preprocess('./source_test_images/mallampati.jpg',
                     './source_test_images',
                     'mallampati.jpg')
