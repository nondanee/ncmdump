# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'gui.ui'
# Created by: PyQt5 UI code generator 5.6
# WARNING!  All changes made in this file will be lost!
from gui import *
from queue import Queue
import threadpool

def main():

    task_pool=threadpool.ThreadPool(8)#8是线程池中线程的个数
    request_list=[]#存放任务列表
    #首先构造任务列表
    #将每个任务放到线程池中，等待线程池中线程各自读取任务，然后进行处理，使用了map函数，不了解的可以去了解一下。
    map(task_pool.putRequest,request_list)
    #等待所有 任务处理完成，则返回，如果没有处理完，则一直阻塞
    task_pool.poll()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    queue  = Queue()
    ui = Ui_music_change()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

