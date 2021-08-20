# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys

from PyQt6.QtCore import QDir, Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton
from PyQt6 import QtGui
from pathlib import Path


class Cloud(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.InputPath = str(Path.home())

        self.inputBtn = QPushButton('📂  输入原始数据', self)
        self.inputBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inputBtn.setToolTip(self.InputPath)
        self.inputBtn.clicked.connect(self.setInputPath)
        self.inputBtn.resize(self.inputBtn.sizeHint())
        self.inputBtn.move(10, 10)

        self.resize(350, 250)
        self.center()
        self.setWindowIcon(QtGui.QIcon("UnionPay.png"))
        self.setWindowTitle('慧图示例')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setInputPath(self):
        # update the output path
        fname = QFileDialog.getOpenFileName(self, 'Open file', self.InputPath)
        # getExistingDirectory(self, "选择原始图数据"))
        if fname[0]:
            with open(fname[0], 'r'):
                pass
            # update tooltip
            self.inputBtn.setToolTip(self.InputPath)


def main():
    app = QApplication(sys.argv)
    ex = Cloud()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()