import sys
from Ui_Main import *
from PyQt4 import QtCore, QtGui
import publish
import os
from asyncTask import Task
def removeEmptyFolders(path,  removeRoot = True):
    if not os.path.isdir(path):
        return
    files = os.listdir(path)
    if(len(files)):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                removeEmptyFolders(fullpath)
    
    files = os.listdir(path)
    if(len(files) == 0 and removeRoot):
        os.rmdir(path)
class MyThread(QtCore.QThread):
    complete = QtCore.pyqtSignal(object)
    def __init__(self,  configs,  textarea,  isIncrement = False,  deleteEmptyFolder = False,  dateTime = None):
        QtCore.QThread.__init__(self)
        self.configs = configs
        self.textarea = textarea
        self.IsIncrement = isIncrement
        self.dateTimeBefore = dateTime
        self.deleteEmptyFolder = deleteEmptyFolder
        self.DeleteConfigFiles = False
        self.WhiteList = []
        self.BlackList = []
    def run(self):
        for c in self.configs:
            self.textarea.appendPlainText('####################################')
            self.textarea.appendPlainText('#源项目名称是：%s.csproj'%(c.ProjectName))
            self.textarea.appendPlainText('#发布中...')
            try:
                        
                [status,  output] = publish.PublishHelper.Publish(c)
                if(status != 0):
                    self.textarea.appendPlainText('#发布出现错误，具体查看以下消息：\n%s'%(output))
                else:
                    self.textarea.appendPlainText('#项目已发布到：%s'%(c.PublishPath))
                    if(self.IsIncrement):
                        self.deleteOldFiles(c.PublishPath)
            except Exception as e:
                self.textarea.appendPlainText("%s"%(e))
            self.textarea.appendPlainText('####################################')
        self.complete.emit(True)
    def deleteFiles(self,  path):
        try:
            for root,  dirs,  files in os.walk(path):
                for f in files:
                    filepath = os.path.join(root,  f)
                    modifytime = os.path.getmtime(filepath) * 1000
                    if(modifytime < self.dateTimeBefore):
                        os.remove(filepath)
            if(self.deleteEmptyFolder):
                removeEmptyFolders(path,  False)
        except Exception as e :
            print(e)
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
        QtCore.QObject.connect(self.ui.isIncrement,  QtCore.SIGNAL("clicked()"),  self.onCheckbox_click)
        self.GeneralConfig = None
        self.Configs = []
        self.publishedPaths = []
        self._LoadDefaultConfig()
        self.ui.dateTimeBefore.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate()))
        
    def _LoadDefaultConfig(self):
        defaultPath = os.path.join(os.path.abspath('.'),  "config.ini")
        self.ui.filepathTxt.setText(defaultPath)
    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        filename = fd.getOpenFileName(self,"Open File",  "/",  "Ini File(*.ini)")
        self.ui.filepathTxt.setText(filename)
    def file_exec(self):
        self.ui.loadBtn.setEnabled(False)
        self.threads = []
        self.publishedPaths = []
        
        configs = self.getSelectedConfigs()
        if(len(configs) == 0):
            return
        
        thread = MyThread(configs,  self.ui.resultTxt, self.ui.isIncrement.isChecked(),  self.ui.deleteEmptyFolder.isChecked(),  self.ui.dateTimeBefore.dateTime().toMSecsSinceEpoch())
        thread.complete.connect(self.onPublishComplete)
        thread.start()
        self.threads.append(thread)
    def onPublishComplete(self):
        self.ui.loadBtn.setEnabled(True)
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
    def onCheckbox_click(self):
        if(self.ui.isIncrement.isChecked() ):
            self.ui.dateTimeBefore.setEnabled(True)
            self.ui.deleteEmptyFolder.setEnabled(True)
        else:
            self.ui.dateTimeBefore.setEnabled(False)
            self.ui.deleteEmptyFolder.setEnabled(False)
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
    
