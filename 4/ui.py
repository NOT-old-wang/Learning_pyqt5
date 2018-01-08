# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        '''少了下面两句话，windows下有点问题'''
#        self.centralwidget = QtWidgets.QWidget(Form)
#        self.centralwidget.setObjectName("centralwidget")  
        ''''''
        self.horizontalScrollBar = QtWidgets.QScrollBar(Form)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(40, 190, 301, 21))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.Button_print = QtWidgets.QPushButton(Form)
        self.Button_print.setGeometry(QtCore.QRect(40, 230, 75, 23))
        self.Button_print.setObjectName("Button_print")
        self.Button_quit = QtWidgets.QPushButton(Form)
        self.Button_quit.setGeometry(QtCore.QRect(260, 230, 75, 23))
        self.Button_quit.setObjectName("Button_quit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 20, 291, 171))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        self.Button_quit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Test"))
        self.Button_print.setText(_translate("Form", "Print"))
        self.Button_quit.setText(_translate("Form", "Quit"))

