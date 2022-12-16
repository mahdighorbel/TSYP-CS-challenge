import torch
import cv2
from PIL import Image
import urllib.request

# model loading


model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path="yolov5/runs/train/exp/weights/best.pt",
                       force_reload=False, trust_repo=True)


def detect_crater(img):
    """
    Applies model on input image
    :param img:
    :return:
    """
    return model(img)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_path = 'Demo_Images/mars_craters.jpg'
    image = Image.open(image_path)
    image.show()
    results = detect_crater(image)
    results.print()
    print(results.pandas().xyxy[0])
    results.show()
