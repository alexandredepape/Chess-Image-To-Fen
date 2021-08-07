import unittest

from PIL import Image

from src.image2fen import Image2Fen


class MyTestCase(unittest.TestCase):
    def test_get_fen(self):
        image_filename = 'img.png'
        Image2Fen.get_fen(image_filename)


if __name__ == '__main__':
    unittest.main()
