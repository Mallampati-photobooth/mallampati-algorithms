#!/usr/bin/env python
# -*- coding: utf-8 -*-

import preprocessing
import unittest, os

class TestImagePreprocessing(unittest.TestCase):

    def test_image_is_returned(self):
        preprocessing.preprocess(
        './source_test_images/example.jpg', '../uploads', 'example.jpg')
        self.assertTrue(os.path.isfile('../uploads/gray_example.jpg'))