# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING!  All changes made in this file will be lost!
import sys,re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ncmdump import *
from gui import *
from queue import Queue

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    queue  = Queue()
    ui = Ui_music_change()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

