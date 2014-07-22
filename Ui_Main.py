# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pyprj\AutoPublisher\Main.ui'
#
# Created: Tue Jul 22 13:16:40 2014
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
        Dialog.setWhatsThis(_fromUtf8(""))
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
        self.zipBtn = QtGui.QPushButton(Dialog)
        self.zipBtn.setEnabled(False)
        self.zipBtn.setGeometry(QtCore.QRect(150, 50, 71, 31))
        self.zipBtn.setToolTip(_fromUtf8(""))
        self.zipBtn.setObjectName(_fromUtf8("zipBtn"))
        self.svnUpdateBtn = QtGui.QPushButton(Dialog)
        self.svnUpdateBtn.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.svnUpdateBtn.setObjectName(_fromUtf8("svnUpdateBtn"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 470, 441, 81))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.checkBoxGroup = QtGui.QGroupBox(Dialog)
        self.checkBoxGroup.setGeometry(QtCore.QRect(10, 90, 441, 121))
        self.checkBoxGroup.setMouseTracking(False)
        self.checkBoxGroup.setToolTip(_fromUtf8(""))
        self.checkBoxGroup.setTitle(_fromUtf8(""))
        self.checkBoxGroup.setObjectName(_fromUtf8("checkBoxGroup"))
        self.isIncrement = QtGui.QCheckBox(Dialog)
        self.isIncrement.setGeometry(QtCore.QRect(10, 220, 91, 16))
        self.isIncrement.setObjectName(_fromUtf8("isIncrement"))
        self.dateTimeBefore = QtGui.QDateTimeEdit(Dialog)
        self.dateTimeBefore.setEnabled(False)
        self.dateTimeBefore.setGeometry(QtCore.QRect(210, 220, 194, 22))
        self.dateTimeBefore.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2100, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateTimeBefore.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateTimeBefore.setCalendarPopup(True)
        self.dateTimeBefore.setObjectName(_fromUtf8("dateTimeBefore"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 220, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(410, 220, 54, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.deleteEmptyFolder = QtGui.QCheckBox(Dialog)
        self.deleteEmptyFolder.setEnabled(False)
        self.deleteEmptyFolder.setGeometry(QtCore.QRect(10, 250, 131, 16))
        self.deleteEmptyFolder.setObjectName(_fromUtf8("deleteEmptyFolder"))
        self.resultTxt = QtGui.QTextBrowser(Dialog)
        self.resultTxt.setGeometry(QtCore.QRect(10, 270, 441, 192))
        self.resultTxt.setObjectName(_fromUtf8("resultTxt"))

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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2. 增量更新会删除修改时间早于指定时间的文件，并且可以设置是否删除空的文件夹。</p></body></html>", None))
        self.isIncrement.setText(_translate("Dialog", "是否增量更新", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>删除早于</p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>的文件</p></body></html>", None))
        self.deleteEmptyFolder.setText(_translate("Dialog", "是否删除空文件夹", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

