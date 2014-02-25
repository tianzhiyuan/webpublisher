# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pyprj\AutoPublisher\Main.ui'
#
# Created: Thu Feb 13 16:20:56 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(479, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("项目1.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.openBtn = QtGui.QPushButton(Dialog)
        self.openBtn.setGeometry(QtCore.QRect(380, 10, 71, 31))
        self.openBtn.setObjectName(_fromUtf8("openBtn"))
        self.loadBtn = QtGui.QPushButton(Dialog)
        self.loadBtn.setGeometry(QtCore.QRect(80, 50, 71, 31))
        self.loadBtn.setObjectName(_fromUtf8("loadBtn"))
        self.filepathTxt = QtGui.QLineEdit(Dialog)
        self.filepathTxt.setGeometry(QtCore.QRect(10, 10, 361, 31))
        self.filepathTxt.setObjectName(_fromUtf8("filepathTxt"))
        self.resultTxt = QtGui.QPlainTextEdit(Dialog)
        self.resultTxt.setGeometry(QtCore.QRect(10, 220, 441, 251))
        self.resultTxt.setObjectName(_fromUtf8("resultTxt"))
        self.zipBtn = QtGui.QPushButton(Dialog)
        self.zipBtn.setGeometry(QtCore.QRect(150, 50, 71, 31))
        self.zipBtn.setObjectName(_fromUtf8("zipBtn"))
        self.svnUpdateBtn = QtGui.QPushButton(Dialog)
        self.svnUpdateBtn.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.svnUpdateBtn.setObjectName(_fromUtf8("svnUpdateBtn"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 480, 441, 71))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.checkBoxGroup = QtGui.QGroupBox(Dialog)
        self.checkBoxGroup.setGeometry(QtCore.QRect(10, 90, 441, 121))
        self.checkBoxGroup.setTitle(_fromUtf8(""))
        self.checkBoxGroup.setObjectName(_fromUtf8("checkBoxGroup"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "自动发布工具", None))
        self.openBtn.setText(_translate("Dialog", "浏览", None))
        self.loadBtn.setText(_translate("Dialog", "发布", None))
        self.zipBtn.setText(_translate("Dialog", "压缩", None))
        self.svnUpdateBtn.setText(_translate("Dialog", "SVN更新", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">注意：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1. 本程序会删除和覆盖发布路径文件夹中的所有文件，在发布前要做好备份。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2. 发布过程中可能会假死，耐心等待。</p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

