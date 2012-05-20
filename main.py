#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys
from SWD import *
# Import Qt modules
from PyQt4 import QtCore,QtGui


from window import Ui_MainWindow


# juz niepotrzebna klasa
###class ChangeTypeDialog(QtGui.QWidget):
###
###	def __init__(self,window):
###		super(ChangeTypeDialog,self).__init__()
###		self.window = window
###		self.initUI()
###
###	def initUI(self):
###		possible = [int,float,bool,unicode]
###		cols = self.window.ui.treeWidget.columnCount()
###		combos = []
###		vbox = QtGui.QVBoxLayout(self)
###		for i in range(cols):
###				cbx = QtGui.QComboBox()
###				for p in possible:
###					cbx.addItems(QtCore.QStringList([str(x) for x in possible]))
###				vbox.addWidget(cbx)
###				combos.append(cbx)
###		self.show()

class Main(QtGui.QMainWindow):
	def DEBUG(self):
		self.recast_data()
		#self.print_data()
		#self.refresh_data()
		#self.edit_types()
	def remove_row(self,i):
		self.zb.usun_obserwacja(i)
		self.populate_from_set()
	def remove_col(self,i):
		self.zb.usun_zmienna(int(i))
		self.populate_from_set()
	
	def print_data(self):
		cols = self.ui.treeWidget.columnCount()
		rows = self.ui.treeWidget.topLevelItemCount()
		zb = Zbior()
		root = self.ui.treeWidget.invisibleRootItem()
		child_count = root.childCount()
		lista = []
		for i in range(child_count):
				item = root.child(i)
				lista.append([u'%s'%(item.text(i)) for i in range(cols)])
		for i in lista:
				print i
		#for i in range(cols):
				#print self.ui.treeWidget.
		#print cols,rows

	def recast_data(self):
		for i in range(len(self.zb.typy)):
				self.zb.rzutuj(self.zb.typy[i],i)
		

	def get_translated(self,string):
		return QtGui.QApplication.translate("MainWindow", string, None, QtGui.QApplication.UnicodeUTF8)
	def populate_from_set(self):
		zb = self.zb
		if(not zb):
				print "Zbior not set"
		self.clear_tree()
		for i in zb.kolumny:
				self.add_column(i)
		for i in zb.lista:
				self.add_row(i)
		text = ",".join([self.TypToS[str(x)] for x in zb.typy])
		self.ui.typesLineEdit.setText(text)
		col_num = len(zb.kolumny)
		text = self.get_translated('')
		for i in range(col_num-1):
			text+=self.get_translated(zb.kolumny[i]+',')
		text+=self.get_translated(str(zb.kolumny[col_num-1]))
		
		#text = self.get_translated(',').join([self.get_translated(str(x)) for x in zb.kolumny])
		#text = ",".join(zb.kolumny)
		self.ui.namesLineEdit.setText(text)

	def set_zbior(self,zb):
		self.zb = zb;

	def clear_tree(self):
		#self.ui.treeWidget = QtGui.QTreeWidget(self.ui.centralwidget)
		self.ui.treeWidget.clear()
		self.ui.treeWidget.setColumnCount(0)

	def edit_types(self):
		types = [self.SToTyp[str(x).strip()] for x in self.ui.typesLineEdit.text().split(',')]
		if(len(types) != len(self.zb.typy)):
				print "can't cast! different size of types"
		else:
				self.zb.typy = types
				for i in range(len(types)):
					self.zb.rzutuj(types[i],i)
				#for i in range(len(types)):
					#self.zb.rzutuj(types[i],i)
				self.populate_from_set()

	def edit_names(self):
		names = [unicode(x).strip() for x in self.ui.namesLineEdit.text().split(',')]
		if(len(names) != len(self.zb.kolumny)):
				print "can't cast! different size of types"
		else:
				self.zb.kolumny = names
				self.populate_from_set()


	#def add_row(self):
		#add_row(None)
		
	def add_row(self,row_data):
		item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
		if(row_data):
				for i in xrange(len(row_data)):
					text = QtGui.QApplication.translate("MainWindow", str(row_data[i]), None, QtGui.QApplication.UnicodeUTF8)
					item.setText(i,text)
		item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

	def add_empty_column(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Nowa kolumna', 'Podaj nazwe')
		if ok:
				self.add_column(str(text))
	def remove_column_dialog(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Usun kolumne', 'Podaj numer kolumny')
		if ok:
				self.remove_col(int(text))
	def remove_row_dialog(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Usun wiersz', 'Podaj numer wiersza')
		if ok:
				self.remove_row(int(text))
	def add_column(self,nazwa):
		idx = self.ui.treeWidget.columnCount()
		self.ui.treeWidget.headerItem().setText(idx, QtGui.QApplication.translate("MainWindow", nazwa, None, QtGui.QApplication.UnicodeUTF8))
	def save_data(self):
		fname = QtGui.QFileDialog.getSaveFileName(self,'Zapisz plik','.')
		if(not fname):
				return
		separ, ok = QtGui.QInputDialog.getText(self, 'Separator', 'Podaj separator (\\t dla tabulatora)')
		if not ok:
				return
		kol, ok = QtGui.QInputDialog.getText(self, 'Nazwy kolumn', 'Zapisac nazwy kolumn ? [T/N]')
		if not ok:
				return
		if(str(kol).upper()=="T"):
			  kol=True
		else:
			  kol=False
		typy, ok = QtGui.QInputDialog.getText(self, 'Nazwy typow', 'Zapisac nazwy typów ? [T/N]')
		if not ok:
				return
		if(separ=='\\t'):separ='\t'
		if(str(typy).upper()=="T"):
			  typy=True
		else:
			  typy=False
		self.zb.zapisz(fname,separ,kol,typy)
		#pass
	def load_data(self):
		zb = Zbior()
		fname = QtGui.QFileDialog.getOpenFileName(self,'Otworz plik','.')
		if(not fname):
				return
		sep, ok = QtGui.QInputDialog.getText(self, 'Separator', 'Podaj separator (\\t dla tabulatora)')
		if not ok:
				return
		ile, ok = QtGui.QInputDialog.getText(self, 'Pomijanie wierszy', 'Ile wierszy pominac ?')
		if not ok:
				return
		kolumny, ok = QtGui.QInputDialog.getText(self, 'Nazwy kolumn', 'Czu 0 wiersz to nazwy kolumn [T/N] ?')
		if not ok:
				return
		typy, ok = QtGui.QInputDialog.getText(self, 'Nazwy typow', 'Czu 1 wiersz to nazwy typu [T/N] ?')
		if not ok:
				return
		if(sep=='\\t'):sep='\t'
		if(str(kolumny).upper()=='T'):
				kolumny = True
		else:
				kolumny = False
				
		if(str(typy).upper()=='T'):
				typy = True
		else:
				typy = False

		zb.wczytaj(fname,sep,int(ile),kolumny,typy)
		self.zb = zb
		self.populate_from_set()
		if(typy==True):
				print "recasting"
				self.recast_data()
	def dyskretyzacjaPRD(self):
		kol, ok = QtGui.QInputDialog.getText(self, 'Kolumna', 'Podaj indeks kolumny:')
		if not ok:
				return
		n, ok = QtGui.QInputDialog.getText(self, 'N', 'Podaj N:')
		if not ok:
				return
		self.zb.dyskretyzuj(int(kol),int(n))
		self.populate_from_set()
	def dyskretyzacjaNK(self):
		kol, ok = QtGui.QInputDialog.getText(self, 'Kolumna', 'Podaj indeks kolumny:')
		if not ok:
				return
		n, ok = QtGui.QInputDialog.getText(self, 'N', 'Podaj N:')
		if not ok:
				return
		self.zb.dyskretyzuj2(int(kol),int(n))
		self.populate_from_set()
	def standaryzacja(self):
		kol, ok = QtGui.QInputDialog.getText(self, 'Kolumna', 'Podaj indeks kolumny:')
		if not ok:
				return
		self.zb.standaryzuj(int(kol))
		self.populate_from_set()
	def odstajace3x(self):
		kol, ok = QtGui.QInputDialog.getText(self, 'Kolumna', 'Podaj indeks kolumny:')
		if not ok:
				return
		self.zb.odchylenie_trzykrotne(int(kol))
		self.populate_from_set()
	def odstajaceProcent(self):
		mi, ok = QtGui.QInputDialog.getText(self, 'Minimum np 0.05', 'Podaj minimum:')
		if not ok:
				return
		mx, ok = QtGui.QInputDialog.getText(self, 'Maksimum np 0.95', 'Podaj maksimum:')
		if not ok:
				return
		kol, ok = QtGui.QInputDialog.getText(self, 'Kolumna', 'Podaj indeks kolumny:')
		if not ok:
				return
		self.zb.odstajace_procentowo(float(mi),float(mx),int(kol))
		self.populate_from_set()
	def normalizacja(self):
		mi, ok = QtGui.QInputDialog.getText(self, 'Minimum np 0.0', 'Podaj minimum:')
		if not ok:
				return
		mx, ok = QtGui.QInputDialog.getText(self, 'Maksimum np 50.0', 'Podaj maksimum:')
		if not ok:
				return
		kol, ok = QtGui.QInputDialog.getText(self, 'Kolumna', 'Podaj indeks kolumny:')
		if not ok:
				return
		self.zb.normalizuj(float(mi),float(mx),int(kol))
		self.populate_from_set()

	def make_col_list(self,col):
		return [self.zb.lista[i][col] for i in range(len(self.zb.lista))]

	def Wykres2D(self):
		import numpy_demo
		i, ok = QtGui.QInputDialog.getText(self, 'Wektor X', 'Podaj kolumne:')
		if not ok:
				return
		j, ok = QtGui.QInputDialog.getText(self, 'Wektor Y', 'Podaj kolumne:')
		if not ok:
				return
		color, ok = QtGui.QInputDialog.getText(self, 'Kolor', 'Podaj kolumne koloru:')
		if not ok:
				return
		i = int(i)
		j = int(j)
		color = int(color)
		l1 = self.make_col_list(i)
		l2 = self.make_col_list(j)
		l3 = self.make_col_list(color)
		numpy_demo.wykres(l1,l2,l3,self.zb.kolumny[i],self.zb.kolumny[j])
	def Wykres3D(self):
		import numpy_demo
		i, ok = QtGui.QInputDialog.getText(self, 'Wektor X', 'Podaj kolumne:')
		if not ok:
				return
		j, ok = QtGui.QInputDialog.getText(self, 'Wektor Y', 'Podaj kolumne:')
		if not ok:
				return
		k, ok = QtGui.QInputDialog.getText(self, 'Wektor Z', 'Podaj kolumne:')
		if not ok:
				return
		color, ok = QtGui.QInputDialog.getText(self, 'Kolor', 'Podaj kolumne koloru:')
		if not ok:
				return
		i = int(i)
		j = int(j)
		k = int(k)
		color = int(color)
		l1 = self.make_col_list(i)
		l2 = self.make_col_list(j)
		l3 = self.make_col_list(k)
		l4 = self.make_col_list(color)
		numpy_demo.wykres3D(l1,l2,l3,l4,[self.zb.kolumny[i],self.zb.kolumny[j],self.zb.kolumny[k]])
	def SprawdzKlasyfikacje(self, metryka):
		indeksy, ok = QtGui.QInputDialog.getText(self, 'Podaj wektory', 'Podaj kolumny oddzielone przecinkiem np. 4,6,7:')
		if not ok:
				return
		
		klasa, ok = QtGui.QInputDialog.getText(self, 'Klasa Decyzyjna', 'Podaj kolumne klasy decyzyjnej:')
		if not ok:
				return

		k, ok = QtGui.QInputDialog.getText(self, 'Sasiedzi', 'Podaj k:')
		if not ok:
				return
		indeksy = [int(i) for i in indeksy.split(',')]
		#metryka = self.zb.metrykaEuklidesowa
		ocena = self.zb.ocenaKlasyfikacji(int(k),metryka,int(klasa), indeksy)
		reply = QtGui.QMessageBox.question(self, 'Podsumowanie',
            "%d z %d Sklasyfikowanych poprawnie (%.2f %%)"%(ocena[0],ocena[1],float(ocena[0])*100./ocena[1]), 
            QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
	def PopupMessage(self,m1,m2):
		QtGui.QMessageBox.question(self, m1, m2, QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		
	def SprawdzEuklidesowa(self):
		self.SprawdzKlasyfikacje(self.zb.metrykaEuklidesowa)
		
	def SprawdzMiejska(self):
		self.SprawdzKlasyfikacje(self.zb.metrykaMiejska)
		
	def SprawdzMahalanobisa(self):
		self.SprawdzKlasyfikacje(self.zb.metrykaMahalanobisa)

	def KlasyfikujEuklidesowa(self):
		self.SklasyfikujObiekt(self.zb.metrykaEuklidesowa)
		
	def KlasyfikujMiejska(self):
		self.SklasyfikujObiekt(self.zb.metrykaMiejska)
		
	def KlasyfikujMahalanobisa(self):
		self.SklasyfikujObiekt(self.zb.metrykaMahalanobisa)

	def SklasyfikujObiekt(self, metryka):
		item_index = self.ui.treeWidget.indexFromItem(self.ui.treeWidget.currentItem()).row()
		if item_index == -1:
			self.PopupMessage("Niepoprawne zaznaczenie", "Prosze najpierw zaznaczyc obiekt z listy.")
		indeksy, ok = QtGui.QInputDialog.getText(self, 'Podaj wektory', 'Podaj kolumny oddzielone przecinkiem np. 4,6,7:')
		if not ok:
				return
		
		klasa, ok = QtGui.QInputDialog.getText(self, 'Klasa Decyzyjna', 'Podaj kolumne klasy decyzyjnej:')
		if not ok:
				return

		k, ok = QtGui.QInputDialog.getText(self, 'Sasiedzi', 'Podaj k:')
		if not ok:
				return
		indeksy = [int(i) for i in indeksy.split(',')]

		wynik =  self.zb.klasyfikuj(self.zb.lista[item_index],indeksy, int(klasa), metryka, int(k))
		zapisac, ok = QtGui.QInputDialog.getText(self, 'Zaktualizowac wynik na liscie ?', 'Uzyskano wynik:%s\nCzy chcesz zapisac wynik do obiektu ?[T/N]'%(wynik))
		if not ok:
				return
		if str(zapisac).upper()=="T":
			self.zb.lista[item_index][int(klasa)] = wynik
			self.populate_from_set()

	def __init__(self):
		QtGui.QMainWindow.__init__(self)

		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.clear_tree()

		self.ui.actionAdd_Row.triggered.connect(self.add_row)
		self.ui.actionAdd_Col.triggered.connect(self.add_empty_column)
		self.ui.actionDelete_Col.triggered.connect(self.remove_column_dialog)
		self.ui.actionDelete_Row.triggered.connect(self.remove_row_dialog)

		self.ui.actionClear.triggered.connect(self.clear_tree)
		self.ui.actionPopulate_from_set.triggered.connect(self.populate_from_set)
		self.ui.actionDEBUG.triggered.connect(self.DEBUG)
		self.ui.typesPushButton.clicked.connect(self.edit_types)
		self.ui.namesPushButton.clicked.connect(self.edit_names)
		self.ui.actionSave.triggered.connect(self.save_data)
		self.ui.actionLoad.triggered.connect(self.load_data)

		#zadanie1
		self.ui.actionDyskretyzacjaPRD.triggered.connect(self.dyskretyzacjaPRD)
		self.ui.actionDyskretyzacjaNK.triggered.connect(self.dyskretyzacjaNK)
		self.ui.actionStandaryzacja.triggered.connect(self.standaryzacja)
		self.ui.actionOdstajace3x.triggered.connect(self.odstajace3x)
		self.ui.actionOdstajaceProcent.triggered.connect(self.odstajaceProcent)
		self.ui.actionNormalizacja.triggered.connect(self.normalizacja)
		self.ui.actionWykres2D.triggered.connect(self.Wykres2D)
		self.ui.actionWykres3D.triggered.connect(self.Wykres3D)
		#self.ui.actionSprawdzOcene.triggered.connect(self.SprawdzOceneKlasyfikacji)
		#self.ui.actionSklasyfikujObiekt.triggered.connect(self.SklasyfikujObiekt)
		self.ui.actionMetryk_Euklidesow.triggered.connect(self.SprawdzEuklidesowa)
		self.ui.actionMetryk_Miejsk.triggered.connect(self.SprawdzMiejska)
		self.ui.actionMetryk_Mahalanobisa.triggered.connect(self.SprawdzMahalanobisa)
		self.ui.actionMetryk_Euklidesow_2.triggered.connect(self.KlasyfikujEuklidesowa)
		self.ui.actionMetryk_Miejsk_2.triggered.connect(self.KlasyfikujMiejska)
		self.ui.actionMetryk_Mahalanobisa_2.triggered.connect(self.KlasyfikujMahalanobisa)

		self.TypToS = TypToS
		self.SToTyp = SToTyp

def main_DBG():
	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()

	zb = Zbior()
	zb.wczytaj('dane2.txt','\t',0,True,True)
	window.set_zbior(zb)
	window.populate_from_set()
	window.recast_data()
	sys.exit(app.exec_())
    
#def main():
#
#	def SklasyfikujObiekt(self):
#		print "hiKlas"
#
#	def __init__(self):
#		QtGui.QMainWindow.__init__(self)
#        
#
#		self.ui=Ui_MainWindow()
#		self.ui.setupUi(self)
#		self.clear_tree()
#
#		self.ui.actionAdd_Row.triggered.connect(self.add_row)
#		self.ui.actionAdd_Col.triggered.connect(self.add_empty_column)
#		self.ui.actionDelete_Col.triggered.connect(self.remove_column_dialog)
#		self.ui.actionDelete_Row.triggered.connect(self.remove_row_dialog)
#
#		self.ui.actionClear.triggered.connect(self.clear_tree)
#		self.ui.actionPopulate_from_set.triggered.connect(self.populate_from_set)
#		self.ui.actionDEBUG.triggered.connect(self.DEBUG)
#		self.ui.typesPushButton.clicked.connect(self.edit_types)
#		self.ui.namesPushButton.clicked.connect(self.edit_names)
#		self.ui.actionSave.triggered.connect(self.save_data)
#		self.ui.actionLoad.triggered.connect(self.load_data)
#
#		#zadanie1
#		self.ui.actionDyskretyzacjaPRD.triggered.connect(self.dyskretyzacjaPRD)
#		self.ui.actionDyskretyzacjaNK.triggered.connect(self.dyskretyzacjaNK)
#		self.ui.actionStandaryzacja.triggered.connect(self.standaryzacja)
#		self.ui.actionOdstajace3x.triggered.connect(self.odstajace3x)
#		self.ui.actionOdstajaceProcent.triggered.connect(self.odstajaceProcent)
#		self.ui.actionNormalizacja.triggered.connect(self.normalizacja)
#		self.ui.actionWykres2D.triggered.connect(self.Wykres2D)
#		self.ui.actionWykres3D.triggered.connect(self.Wykres3D)
#		#self.ui.actionSprawdzOcene.triggered.connect(self.SprawdzOceneKlasyfikacji)
#		#self.ui.actionSklasyfikujObiekt.triggered.connect(self.SklasyfikujObiekt)
#		self.ui.actionMetryk_Euklidesow.triggered.connect(self.SprawdzEuklidesowa)
#		self.ui.actionMetryk_Miejsk.triggered.connect(self.SprawdzMiejska)
#		#self.ui.actionMetryk_Mahalanobisa.triggered.connect(self.SprawdzMahalanobisa)
#		self.ui.actionMetryk_Euklidesow_2.triggered.connect(self.KlasyfikujEuklidesowa)
#		self.ui.actionMetryk_Miejsk_2.triggered.connect(self.KlasyfikujMiejska)
#		#self.ui.actionMetryk_Mahalanobisa_2.triggered.connect(self.KlasyfikujMahalanobisa)
#
#		
#		self.TypToS = TypToS
#		self.SToTyp = SToTyp

def main_DBG():
	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()

	zb = Zbior()
	zb.wczytaj('dane/dane2.txt','\t',0,True,True)
	window.set_zbior(zb)
	window.populate_from_set()
	window.recast_data()
	sys.exit(app.exec_())
    
def main():

	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()

	sys.exit(app.exec_())
    

if __name__ == "__main__":
    main_DBG()
	#main()
	
