#!/usr/bin/env python
# -*- coding: utf-8 -*-

import preprocessing
import unittest

class TestImagePreprocessing(unittest.TestCase):

    def test_image_is_returned(self):
        self.assertIsNotNone(preprocessing.preprocess('./source_test_images/example.jpg'))