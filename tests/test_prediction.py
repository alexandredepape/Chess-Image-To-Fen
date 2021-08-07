import unittest

from PIL import Image

from src.prediction import PiecePredictor


class MyTestCase(unittest.TestCase):
    def test_something(self):
        image = Image.open('piece.png')
        rgb_im = image.convert('RGB')
        chess_predictor = PiecePredictor()
        print(chess_predictor.predict(rgb_im))


if __name__ == '__main__':
    unittest.main()
