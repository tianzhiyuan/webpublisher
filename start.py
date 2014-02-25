import sys
from Ui_Main import *
from PyQt4 import QtCore, QtGui
import publish
import os
from asyncTask import Task
class StartQT4(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,  parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.Published = False
        QtCore.QObject.connect(self.ui.openBtn,QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.loadBtn,  QtCore.SIGNAL("clicked()"),  self.file_exec)
        QtCore.QObject.connect(self.ui.svnUpdateBtn,  QtCore.SIGNAL("clicked()"),  self.svn_update)
        QtCore.QObject.connect(self.ui.zipBtn,  QtCore.SIGNAL("clicked()"),  self.zip_file)
        QtCore.QObject.connect(self.ui.filepathTxt,  QtCore.SIGNAL("textChanged(const QString&)"),  self.refresh)
        self.GeneralConfig = None
        self.Configs = []
        self._LoadDefaultConfig()
    def _LoadDefaultConfig(self):
        defaultPath = os.path.join(os.path.abspath('.'),  "config.ini")
        self.ui.filepathTxt.setText(defaultPath)
    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        filename = fd.getOpenFileName(self,"Open File",  "/",  "Ini File(*.ini)")
        self.ui.filepathTxt.setText(filename)
    def file_exec(self):
       
        txt = self.ui.resultTxt
        configs = self.getSelectedConfigs()
        if(len(configs) == 0):
            return
        def cb(pconfigs,  textarea):
            print ("in cb")
            for c in pconfigs:
                textarea.appendPlainText('Source project is [%s.csproj]'%(c.ProjectName))
                textarea.appendPlainText('Publishing...')
                try:
                    
                    [status,  output] = publish.PublishHelper.Publish(c)
                    
                    if(status != 0):
                        textarea.appendPlainText('发布出现错误，具体查看以下消息：\n%s'%(output))
                    else:
                        textarea.appendPlainText('Project published to directory: [%s]'%(c.PublishPath))
                except Exception as e:
                    textarea.appendPlainText("%s"%(e))
        cb(configs,  txt)
        self.Published = True
    def svn_update(self):
        c = self.GeneralConfig
        publish.PublishHelper.ProcessGeneralConfig(c)
    def zip_file(self):
        filename = self.ui.filepathTxt.text();
        c = publish.PublishHelper.ReadGeneralConfigFromFile(filename)
        if(c is None):
            return
        if(not self.Published):
            return
        if(c.ZipPath == ""):
            return
        for config in self.Configs:
            publish.PublishHelper.ZipFile(config.PublishPath,  config.ProjectName,  c.ZipPath)
        self.ui.resultTxt.appendPlainText('[Info] 压缩完成')
    def DrawProjectConfig(self,  configs):
        if(configs is None or len(configs) <= 0):
            return
        
        checkBoxes = []
        layout = self.ui.checkBoxGroup.layout()
        if(layout is None):
             layout = QtGui.QVBoxLayout()
        while(layout.count()):
            c = layout.takeAt(0)
            c.widget().deleteLater()
        for c in configs:
            checkbox = QtGui.QCheckBox(c.ProjectName)
            checkBoxes.append(checkbox)
            checkbox.setChecked(True)
            layout.addWidget(checkbox)
        self.ui.checkBoxGroup.setLayout(layout)
    def refresh(self,  text):
        filename = text
        c = publish.PublishHelper.ReadConfigFromFile(filename)
        self.DrawProjectConfig(c)
        self.Configs = c
        self.GeneralConfig = publish.PublishHelper.ReadGeneralConfigFromFile(filename)
    def getSelectedConfigs(self):
        selected = []
        layout = self.ui.checkBoxGroup.layout()
        if(self.Configs != None and len(self.Configs) > 0 and layout != None):
            for i in range(layout.count()):
                c = self.Configs[i]
                if(c != None and layout.itemAt(i).widget().isChecked()):
                    selected.append(c)
        return selected
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
    
