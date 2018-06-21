# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mian.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5 import QtCore as core
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
import sys
from MyIM_Client.core import main_controller


class Ui_MainWindow(object):

    def __init__(self, runMonitor):
        super().__init__()
        self.runMonitor = runMonitor
        self.mainwindow = QMainWindow()
        self.setupUi(self.mainwindow)
        self.retranslateUi(self.mainwindow)
        self.timer1 = core.QTimer()
        self.timer2 = core.QTimer()

    def show(self):
        self.mainwindow.show()
        self.timer1.timeout.connect(self.screen_show)
        self.timer1.start(1000)
        self.timer2.timeout.connect(self.flush_list)
        self.timer2.start(1000)

    def screen_show(self):
        try:
            message = main_controller.RunnerMointor.queue1.get_nowait()
            metadata = self.message_screen.toPlainText().strip()
            metadata += "\n\n" + str(message)
            self.message_screen.setPlainText(self.translate("MainWindow", metadata))
        except:
            pass

    def flush_list(self):
        try:
            message = main_controller.RunnerMointor.queue2.get_nowait()
            self.aliveList.clearContents()
            # self.online_item1.setText(self.translate("MainWindow", "在线列表"))
            # self.state_item2.setText(self.translate("MainWindow", "当前状态"))
            self.aliveList.setRowCount(len(message))
            # self.aliveList.clearContents()
            index = 0
            for row in message:
                item = QtWidgets.QTableWidgetItem()
                self.aliveList.setVerticalHeaderItem(index, item)

                item = QtWidgets.QTableWidgetItem()
                self.aliveList.setItem(index, 0, item)
                item = self.aliveList.item(index, 0)
                item.setText(self.translate("MainWindow", row))

                item = QtWidgets.QTableWidgetItem()
                self.aliveList.setItem(index, 1, item)
                item = self.aliveList.item(index, 1)
                item.setText(self.translate("MainWindow", "在线"))

                index += 1

        except:
            pass

    def send_message(self):
        data = self.input_area.toPlainText()
        self.input_area.clear()
        if data:
            self.runMonitor.test_send_message(data)

    def clear_screen(self):
        try:
            message = main_controller.RunnerMointor.queue3.get_nowait()
            if message == '1':
                self.message_screen.clear()
        except:
            pass

    def peer_to_peer_chat(self):
        conn_object = self.aliveList.selectedItems()[0].text()
        self.message_screen.clear()
        if conn_object:
            self.runMonitor.create_peer_to_peer_chat(conn_object)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 588)
        MainWindow.setMinimumSize(QtCore.QSize(804, 588))
        MainWindow.setMaximumSize(QtCore.QSize(804, 588))
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.message_screen = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.message_screen.setReadOnly(True)
        self.message_screen.setGeometry(QtCore.QRect(20, 70, 541, 361))
        self.message_screen.setObjectName("message_screen")
        self.input_area = QtWidgets.QTextEdit(self.centralwidget)
        self.input_area.setGeometry(QtCore.QRect(20, 450, 541, 91))
        self.input_area.setObjectName("input_area")
        self.aliveList = QtWidgets.QTableWidget(self.centralwidget)
        self.aliveList.setGeometry(QtCore.QRect(580, 70, 201, 471))
        self.aliveList.setObjectName("aliveList")
        self.aliveList.setColumnCount(2)
        self.aliveList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.aliveList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.aliveList.setHorizontalHeaderItem(1, item)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 761, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.store_message = QtWidgets.QCheckBox(self.widget)
        self.store_message.setObjectName("store_message")
        self.horizontalLayout.addWidget(self.store_message)
        self.roam_message = QtWidgets.QCheckBox(self.widget)
        self.roam_message.setObjectName("roam_message")
        self.horizontalLayout.addWidget(self.roam_message)
        self.queryMessage = QtWidgets.QPushButton(self.widget)
        self.queryMessage.setObjectName("queryMessage")
        self.horizontalLayout.addWidget(self.queryMessage)
        self.queryRoam = QtWidgets.QPushButton(self.widget)
        self.queryRoam.setObjectName("queryRoam")
        self.horizontalLayout.addWidget(self.queryRoam)
        self.upload_file = QtWidgets.QPushButton(self.widget)
        self.upload_file.setObjectName("upload_file")
        self.horizontalLayout.addWidget(self.upload_file)
        self.download_file = QtWidgets.QPushButton(self.widget)
        self.download_file.setObjectName("download_file")
        self.horizontalLayout.addWidget(self.download_file)
        self.logout = QtWidgets.QPushButton(self.widget)
        self.logout.setObjectName("logout")
        self.horizontalLayout.addWidget(self.logout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.send_message_bnt = QtWidgets.QPushButton(self.centralwidget)
        self.send_message_bnt.setGeometry(QtCore.QRect(490, 510, 71, 31))
        self.send_message_bnt.setObjectName("send_message")
        self.send_message_bnt.clicked.connect(self.send_message)

        # 待实现，点对点通信功能，不经过服务器转发
        # self.aliveList.cellClicked.connect(self.peer_to_peer_chat)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self.translate("MainWindow", "MainWindow"))
        # metadata = self.message_screen.getPaintContext()
        self.message_screen.setPlainText(self.translate("MainWindow", ""))

        self.online_item1 = self.aliveList.horizontalHeaderItem(0)
        self.online_item1.setText(self.translate("MainWindow", "在线列表"))
        self.state_item2 = self.aliveList.horizontalHeaderItem(1)
        self.state_item2.setText(self.translate("MainWindow", "当前状态"))

        self.store_message.setText(self.translate("MainWindow", "开启消息存储"))
        self.roam_message.setText(self.translate("MainWindow", "开启消息漫游"))
        self.queryMessage.setText(self.translate("MainWindow", "查询历史记录"))
        self.queryRoam.setText(self.translate("MainWindow", "漫游历史信息"))
        self.upload_file.setText(self.translate("MainWindow", "上传文件"))
        self.download_file.setText(self.translate("MainWindow", "下载文件"))
        self.logout.setText(self.translate("MainWindow", "注销登录"))
        self.send_message_bnt.setText(self.translate("MainWindow", "发送"))

        self.exitAct1 = QAction(QIcon('send1.png'), '&Send Message', MainWindow)
        self.exitAct1.setShortcut('Ctrl+S')
        self.exitAct1.setStatusTip('sending ...')
        self.exitAct1.triggered.connect(self.send_message)
        fileMenu = self.menubar.addMenu('&Tool')
        fileMenu.addAction(self.exitAct1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())

