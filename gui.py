# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys, re, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ncmdump import *
import threading
from queue import Queue


class Ui_music_change(object):
    def setupUi(self, music_change):
        self.filelist = list()
        self.flag = True
        self.music_change = music_change
        self.queue = Queue()
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
        self.listView = QtWidgets.QTextBrowser(self.layoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(music_change)

        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.clearAll)
        QtCore.QMetaObject.connectSlotsByName(music_change)

    def ok(self):
        if self.filelist is not None and len(self.filelist) > 0:
            if self.flag:
                self.listView.append("正在转化文件，请稍等")

                self.flag = False
                self.start_trasnsfer()
                reply = QMessageBox.question(self.music_change, 'Message',
                                             "确定退出?",
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    sys.exit()
                else:
                    self.clearAll()


            else:
                self.qmessagebox = QMessageBox.information(self.music_change, "提示",
                                                           "正在转化文件，请稍等")
        else:
            self.qmessagebox = QMessageBox.information(self.music_change, "提示",
                                                       "没有文件")

    def start_trasnsfer(self):
        Thread_list = []
        for i in range(0, len(self.filelist)):
            thread = ncm_dump(self.filename, self.filelist[i], self.savefile, self.queue)
            thread.start()
            # mp3file, imgfile
            Thread_list.append(thread)
            # self.listView.append("已生成 --- " + mp3file)
            # self.listView.append("已生成 --- " + imgfile)
        while not self.queue.empty():
            self.listView.append(self.queue.get())
            # self.queue.task_done()  # 告诉队列任务完成以解除阻塞
        for i in Thread_list:
            i.join()

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
                if re.match(".*\.ncm$", str(file)) is not None:
                    self.filelist.append(file)
                    self.listView.append("已添加文件 --- " + file)

    def saveFile(self):
        self.savefile = QFileDialog.getExistingDirectory(self.music_change)
        if self.savefile:
            self.lineEdit_2.setText(self.savefile)

    def clearAll(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.listView.clear()
        self.filelist.clear()
        self.savefile = None
        self.filename = None

    def retranslateUi(self, music_change):
        _translate = QtCore.QCoreApplication.translate
        music_change.setWindowTitle(_translate("music_change", "Dialog"))
        self.label.setText(_translate("music_change", "请选择ncm文件所在的文件夹"))
        self.pushButton_2.setText(_translate("music_change", "选择文件夹"))
        self.pushButton_2.clicked.connect(self.openFile)
        self.label_2.setText(_translate("music_change", "请选择生成的MP3和jpg所在目录"))
        self.pushButton_3.setText(_translate("music_change", "选择文件夹"))
        self.pushButton_3.clicked.connect(self.saveFile)
