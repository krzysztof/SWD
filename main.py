# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys
from SWD import Zbior
# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from window import Ui_MainWindow

# Import our backend
#import todo

# Create a class for our main window
class ChangeTypeDialog(QtGui.QWidget):

	 def __init__(self,window):
		  super(ChangeTypeDialog,self).__init__()
		  self.window = window
		  self.initUI()

	 def initUI(self):
		  possible = [int,float,bool,unicode]
		  cols = self.window.ui.treeWidget.columnCount()
		  combos = []
		  vbox = QtGui.QVBoxLayout(self)
		  for i in range(cols):
				cbx = QtGui.QComboBox()
				for p in possible:
					 cbx.addItems(QtCore.QStringList([str(x) for x in possible]))
				vbox.addWidget(cbx)
				combos.append(cbx)
		  self.show()

class Main(QtGui.QMainWindow):
	 def DEBUG(self):
#		  self.print_data()
		  #self.refresh_data()
		  self.edit_types()
	 
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

	 def refresh_data(self):
		  data = Zbior()
		  cols = self.ui.treeWidget.columnCount()
		  rows = self.ui.treeWidget.topLevelItemCount()
		  #self.ui.treeWidget.setHeaderLabels(["xxx"]*cols)
		  labels = self.ui.treeWidget.headerItem()
		  data.dodaj_kolumny([u'%s'%labels.text(i) for i in xrange(cols)])
		  #narazie x razy unicode
		  #data.dodaj_typy(self.zb.typy)
		  data.dodaj_typy([unicode for i in xrange(cols)])
		  lista = []
		  root = self.ui.treeWidget.invisibleRootItem()
		  child_count = root.childCount()
		  for i in range(child_count):
				item = root.child(i)
				lista.append([data.typy[i](u'%s'%item.text(i)) for i in range(cols)])
		  data.dodaj_liste(lista)
		  self.zb = data

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
		  self.ui.typesLineEdit.insert(text)

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

	 def add_row(self):
		  add_row(None)
		  
	 def add_row(self,row_data):
		  item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
		  if(row_data):
				for i in xrange(len(row_data)):
					 text = QtGui.QApplication.translate("MainWindow", row_data[i], None, QtGui.QApplication.UnicodeUTF8)
					 item.setText(i,text)
		  item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

	 def add_empty_column(self):
		  text, ok = QtGui.QInputDialog.getText(self, 'Nowa kolumna', 'Podaj nazwe')
		  if ok:
				self.add_column(str(text))
		  
	 def add_column(self,nazwa):
		  idx = self.ui.treeWidget.columnCount()
		  self.ui.treeWidget.headerItem().setText(idx, QtGui.QApplication.translate("MainWindow", nazwa, None, QtGui.QApplication.UnicodeUTF8))

	 def __init__(self):
		  QtGui.QMainWindow.__init__(self)
        
        # This is always the same
		  self.ui=Ui_MainWindow()
		  self.ui.setupUi(self)
		  self.clear_tree()

		  self.ui.actionAdd_Row.triggered.connect(self.add_row)
		  self.ui.actionAdd_Col.triggered.connect(self.add_empty_column)
		  self.ui.actionClear.triggered.connect(self.clear_tree)
		  self.ui.actionPopulate_from_set.triggered.connect(self.populate_from_set)
		  self.ui.actionDEBUG.triggered.connect(self.DEBUG)
		  self.ui.typesPushButton.clicked.connect(self.edit_types)
		  self.TypToS = {str(int):"int",str(float):"float",str(bool):"bool",str(unicode):"unicode"}
		  self.SToTyp = {"int":int,"float":float,"bool":bool,"unicode":unicode}

        # Let's do something interesting: load the database contents 
        # into our task list widget
#        for task in todo.Task.query().all():
#            tags=','.join([t.name for t in task.tags])
#            item=QtGui.QTreeWidgetItem([task.text,str(task.date),tags])
#            item.task=task
#            if task.done:
#                item.setCheckState(0,QtCore.Qt.Checked)
#            else:
#                item.setCheckState(0,QtCore.Qt.Unchecked)
#            self.ui.list.addTopLevelItem(item)

#    def on_list_itemChanged(self,item,column):
#        if item.checkState(0):
#            item.task.done=True
#        else:
#            item.task.done=False
#        todo.saveData()


def main_DBG():
	 app = QtGui.QApplication(sys.argv)
	 window=Main()
	 window.show()
	 zb = Zbior()
	 zb.wczytaj('dane.txt','    ',11,'Q')
	 window.set_zbior(zb)
	 window.populate_from_set()
	 window.DEBUG()
    # It's exec_ because exec is a reserved word in Python
	 sys.exit(app.exec_())
    
def main():
    # Init the database before doing anything else
#    todo.initDB()
    
    # Again, this is boilerplate, it's going to be the same on 
    # almost every app you write
	 app = QtGui.QApplication(sys.argv)
	 window=Main()
	 window.show()
    # It's exec_ because exec is a reserved word in Python
	 sys.exit(app.exec_())
    

if __name__ == "__main__":
    main_DBG()
