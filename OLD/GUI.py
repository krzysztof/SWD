import sys
from PyQt4 import QtGui,QtCore
from SWD import *

typ = [int, float, str, str ,bool]
names = ['zm1','zm2','Imie','Miasto','?']
vals = [[1,2.33,"ALA","Warszawa",True],
	[-3,3.33,"Jacek","A",True],
	[3,61.33,"Ola","X",False]]
zb = Zbior()
zb.dodaj_liste(vals)
zb.dodaj_typy(typ)
zb.dodaj_kolumny(names)



class MainOkno(QtGui.QMainWindow):
	
	def __init__(self):
		super(MainOkno, self).__init__()		
		self.initUI()
		
	def initUI(self):
		
		self.tabWidget = QtGui.QTabWidget()
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 451))
		self.tab_1 = QtGui.QWidget()
		self.tab_2 = QtGui.QWidget()
		self.tabWidget.addTab(self.tab_1,"Data Edit")
		self.tabWidget.addTab(self.tab_2,"Debug")
		self.tabWidget.setCurrentIndex(1)

#		self.textEdit = QtGui.QTextEdit()
#		self.setCentralWidget(self.textEdit)
#		self.statusBar()
#		self.lst_items = QtGui.QListView(self)
#		self.lst_items.setGeometry(QtCore.QRect(0,10,300,300))

#		openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
#		openFile.setShortcut('Ctrl+O')
#		openFile.setStatusTip('Open new File')
#		openFile.triggered.connect(self.showDataDialog)
	
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)	   
			
		self.setGeometry(300, 300, 600, 600)
		self.setWindowTitle('File dialog')
		self.show()
	def showDataDialog(self):
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.')		
		f = open(fname, 'r')
		
		with f:		
			data = f.read()
			self.textEdit.setText(data) 

		
def main():
	
	app = QtGui.QApplication(sys.argv)
	ex = MainOkno()
	sys.exit(app.exec_())
	print zb



if(__name__ == "__main__"):
	main()
	
