import unittest
from src.img_load import *

class TestImgLoader(unittest.TestCase):
    def setUp(self):
        self.img_loader = ImgLoader()

    def test_load_image_success(self):
        self.assertIn("error", "error in this")


if __name__ == "__main__":
    unittest.main()