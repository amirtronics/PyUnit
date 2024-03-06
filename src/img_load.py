import cv2

class ImageNotFoundError(Exception):
    pass

class ImageSizeError(Exception):
    pass

class ImgLoader():
    def __init__(self):
        self.image = None

    def load(self, path):
        self.image = cv2.imread(path)
        if self.image is None:
            raise ImageNotFoundError(f"Image not found at path: {path}")
        elif self.image.shape[0] != 512:
            raise ImageSizeError(f"Incompatible image size: {self.image.shape[0]}x{self.image.shape[1]}")
        return self.image

img_loader = ImgLoader()


try:
    img_loader.load("/home/accurpress/Documents/Codes/Python/Detection_Thickness/archive/Data/repo/resized/images/img24_36.jpg")
    # Process the image if successfully loaded
except Exception as e:
    print(f"Error: {e}")