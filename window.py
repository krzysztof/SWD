# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Mon May 21 00:27:51 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(765, 635)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.typesLineEdit = QtGui.QLineEdit(self.widget)
        self.typesLineEdit.setObjectName(_fromUtf8("typesLineEdit"))
        self.horizontalLayout_2.addWidget(self.typesLineEdit)
        self.typesPushButton = QtGui.QPushButton(self.widget)
        self.typesPushButton.setObjectName(_fromUtf8("typesPushButton"))
        self.horizontalLayout_2.addWidget(self.typesPushButton)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.namesLineEdit = QtGui.QLineEdit(self.widget_2)
        self.namesLineEdit.setObjectName(_fromUtf8("namesLineEdit"))
        self.horizontalLayout.addWidget(self.namesLineEdit)
        self.namesPushButton = QtGui.QPushButton(self.widget_2)
        self.namesPushButton.setObjectName(_fromUtf8("namesPushButton"))
        self.horizontalLayout.addWidget(self.namesPushButton)
        self.verticalLayout.addWidget(self.widget_2)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.treeWidget.setPalette(palette)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setDefaultSectionSize(90)
        self.treeWidget.header().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.treeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuFile.sizePolicy().hasHeightForWidth())
        self.menuFile.setSizePolicy(sizePolicy)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName(_fromUtf8("menuData"))
        self.menuDebug = QtGui.QMenu(self.menubar)
        self.menuDebug.setObjectName(_fromUtf8("menuDebug"))
        self.menuStat = QtGui.QMenu(self.menubar)
        self.menuStat.setObjectName(_fromUtf8("menuStat"))
        self.menuPlot = QtGui.QMenu(self.menubar)
        self.menuPlot.setObjectName(_fromUtf8("menuPlot"))
        self.menuKlasyfikacja = QtGui.QMenu(self.menubar)
        self.menuKlasyfikacja.setObjectName(_fromUtf8("menuKlasyfikacja"))
        self.menuSklasyfikuj_obiekt = QtGui.QMenu(self.menuKlasyfikacja)
        self.menuSklasyfikuj_obiekt.setObjectName(_fromUtf8("menuSklasyfikuj_obiekt"))
        self.menuSprawd_ocene_klasyfikacji = QtGui.QMenu(self.menuKlasyfikacja)
        self.menuSprawd_ocene_klasyfikacji.setObjectName(_fromUtf8("menuSprawd_ocene_klasyfikacji"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAdd_Row = QtGui.QAction(MainWindow)
        self.actionAdd_Row.setObjectName(_fromUtf8("actionAdd_Row"))
        self.actionAdd_Col = QtGui.QAction(MainWindow)
        self.actionAdd_Col.setObjectName(_fromUtf8("actionAdd_Col"))
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionDelete_Row = QtGui.QAction(MainWindow)
        self.actionDelete_Row.setObjectName(_fromUtf8("actionDelete_Row"))
        self.actionDelete_Col = QtGui.QAction(MainWindow)
        self.actionDelete_Col.setObjectName(_fromUtf8("actionDelete_Col"))
        self.actionPopulate_from_set = QtGui.QAction(MainWindow)
        self.actionPopulate_from_set.setObjectName(_fromUtf8("actionPopulate_from_set"))
        self.actionDEBUG = QtGui.QAction(MainWindow)
        self.actionDEBUG.setObjectName(_fromUtf8("actionDEBUG"))
        self.actionEdit_Column_Types = QtGui.QAction(MainWindow)
        self.actionEdit_Column_Types.setObjectName(_fromUtf8("actionEdit_Column_Types"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionDyskretyzacjaPRD = QtGui.QAction(MainWindow)
        self.actionDyskretyzacjaPRD.setObjectName(_fromUtf8("actionDyskretyzacjaPRD"))
        self.actionDyskretyzacjaNK = QtGui.QAction(MainWindow)
        self.actionDyskretyzacjaNK.setObjectName(_fromUtf8("actionDyskretyzacjaNK"))
        self.actionStandaryzacja = QtGui.QAction(MainWindow)
        self.actionStandaryzacja.setObjectName(_fromUtf8("actionStandaryzacja"))
        self.actionNormalizacja = QtGui.QAction(MainWindow)
        self.actionNormalizacja.setObjectName(_fromUtf8("actionNormalizacja"))
        self.actionOdstajace3x = QtGui.QAction(MainWindow)
        self.actionOdstajace3x.setObjectName(_fromUtf8("actionOdstajace3x"))
        self.actionOdstajaceProcent = QtGui.QAction(MainWindow)
        self.actionOdstajaceProcent.setObjectName(_fromUtf8("actionOdstajaceProcent"))
        self.actionWykres2D = QtGui.QAction(MainWindow)
        self.actionWykres2D.setObjectName(_fromUtf8("actionWykres2D"))
        self.actionWykres3D = QtGui.QAction(MainWindow)
        self.actionWykres3D.setObjectName(_fromUtf8("actionWykres3D"))
        self.actionMetryk_Miejsk = QtGui.QAction(MainWindow)
        self.actionMetryk_Miejsk.setObjectName(_fromUtf8("actionMetryk_Miejsk"))
        self.actionMetryk_Euklidesow = QtGui.QAction(MainWindow)
        self.actionMetryk_Euklidesow.setObjectName(_fromUtf8("actionMetryk_Euklidesow"))
        self.actionMetryk_Mahalanobisa = QtGui.QAction(MainWindow)
        self.actionMetryk_Mahalanobisa.setObjectName(_fromUtf8("actionMetryk_Mahalanobisa"))
        self.actionMetryk_Euklidesow_2 = QtGui.QAction(MainWindow)
        self.actionMetryk_Euklidesow_2.setObjectName(_fromUtf8("actionMetryk_Euklidesow_2"))
        self.actionMetryk_Miejsk_2 = QtGui.QAction(MainWindow)
        self.actionMetryk_Miejsk_2.setObjectName(_fromUtf8("actionMetryk_Miejsk_2"))
        self.actionMetryk_Mahalanobisa_2 = QtGui.QAction(MainWindow)
        self.actionMetryk_Mahalanobisa_2.setObjectName(_fromUtf8("actionMetryk_Mahalanobisa_2"))
        self.actionAAA = QtGui.QAction(MainWindow)
        self.actionAAA.setObjectName(_fromUtf8("actionAAA"))
        self.actionMetoda_K_Srednich = QtGui.QAction(MainWindow)
        self.actionMetoda_K_Srednich.setObjectName(_fromUtf8("actionMetoda_K_Srednich"))
        self.actionMetoda_K_Srednich_optymalne_K = QtGui.QAction(MainWindow)
        self.actionMetoda_K_Srednich_optymalne_K.setObjectName(_fromUtf8("actionMetoda_K_Srednich_optymalne_K"))
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuData.addAction(self.actionAdd_Row)
        self.menuData.addAction(self.actionAdd_Col)
        self.menuData.addAction(self.actionDelete_Row)
        self.menuData.addAction(self.actionDelete_Col)
        self.menuDebug.addAction(self.actionPopulate_from_set)
        self.menuDebug.addAction(self.actionClear)
        self.menuDebug.addAction(self.actionDEBUG)
        self.menuStat.addAction(self.actionDyskretyzacjaPRD)
        self.menuStat.addAction(self.actionDyskretyzacjaNK)
        self.menuStat.addAction(self.actionStandaryzacja)
        self.menuStat.addAction(self.actionNormalizacja)
        self.menuStat.addAction(self.actionOdstajace3x)
        self.menuStat.addAction(self.actionOdstajaceProcent)
        self.menuPlot.addAction(self.actionWykres2D)
        self.menuPlot.addAction(self.actionWykres3D)
        self.menuSklasyfikuj_obiekt.addAction(self.actionMetryk_Euklidesow_2)
        self.menuSklasyfikuj_obiekt.addAction(self.actionMetryk_Miejsk_2)
        self.menuSklasyfikuj_obiekt.addAction(self.actionMetryk_Mahalanobisa_2)
        self.menuSprawd_ocene_klasyfikacji.addAction(self.actionMetryk_Euklidesow)
        self.menuSprawd_ocene_klasyfikacji.addAction(self.actionMetryk_Miejsk)
        self.menuSprawd_ocene_klasyfikacji.addAction(self.actionMetryk_Mahalanobisa)
        self.menuKlasyfikacja.addAction(self.menuSklasyfikuj_obiekt.menuAction())
        self.menuKlasyfikacja.addAction(self.menuSprawd_ocene_klasyfikacji.menuAction())
        self.menuKlasyfikacja.addAction(self.actionMetoda_K_Srednich)
        self.menuKlasyfikacja.addAction(self.actionMetoda_K_Srednich_optymalne_K)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuStat.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuKlasyfikacja.menuAction())
        self.menubar.addAction(self.menuDebug.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Systemy Wspomagania Decyzji", None, QtGui.QApplication.UnicodeUTF8))
        self.typesPushButton.setText(QtGui.QApplication.translate("MainWindow", "Cast Types", None, QtGui.QApplication.UnicodeUTF8))
        self.namesPushButton.setText(QtGui.QApplication.translate("MainWindow", "Change Names", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData.setTitle(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDebug.setTitle(QtGui.QApplication.translate("MainWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.menuStat.setTitle(QtGui.QApplication.translate("MainWindow", "Stat", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlot.setTitle(QtGui.QApplication.translate("MainWindow", "Wykresy", None, QtGui.QApplication.UnicodeUTF8))
        self.menuKlasyfikacja.setTitle(QtGui.QApplication.translate("MainWindow", "Klasyfikacja", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSklasyfikuj_obiekt.setTitle(QtGui.QApplication.translate("MainWindow", "Sklasyfikuj obiekt", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSprawd_ocene_klasyfikacji.setTitle(QtGui.QApplication.translate("MainWindow", "Sprawdź ocene klasyfikacji", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Row.setText(QtGui.QApplication.translate("MainWindow", "Add Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Col.setText(QtGui.QApplication.translate("MainWindow", "Add Col", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("MainWindow", "(DEBUG)Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Row.setText(QtGui.QApplication.translate("MainWindow", "Delete Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Col.setText(QtGui.QApplication.translate("MainWindow", "Delete Col", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPopulate_from_set.setText(QtGui.QApplication.translate("MainWindow", "(DEBUG)Populate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDEBUG.setText(QtGui.QApplication.translate("MainWindow", "DEBUG", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Column_Types.setText(QtGui.QApplication.translate("MainWindow", "Edit Column Types", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDyskretyzacjaPRD.setText(QtGui.QApplication.translate("MainWindow", "Dyskretyzacja PRD", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDyskretyzacjaNK.setText(QtGui.QApplication.translate("MainWindow", "Dyskretyzacja NK", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStandaryzacja.setText(QtGui.QApplication.translate("MainWindow", "Standaryzacja", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNormalizacja.setText(QtGui.QApplication.translate("MainWindow", "Normalizacja MinMax", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOdstajace3x.setText(QtGui.QApplication.translate("MainWindow", "Odstajace3x", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOdstajaceProcent.setText(QtGui.QApplication.translate("MainWindow", "OdstajaceProcent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWykres2D.setText(QtGui.QApplication.translate("MainWindow", "Wykres2D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWykres3D.setText(QtGui.QApplication.translate("MainWindow", "Wykres3D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetryk_Miejsk.setText(QtGui.QApplication.translate("MainWindow", "Metryką Miejską", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetryk_Euklidesow.setText(QtGui.QApplication.translate("MainWindow", "Metryką Euklidesową", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetryk_Mahalanobisa.setText(QtGui.QApplication.translate("MainWindow", "Metryką Mahalanobisa", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetryk_Euklidesow_2.setText(QtGui.QApplication.translate("MainWindow", "Metryką Euklidesową", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetryk_Miejsk_2.setText(QtGui.QApplication.translate("MainWindow", "Metryką Miejską", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetryk_Mahalanobisa_2.setText(QtGui.QApplication.translate("MainWindow", "Metryką Mahalanobisa", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAAA.setText(QtGui.QApplication.translate("MainWindow", "AAA", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetoda_K_Srednich.setText(QtGui.QApplication.translate("MainWindow", "Metoda K-Srednich", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetoda_K_Srednich_optymalne_K.setText(QtGui.QApplication.translate("MainWindow", "Metoda K-Srednich - optymalne K", None, QtGui.QApplication.UnicodeUTF8))

