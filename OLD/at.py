# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'at.ui'
#
# Created: Sun Mar 18 11:48:41 2012
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
        Form.resize(595, 457)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 451))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.lst_items = QtGui.QListView(self.tab_1)
        self.lst_items.setGeometry(QtCore.QRect(0, 10, 341, 411))
        self.lst_items.setObjectName(_fromUtf8("lst_items"))
        self.btn_row = QtGui.QPushButton(self.tab_1)
        self.btn_row.setGeometry(QtCore.QRect(350, 10, 85, 27))
        self.btn_row.setObjectName(_fromUtf8("btn_row"))
        self.btn_col = QtGui.QPushButton(self.tab_1)
        self.btn_col.setGeometry(QtCore.QRect(350, 40, 85, 27))
        self.btn_col.setObjectName(_fromUtf8("btn_col"))
        self.btn_file = QtGui.QPushButton(self.tab_1)
        self.btn_file.setGeometry(QtCore.QRect(350, 70, 85, 27))
        self.btn_file.setObjectName(_fromUtf8("btn_file"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textEdit = QtGui.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 571, 401))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_row.setText(QtGui.QApplication.translate("Form", "Add Row", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_col.setText(QtGui.QApplication.translate("Form", "Add Column", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_file.setText(QtGui.QApplication.translate("Form", "file..", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("Form", "Data Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Debug", None, QtGui.QApplication.UnicodeUTF8))

