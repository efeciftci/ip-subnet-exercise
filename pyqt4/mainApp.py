#!/usr/bin/python

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
from PyQt4 import QtCore, QtGui
from mainWindow import Ui_MainWindow
from random import randint

class MyDialog(QtGui.QMainWindow):
	correctAnswers = 0
	tmpsubnet = [[0, 0], [128, 0], [192, 0], [224, 0], [240, 0], [248, 0], [252, 0], [254, 0], [255, 0], [255, 128], [255, 192], [255, 224], [255, 240]]
	tmpsubnet2 = [[255, 255], [127, 255], [63, 255], [31, 255], [15, 255], [7, 255], [3, 255], [1, 255], [0, 255], [0, 127], [0, 63], [0, 31], [0, 15]]

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.check)
		self.generate()
	
	def generate(self):
		self.flag = 0
		self.ip = [randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255)]
		self.tmp = randint(0, 12)
		self.subnet = [255, 255, self.tmpsubnet[self.tmp][0], self.tmpsubnet[self.tmp][1]]
		self.ui.label_ip.setText("{:d}.{:d}.{:d}.{:d}".format(self.ip[0], self.ip[1], self.ip[2], self.ip[3]))
		self.ui.label_mask.setText("{:d}.{:d}.{:d}.{:d}".format(self.subnet[0], self.subnet[1], self.subnet[2], self.subnet[3]))
		self.ui.lineEdit_network.setText("")
		self.ui.lineEdit_network.setFocus()
		self.ui.lineEdit_bcast.setText("")
	
	def check(self):
		ansNetwork = [self.ip[0] & self.subnet[0], self.ip[1] & self.subnet[1], self.ip[2] & self.subnet[2], self.ip[3] & self.subnet[3]]
		ansBcast = [self.ip[0], self.ip[1], self.ip[2] | self.tmpsubnet2[self.tmp][0], self.ip[3] | self.tmpsubnet2[self.tmp][1]]
		
		try:
			usrNetwork = [int(n) for n in self.ui.lineEdit_network.text().split(".")]
		except ValueError:
			usrNetwork = [0, 0, 0, 0]
		if usrNetwork[0] == ansNetwork[0] and usrNetwork[1] == ansNetwork[1] and usrNetwork[2] == ansNetwork[2] and usrNetwork[3] == ansNetwork[3]:
			self.flag = self.flag + 1
		else:
			self.ui.textEdit_log.append("Network address is incorrect! The answer is {:d}.{:d}.{:d}.{:d}".format(ansNetwork[0], ansNetwork[1], ansNetwork[2], ansNetwork[3]))
		
		try:
			usrBcast = [int(n) for n in self.ui.lineEdit_bcast.text().split(".")]
		except ValueError:
			usrBcast = [0, 0, 0, 0]
		if usrBcast[0] == ansBcast[0] and usrBcast[1] == ansBcast[1] and usrBcast[2] == ansBcast[2] and usrBcast[3] == ansBcast[3]:
			self.flag = self.flag + 1
		else:
			self.ui.textEdit_log.append("Broadcast address is incorrect! The answer is {:d}.{:d}.{:d}.{:d}".format(self.ip[0], self.ip[1], ansBcast[2], ansBcast[3]))
		
		if self.flag == 2:
			self.correctAnswers = self.correctAnswers + 1
		
		self.ui.textEdit_log.append("You have " + str(self.correctAnswers) + " correct answers.\n")
		
		self.generate()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyDialog()
	myapp.show()
	sys.exit(app.exec_()) 
