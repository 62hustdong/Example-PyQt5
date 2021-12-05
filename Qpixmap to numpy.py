import numpy as np
import cv2
import matplotlib.pyplot as plt

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#
# def QPixmapToArray(pixmap):
#     ## Get the size of the current pixmap
#     size = pixmap.size()
#     h = size.width()
#     w = size.height()
#
#     ## Get the QImage Item and convert it to a byte string
#     qimg = pixmap.toImage()
#     byte_str = qimg.bits().tobytes()
#
#     ## Using the np.frombuffer function to convert the byte string into an np array
#     img = np.frombuffer(byte_str, dtype=np.uint8).reshape((w, h, 4))
#
#     return img


def np2qpixmap(np_img):
    frame = cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB)
    img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
    return QPixmap.fromImage(img)

# image = QImage("K://PROJECT//QT//QT_APP_1//APP//Project//picture//anh_tb.png")
# display_image = QPixmap.fromImage(image)

img = cv2.imread("K://PROJECT//QT//QT_APP_1//APP//Project//picture//anh_tb.png")

# img = QPixmapToArray(display_image)
# print(img)
# print(image)
# print(display_image)
cv2.imshow("Anh", img)
cv2.waitKey()