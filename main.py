# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import os

from PyQt6.QtCore import QDir, Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QGridLayout, QTextEdit, QLineEdit
from PyQt6 import QtGui
from presentation import draw_origin, draw_influence, candidate_list


class Cloud(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.InputPath = os.getcwd()
        self.inputBtn = QPushButton('📂  输入原始数据', self)
        self.inputBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inputBtn.setToolTip(self.InputPath)
        self.inputBtn.clicked.connect(self.setInputPath)
        # self.inputBtn.resize(self.inputBtn.sizeHint())
        # self.inputBtn.move(10, 10)
        grid.addWidget(self.inputBtn, 1, 0)

        self.textChart = QTextEdit(self)
        self.textChart.setReadOnly(True)
        grid.addWidget(self.textChart, 2, 0)

        self.funBtn = QPushButton('生成示例', self)
        self.funBtn.clicked.connect(self.get_origin)
        grid.addWidget(self.funBtn, 1, 1)

        self.funBtn2 = QPushButton('影响力分析', self)
        self.funBtn2.clicked.connect(self.get_influence)
        grid.addWidget(self.funBtn2, 2, 1)

        self.textRes = QLineEdit(self)
        grid.addWidget(self.textRes, 4, 1)

        self.funBtn3 = QPushButton('反馈关键用户信息', self)
        self.funBtn3.clicked.connect(self.get_candidate)
        grid.addWidget(self.funBtn3, 4, 0)

        self.resize(800, 700)
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
            with open(fname[0], 'r', encoding='utf-8') as f:
                lines = f.readlines()
                res = ""
                for i in range(len(lines)):
                    line = lines[i].split(",")
                    res += " , ".join(line)
            self.textChart.setPlainText(res)
            # update tooltip
            self.inputBtn.setToolTip(self.InputPath)

    def get_origin(self):
        draw_origin()

    def get_influence(self):
        draw_influence()

    def get_candidate(self):
        if self.textRes.text():
            res = candidate_list(self.textRes.text())
            if res == []:
                self.textRes.setText("找不到合适的用户！")
            else:
                self.textRes.setText(",".join(res))
        else:
            self.textRes.setText("请输入正确的查询！")

def main():
    app = QApplication(sys.argv)
    ex = Cloud()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
