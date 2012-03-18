import sys
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow
import at
from at import Ui_Form


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QMainWindow()
	ui = Ui_Form()
	ui.setupUi(window)

	openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', window)
	openFile.setShortcut('Ctrl+O')
	openFile.setStatusTip('Open new File')
	openFile.triggered.connect(window.showDataDialog)
	
	ui.btn_file.clicked.connect(openFile)
	window.show()
	sys.exit(app.exec_())
