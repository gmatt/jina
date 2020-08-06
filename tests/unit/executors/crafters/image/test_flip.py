from jina.executors.crafters.image.flip import ImageHorizontalFlipper
from jina.executors.crafters.image.flip import ImageVerticalFlipper
from tests.unit.executors.crafters.image import JinaImageTestCase

import numpy as np


class ImageHorizontalFlipperTestCase(JinaImageTestCase):
    def test_horizontal_flip(self):
        img_size = 217
        crafter = ImageHorizontalFlipper()
        # generates a random image array of size (217, 217)
        img_array = self.create_random_img_array(img_size, img_size)
        crafted_chunk = crafter.craft(img_array)
        # image flips along the second axis (horizontal flip)
        flip_img_array = np.fliplr(img_array)
        # assert flipped image using numpy's fliplr method
        np.testing.assert_equal(crafted_chunk['blob'], flip_img_array)


class ImageVerticalFlipperTestCase(JinaImageTestCase):
    def test_vertical_flip(self):
        img_size = 217
        crafter = ImageVerticalFlipper(vertical=True)
        # generates a random image array of size (217, 217)
        img_array = self.create_random_img_array(img_size, img_size)
        crafted_chunk = crafter.craft(img_array)
        # image flips along the first axis (vertical flip)
        flip_img_array = np.flipud(img_array)
        # assert flipped image using numpy's flipud method
        np.testing.assert_equal(crafted_chunk['blob'], flip_img_array)
