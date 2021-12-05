import os
import sys
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QLabel,
                             QLineEdit,
                             QPushButton,
                             QShortcut,
                             QFileSystemModel,
                             QTreeView,
                             QWidget,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLayout,
                             QMenu,
                             QPlainTextEdit,
                             QSizePolicy,
                             QMessageBox,
                             QAbstractItemView)
from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QKeySequence

class FSView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(size.width()*1/4, size.height()*0.85)

        self.model = QFileSystemModel()
        self.model.setRootPath('')

        self.model.setReadOnly(False)
        self.tree = QTreeView()
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.openMenu)
        self.tree.setModel(self.model)

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setDragDropMode(QAbstractItemView.InternalMove)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)

    def openMenu(self, position):
        menu = QMenu()
        menu.addAction('New folder', self.NewF)
        menu.exec_(self.tree.viewport().mapToGlobal(position))

    def NewF(self):
        d = str(self.model.filePath(self.tree.currentIndex())) + '/New folder'
        if not os.path.exists(d):
            os.mkdir(d)
#        correctIndex = self.tree.currentIndex() + 1 #not working
#        self.tree.edit(correctIndex)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()

    ex = FSView()
    ex.show()
    sys.exit(app.exec_())