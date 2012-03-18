# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'at.ui'
#
# Created: Tue Mar 13 22:41:26 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.command = QtGui.QLineEdit(Form)
        self.command.setGeometry(QtCore.QRect(20, 130, 113, 24))
        self.command.setObjectName(_fromUtf8("command"))
        self.time = QtGui.QDateTimeEdit(Form)
        self.time.setGeometry(QtCore.QRect(180, 90, 194, 24))
        self.time.setObjectName(_fromUtf8("time"))
        self.schedule = QtGui.QPushButton(Form)
        self.schedule.setGeometry(QtCore.QRect(200, 230, 85, 27))
        self.schedule.setObjectName(_fromUtf8("schedule"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.schedule.setText(QtGui.QApplication.translate("Form", "Schedule", None, QtGui.QApplication.UnicodeUTF8))

