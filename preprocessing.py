#!/usr/bin/env python

import os
from skimage import io, exposure
from skimage.transform import pyramid_gaussian
import numpy as np

def preprocess(imgpath, UPLOAD_FOLDER, filename):
    '''
    Takes an image name or url path as input, and returns a preprocessed
    image suitable for the mallampati score detection algorithm to work on.
    '''       
    io.use_plugin('pil')    
    
    # read & convert to grayscale
    image = io.imread(imgpath, as_grey = True)
    
    # Histogram equalization
    image = exposure.equalize_adapthist(image, clip_limit = 0.03)

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
            #cols += n_cols
        except:
            continue
        
    # save to disk
    io.imsave(os.path.join(UPLOAD_FOLDER, "gray_" + filename), composite_image)
    
    # debug
    #return composite_image    
    
if __name__ == '__main__':
    img = preprocess('./source_test_images/mallampati.jpg',
                     './source_test_images',
                     'mallampati.jpg')
    io.imshow(img)
    io.show()
    