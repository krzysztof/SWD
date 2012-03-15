import sys
from PyQt4 import *
from PyQt4.QtGui import QApplication, QDialog
import at_auto
from at_auto import Ui_Form


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QDialog()
	ui = Ui_Form()
	ui.setupUi(window)
	window.show()
	sys.exit(app.exec_())
