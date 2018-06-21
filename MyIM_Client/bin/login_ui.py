# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import re
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from MyIM_Client.core.main_controller import RunnerMointor
from MyIM_Client.conf.settings import LOGIN_SERVER


class Ui_Dialog(object):

    def __init__(self, main_obj):
        super().__init__()
        self.main_monitor = main_obj
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.retranslateUi(self.dialog)
        self.dialog.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Login&Reg")
        Dialog.resize(277, 212)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditName = QtWidgets.QLineEdit(self.tab)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout_2.addWidget(self.lineEditName)
        self.lineEditPwd = QtWidgets.QLineEdit(self.tab)
        self.lineEditPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPwd.setObjectName("lineEditPwd")
        self.verticalLayout_2.addWidget(self.lineEditPwd)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.bnLogin = QtWidgets.QPushButton(self.tab)
        self.bnLogin.setEnabled(False)
        self.bnLogin.setObjectName("bnLogin")
        self.horizontalLayout_3.addWidget(self.bnLogin)
        self.bnCancel = QtWidgets.QPushButton(self.tab)
        self.bnCancel.setObjectName("bnCancel")
        self.horizontalLayout_3.addWidget(self.bnCancel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEditNameReg = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditNameReg.setObjectName("lineEditNameReg")
        self.verticalLayout_4.addWidget(self.lineEditNameReg)
        self.lineEditPwdReg1 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditPwdReg1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPwdReg1.setObjectName("lineEditPwdReg1")
        self.verticalLayout_4.addWidget(self.lineEditPwdReg1)
        self.lineEditPwdReg2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditPwdReg2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPwdReg2.setObjectName("lineEditPwdReg2")
        self.verticalLayout_4.addWidget(self.lineEditPwdReg2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.bnReg = QtWidgets.QPushButton(self.tab_2)
        self.bnReg.setEnabled(False)
        self.bnReg.setObjectName("bnReg")
        self.horizontalLayout_4.addWidget(self.bnReg)
        self.bnCancelReg = QtWidgets.QPushButton(self.tab_2)
        self.bnCancelReg.setObjectName("bnCancelReg")
        self.horizontalLayout_4.addWidget(self.bnCancelReg)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.tabWidget.raise_()
        self.label.setBuddy(self.lineEditName)
        self.label_2.setBuddy(self.lineEditPwd)
        self.label_3.setBuddy(self.lineEditNameReg)
        self.label_4.setBuddy(self.lineEditPwdReg1)
        self.label_5.setBuddy(self.lineEditPwdReg2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)

        self.lineEditName.textChanged.connect(self.enable_login)
        self.lineEditNameReg.textChanged.connect(self.enable_register)
        self.bnLogin.clicked.connect(self.login_auth)
        self.bnReg.clicked.connect(self.register_auth)

        self.bnCancel.clicked.connect(Dialog.close)
        self.bnCancelReg.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditName, self.lineEditPwd)
        Dialog.setTabOrder(self.lineEditPwd, self.bnLogin)
        Dialog.setTabOrder(self.bnLogin, self.bnCancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MyIM"))
        self.label.setText(_translate("Dialog", "Login Name"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.bnLogin.setText(_translate("Dialog", "Login"))
        self.bnCancel.setText(_translate("Dialog", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog", "Login Name"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.label_5.setText(_translate("Dialog", "Retype"))
        self.bnReg.setText(_translate("Dialog", "Reg"))
        self.bnCancelReg.setText(_translate("Dialog", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Register"))

    def enable_login(self):
        username = self.lineEditName.text()
        res = re.match(r"\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*", username)
        if res is not None:
            self.bnLogin.setEnabled(True)
        else:
            self.bnLogin.setEnabled(False)

    def enable_register(self):
        username = self.lineEditNameReg.text()
        res = re.match(r"\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*", username)
        if res is not None:
            self.bnReg.setEnabled(True)
        else:
            self.bnReg.setEnabled(False)

    def login_auth(self):
        global message_queue
        username = self.lineEditName.text()
        password = self.lineEditPwd.text()
        self.message1 = QMessageBox()
        if len(password) < 6:
            self.message1.setText("不能密码长度小于6！")
            self.message1.show()
        else:
            from MyIM_Client.core.login import LoginClient
            login_obj = LoginClient(username, password, LOGIN_SERVER['ADDRESS'], LOGIN_SERVER['PORT'])
            login_obj.connect()
            res = login_obj.auth()
            if res['code'] == 200:
                # create main ui and destroy login ui
                self.dialog.hide()
                self.main_monitor.show(login_obj, username)

            elif res['code'] == 302:
                self.message1.setText(res['message'])
                self.message1.show()
                self.lineEditPwd.setText("")

    def register_auth(self):
        global message_queue
        username = self.lineEditNameReg.text()
        password_1 = self.lineEditPwdReg1.text()
        password_2 = self.lineEditPwdReg2.text()
        if password_1 != password_2:
            self.message1 = QMessageBox()
            self.message1.setText("两次密码不一致！")
            self.message1.show()
        elif len(password_1) < 6:
            self.message1 = QMessageBox()
            self.message1.setText("不能密码长度小于6！")
            self.message1.show()
        else:
            from MyIM_Client.core.login import LoginClient
            login_obj = LoginClient(username, password_1)
            login_obj.connect()
            res = login_obj.reg()
            login_obj.disconnect()
            self.message1 = QMessageBox()
            if res['code'] == 200:
                self.message1.setText(res['message'])
                self.message1.show()
            elif res['code'] == 414:
                self.message1.setText(res['message'])
                self.message1.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_monitor = RunnerMointor()
    ex = Ui_Dialog(main_monitor)
    sys.exit(app.exec_())
