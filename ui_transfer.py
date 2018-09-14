# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '网易云音乐.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING!  All changes made in this file will be lost!
import sys,re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from pyQT.ncmdump import *


class Ui_music_change(object):
    def setupUi(self, music_change):
        self.filelist = list()
        self.music_change = music_change
        music_change.setObjectName("music_change")
        music_change.resize(384, 275)
        self.buttonBox = QtWidgets.QDialogButtonBox(music_change)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listView = QtWidgets.QTextBrowser(music_change)
        self.listView.setGeometry(QtCore.QRect(20, 60, 351, 181))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(music_change)
        self.pushButton.setGeometry(QtCore.QRect(295, 29, 75, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openFile)
        self.label = QtWidgets.QLabel(music_change)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(music_change)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 261, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(music_change)
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.clearAll)

        QtCore.QMetaObject.connectSlotsByName(music_change)


    def ok(self):
        self.listView.append("正在转化文件，请稍等")
        self.start_trasnsfer()

    def start_trasnsfer(self):
        for i in range(0,len(self.filelist)):
            self.listView.append("正在转化 --- "+ self.filelist[i])
            mp3file,imgfile = dump(self.filename+"\\"+self.filelist[i])
            self.listView.append("已生成 --- "+mp3file)
            self.listView.append("已生成 --- "+imgfile)
        self.listView.append("转化完成")


    def openFile(self):
        self.filename = QFileDialog.getExistingDirectory(self.music_change)
        # self.fname = QFileDialog.getOpenFileName(self.music_change, 'Open file')
        if self.filename:
            # f = open(self.fname[0], 'r')
            # with f:
            #     data = f.read()
            self.lineEdit.setText(self.filename)
        for (root, dirs, files) in os.walk(self.filename):
            for file in files:
                if re.match(".*\.ncm$",str(file)) is not None:
                    self.filelist.append(file)
                    self.listView.append("已添加文件 --- " + file)

    def clearAll(self):
        self.lineEdit.clear()
        self.listView.clear()

    def retranslateUi(self, music_change):
        _translate = QtCore.QCoreApplication.translate
        music_change.setWindowTitle(_translate("music_change", "网易云音乐转换工具"))
        self.pushButton.setText(_translate("music_change", "选择文件夹"))
        self.pushButton.setToolTip("请选择所转换的文件夹目录")
        self.label.setText(_translate("music_change", "请选择要转换的文件所在目录"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_music_change()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
