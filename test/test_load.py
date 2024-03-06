import unittest
from src.img_load import *

class TestImgLoader(unittest.TestCase):
    def setUp(self):
        self.img_loader = ImgLoader()

    def test_load_image_success(self):
        path = "/home/accurpress/Documents/Codes/Python/Detection_Thickness/archive/Data/repo/resized/images/img24_36.jpg"
        image = self.img_loader.load(path)
        self.assertIsInstance(image, type(self.img_loader.image))
        self.assertEqual(image.shape[0], 512)

    # def test_load_image_not_found(self):
    #     with self.assertRaises(ImageNotFoundError) as context:
    #         self.img_loader.load("nonexistent_path.jpg")
    #     self.assertIn("Image not found at path", str(context.exception))

    def test_load_image_incompatible_size(self):
        with self.assertRaises(ImageSizeError) as context:
            self.img_loader.load("/home/accurpress/Documents/Codes/Python/Detection_Thickness/archive/Data/repo/unresized/Images/img44_58.jpg")
        self.assertIn("Incompatible image size", str(context.exception))

if __name__ == "__main__":
    unittest.main()