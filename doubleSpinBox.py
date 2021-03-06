import sys
from decimal import Decimal, ROUND_HALF_UP
from PyQt5 import QtCore, QtGui, QtWidgets


class DoublespinboxAndSlider(QtWidgets.QWidget):
    def __init__(self, parent, minimum=0, maximum=100, step=1):
        super(DoublespinboxAndSlider, self).__init__(parent)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)

        self.label = QtWidgets.QLabel('Label', self)
        self.label.setSizePolicy(size_policy)

        self.double_spinbox = QtWidgets.QDoubleSpinBox(self)
        self.double_spinbox.setSizePolicy(size_policy)

        self.slider = QtWidgets.QSlider(self)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setSizePolicy(size_policy)

        self.double_spinbox.valueChanged.connect(self.double_spinbox_changed)
        self.slider.valueChanged.connect(self.slider_changed)

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addWidget(self.double_spinbox)
        self.vertical_layout.addWidget(self.slider)

        self.set_single_step(step)
        self.slider.setMinimum(0)
        self.set_minimum(minimum)
        self.set_maximum(maximum)

    def set_maximum(self, value):
        self.double_spinbox.setMaximum(value)
        self.set_slider_maximum()

    def set_minimum(self, value):
        self.double_spinbox.setMinimum(value)
        self.set_slider_maximum()

    def set_single_step(self, value):
        self.double_spinbox.setSingleStep(value)
        self.double_spinbox.setDecimals(len(str(value).split('.')[-1]))
        self.set_slider_maximum()

    def set_slider_maximum(self):
        double_spinbox_range = self.double_spinbox.maximum() - self.double_spinbox.minimum()
        slider_max = double_spinbox_range / self.double_spinbox.singleStep()
        self.slider.setMaximum(int(slider_max))

    def slider_changed(self, value):
        value2 = self.round2(float(value) * self.double_spinbox.singleStep())
        self.double_spinbox.setValue(value2)

    def double_spinbox_changed(self, value):
        value2 = int(self.round2(value / self.double_spinbox.singleStep()))
        self.slider.setValue(value2)

    def round2(self, value):
        dicimals = str(self.double_spinbox.singleStep() / 10.0)
        value2 = float(Decimal(str(value)).quantize(Decimal(dicimals), rounding=ROUND_HALF_UP))
        return value2


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.doublespinbox_and_slider = DoublespinboxAndSlider(self, 0, 20, 0.001)
        self.verticalLayout.addWidget(self.doublespinbox_and_slider)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow(None)
    mainwindow.show()
    app.exec()


if __name__ == '__main__':
    main()