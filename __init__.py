from Ui_Main import *
import sys
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.openBtn.clicked.connect(print("test"))
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
