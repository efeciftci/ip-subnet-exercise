#!/usr/bin/python3

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
from random import randint


class MyDialog(QMainWindow):
    correctAnswers = 0
    tmpsubnet = [[0, 0], [128, 0], [192, 0], [224, 0], [240, 0], [248, 0],
                 [252, 0], [254, 0], [255, 0], [255, 128], [255, 192],
                 [255, 224], [255, 240]]
    tmpsubnet2 = [[255, 255], [127, 255], [63, 255], [31, 255], [15, 255],
                  [7, 255], [3, 255], [1, 255], [0, 255], [0, 127], [0, 63],
                  [0, 31], [0, 15]]

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.check)
        self.generate()

    def generate(self):
        self.flag = 0
        self.ip = [randint(0, 255) for _ in range(4)]
        self.tmp = randint(0, 12)
        self.subnet = [255, 255, *self.tmpsubnet[self.tmp]]
        self.ui.label_ip.setText(".".join(map(str, self.ip)))
        self.ui.label_mask.setText(".".join(map(str, self.subnet)))
        self.ui.lineEdit_network.clear()
        self.ui.lineEdit_network.setFocus()
        self.ui.lineEdit_bcast.clear()

    def check(self):
        ansNetwork = [ip & subnet for ip, subnet in zip(self.ip, self.subnet)]
        ansBcast = [self.ip[0], self.ip[1], self.ip[2] | self.tmpsubnet2[self.tmp][0], self.ip[3] | self.tmpsubnet2[self.tmp][1]]

        usrNetwork = [int(n) if n.isdigit() else 0 for n in self.ui.lineEdit_network.text().split(".")]
        if usrNetwork == ansNetwork:
            self.flag += 1
        else:
            self.ui.textEdit_log.append(f"Network address is incorrect! The answer is {'.'.join(map(str, ansNetwork))}")

        usrBcast = [int(n) if n.isdigit() else 0 for n in self.ui.lineEdit_bcast.text().split(".")]
        if usrBcast == ansBcast:
            self.flag += 1
        else:
            self.ui.textEdit_log.append(f"Broadcast address is incorrect! The answer is {'.'.join(map(str, ansBcast))}")

        if self.flag == 2:
            self.correctAnswers += 1

        self.ui.textEdit_log.append(f"You have {self.correctAnswers} correct answers.")

        self.generate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec())
