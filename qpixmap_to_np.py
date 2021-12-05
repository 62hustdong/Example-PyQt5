import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2


# def convert_nparray_to_QPixmap(img):
#     ## input: Anh mau RGB hoac anh xam
#     ## output: Tao mot doi tuong QPixmax de hien thi bang cach chuyen du lieu anh sang mot doi tuong QImage
#     if img.ndim == 2:
#         w, h = img.shape
#         # Convert resulting image to pixmap
#         qimg = QImage(img.data, h, w, h, QImage.Format_Grayscale8)
#         qpixmap = QPixmap(qimg)
#     if img.ndim == 3:
#         w, h, ch = img.shape
#         # Convert resulting image to pixmap
#         qimg = QImage(img.data, h, w, 3 * h, QImage.Format_RGB888).rgbSwapped()
#         qpixmap = QPixmap(qimg)
#     ### print("{0} {1} {2}".format(img.shape[0], img.shape[1], img.ndim, ))
#     return qpixmap

def convert_nparray_to_QPixmap(img):
    ## input: Anh mau RGB hoac anh xam
    ## output: Tao mot doi tuong QPixmax de hien thi bang cach chuyen du lieu anh sang mot doi tuong QImage
    ### print("{0} {1} {2}".format(img.shape[0], img.shape[1], img.ndim, ))
    if img.ndim == 2:
        w, h = img.shape
        # Convert resulting image to pixmap
        qimg = QImage(img.data, h, w, h, QImage.Format_Grayscale8)
        qpixmap = QPixmap(qimg)
        return qpixmap
    if img.ndim == 3:
        w, h, ch = img.shape
        # Convert resulting image to pixmap
        qimg = QImage(img.data, h, w, 3 * h, QImage.Format_RGB888).rgbSwapped()
        qpixmap = QPixmap(qimg)
        return qpixmap

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

if __name__ == '__main__':
    img = cv2.imread("K://PROJECT//QT//QT_APP_1//APP//Project//picture//anh_tb.png")


    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("My App")
    lay = QHBoxLayout(w)
    view = QLabel()
    # view.setPixmap(QPixmap("K://PROJECT//QT//QT_APP_1//APP//Project//picture//anh_tb.png"))
    pixmap = convert_nparray_to_QPixmap(img)

    view.setPixmap(pixmap)
    lay.addWidget(view)
    w.show()

    cv2.imshow("Anh goc", img)
    cv2.waitKey()

    sys.exit(app.exec_())
