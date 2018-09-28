# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_music_change(object):
    def setupUi(self, music_change):
        music_change.setObjectName("music_change")
        music_change.resize(379, 345)
        self.layoutWidget = QtWidgets.QWidget(music_change)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 317))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(168, 0))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.listView = QtWidgets.QListView(self.layoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(music_change)
        self.buttonBox.accepted.connect(music_change.accept)
        self.buttonBox.rejected.connect(music_change.reject)
        QtCore.QMetaObject.connectSlotsByName(music_change)

    def retranslateUi(self, music_change):
        _translate = QtCore.QCoreApplication.translate
        music_change.setWindowTitle(_translate("music_change", "Dialog"))
        self.label.setText(_translate("music_change", "请选择ncm文件所在的文件夹"))
        self.pushButton_2.setText(_translate("music_change", "选择文件夹"))
        self.label_2.setText(_translate("music_change", "请选择生成的MP3和jpg所在目录"))
        self.pushButton_3.setText(_translate("music_change", "选择文件夹"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()

    ui = Ui_music_change()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
