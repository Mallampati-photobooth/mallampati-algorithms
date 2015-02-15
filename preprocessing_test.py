#!/usr/bin/env python
# -*- coding: utf-8 -*-

import preprocessing
import unittest, os

class TestImagePreprocessing(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove('./source_test_images/gray_example.jpg')
        except:
            pass
        
    def test_image_is_returned(self):
        preprocessing.preprocess('./source_test_images/example.jpg',
                                 './source_test_images', 'example.jpg')
        self.assertTrue(os.path.isfile(
            './source_test_images/gray_example.jpg'))