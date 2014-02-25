# -*- coding:gb2312 -*-
###########################################################################################
'''
@author: Tian Zhiyuan
@brief: 自动发布c#项目：可以自动完成svn更新、网站项目发布、打包工作
@version: 1.0
@attention: 只支持VS2012环境+Python3.x
@todo: 配置提到外部配置文件中
@history:
    2013/8/28:  现在可以使用ini配置文件来自动发布
    2013/12/7:  如果发布目标路径不存在，则自动创建
                重构代码
                增加简单的GUI
                重新加入压缩功能
'''
##########################################################################################
import os
import time

from configparser import *
import sys
def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    import sys
    mswindows = (sys.platform == "win32")
    import os
    if (not mswindows):
        cmd = '{' + cmd + ';}'
    pipe = os.popen(cmd + ' 2>&1',  'r')
    text = pipe.read()
    status = pipe.close()
    if(status is None):
        status = 0
    if(text[-1:0] == '\n'):
        text = text[:-1]
    return status,  text
class PublishConfig:
    def __init__(self, prjName = "", prjPath = "", publishPath = "", enabled = True, compileType = 'Release'):
        self.CompileType = compileType;
        self.ProjectPath = prjPath;
        self.PublishPath = publishPath;
        self.ProjectName = prjName;
        self.Enabled = enabled;
class GeneralConfig:
    def __init__(self,  svnpaths = [],  doZip = False,  dstPath = ""):
        self.SvnPaths = svnpaths
        self.DoZip = doZip
        self.ZipPath = dstPath
def pathExists(path):
    return os.path.exists(path);

class PublishHelper:
    @staticmethod
    def Publish(config):
        if(not config.Enabled):
            return;
        #检查目标发布路径是否存在，如果不存在，则创建
        if(not pathExists(config.PublishPath)):
           os.makedirs(config.PublishPath);
        
        #生成目标cmd
        cmd = [
            r'call "%VS110COMNTOOLS%\vsvars32.bat" ',
            r'IF EXIST "%s" RD /S /Q "%s"'%(config.PublishPath, config.PublishPath),
            r'MSBuild "%s\%s.csproj" /p:Configuration=%s'%(config.ProjectPath, config.ProjectName, config.CompileType),
            r'MSBuild "%s\%s.csproj" /target:_CopyWebApplication  /property:OutDir=%s\ /property:WebProjectOutputDir=%s  /p:Configuration=%s'%(
			config.ProjectPath, config.ProjectName, config.PublishPath, config.PublishPath, config.CompileType),
            r'xcopy "%s\bin\*.*" "%s\bin\" /k /y'%(config.ProjectPath, config.PublishPath)
        ];
        command = '&&'.join(cmd);
        return getstatusoutput(command)
    @staticmethod
    def RemoveUnusedSections(filename):
        newfile = 'web.config.new'
        import shutil
        a_write = True
        b_write = True
        with open(filename, 'r', -1, 'UTF-8') as f:
            with open(newfile, 'w', -1, 'UTF-8') as g:
                for line in f.readlines():
                    a_old = a_write
                    b_old = b_write
                    if '<httpHandlers>' in line:
                        a_write = False
                    if '</httpHandlers>' in line:
                        a_write = True
                    if '<httpModules>' in line:
                        b_write = False
                    if '</httpModules>' in line:
                        b_write = True
                    if a_write and b_write and a_old and b_old:
                        g.write(line)
        shutil.move(newfile, filename)
    @staticmethod
    def ReadConfigFromFile(filename):
        if(not os.path.exists(filename)):
            return [];
        reader = ConfigParser();
        file = open(filename)
        reader.read_file(file)
        sections = reader.sections();
        configs = []
        for section in sections:
            if ("Project" in section):
                opts = reader.options(section)
                config = PublishConfig()
                for opt in opts:
                    if(opt == "name"):
                        config.ProjectName = reader.get(section, opt);
                    elif(opt == "path"):
                        config.ProjectPath = reader.get(section, opt);
                    elif(opt == "publishpath"):
                        config.PublishPath = reader.get(section, opt)
                    elif(opt == "type"):
                        config.CompileType = reader.get(section, opt)
                    elif(opt == "enabled"):
                        config.Enabled = reader.getboolean(section, opt)
                configs.append(config)
        return configs
    @staticmethod
    def ReadGeneralConfigFromFile(filename):
        if(not os.path.exists(filename)):
            return None;
        reader = ConfigParser();
        file = open(filename)
        reader.read_file(file)
        sections = reader.sections();
        svnpaths = []
        config = GeneralConfig()
        for section in sections:
            if(section == "General"):
                opts = reader.options(section)
                for opt in opts:
                    if("svnpath" in opt):
                        svnpaths.append(reader.get(section, opt))
                    elif("zip" == opt):
                        config.DoZip = reader.getboolean(section,  opt)
                    elif("zippath" == opt):
                        config.ZipPath = reader.get(section,  opt)
        config.SvnPaths = svnpaths
        return config
    @staticmethod
    def ProcessGeneralConfig(config):
        for path in config.SvnPaths:
            os.system("svn update %s"%(path))
    @staticmethod
    def ZipFile(srcPath, prjName,  dstPath):
        if(not os.path.exists(srcPath)):
            return
        if(not os.path.exists(dstPath)):
            os.makedirs(dstPath)
        import zipfile
        v_str = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
        zipfilename = os.path.join(dstPath,  "%s[%s].zip"%(prjName,  v_str))
        filelist = []
        if os.path.isfile(srcPath):
            filelist.append(srcPath)
        else :
            for root, dirs, files in os.walk(srcPath):
                for name in files:
                    filelist.append(os.path.join(root, name))
        
        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(srcPath):]
            zf.write(tar,arcname)
        zf.close()

#deprecated        
class Project:
    def __init__(self, name, src_path, dst_path, config = 'Release'):
        self.Name = name
        self.Source = src_path
        self.IIS_Path = dst_path
        self.Config = config
    def release(self):
        if(not pathExists(self.IIS_Path)):
            os.makedirs(self.IIS_Path);
        cmd = [
            r'call "%VS110COMNTOOLS%\vsvars32.bat" ',
            r'IF EXIST "%s" RD /S /Q "%s"'%(self.IIS_Path, self.IIS_Path),
            r'MSBuild "%s\%s.csproj" /p:Configuration=%s'%(self.Source, self.Name, self.Config),
            r'MSBuild "%s\%s.csproj" /target:_CopyWebApplication  /property:OutDir=%s\ /property:WebProjectOutputDir=%s  /p:Configuration=%s'%(
			self.Source, self.Name, self.IIS_Path, self.IIS_Path, self.Config),
            r'xcopy "%s\bin\*.*" "%s\bin\" /k /y'%(self.Source, self.IIS_Path)
        ]
        command = '&&'.join(cmd)
        #print(command)
        os.system(command)
        return True
	
    def proc_config(self):
        filename = '%s\\%s'%(self.IIS_Path, 'Web.config')
        newfile = '%s\\%s.new'%(self.IIS_Path, 'Web.config')
        import shutil
        a_write = True
        b_write = True
        with open(filename, 'r', -1, 'UTF-8') as f:
            with open(newfile, 'w', -1, 'UTF-8') as g:
                for line in f.readlines():
                    a_old = a_write
                    b_old = b_write
                    if '<httpHandlers>' in line:
                        a_write = False
                    if '</httpHandlers>' in line:
                        a_write = True
                    if '<httpModules>' in line:
                        b_write = False
                    if '</httpModules>' in line:
                        b_write = True
                    if a_write and b_write and a_old and b_old:
                        g.write(line)
        shutil.move(newfile, filename)
    def zip(self, dir_path):
        v_str = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
        f_name = '%s\\%s[%s].zip'%(dir_path,self.Name, v_str)
        file = zipfile.ZipFile(f_name, 'w', zipfile.ZIP_DEFLATED)
        #print([f_name, self.IIS_Path])
        self.__zip_dir(self.IIS_Path, f_name)
    def __zip_dir(self,dirname, zipfilename):
        filelist = []
        if os.path.isfile(dirname):
            print('is file')
            filelist.append(dirname)
        else :
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    #print(name)
                    filelist.append(os.path.join(root, name))
        
        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            #print(tar)
            arcname = tar[len(dirname):]
            #print arcname
            zf.write(tar,arcname)
        zf.close()
#deprecated
def build_task():
    # SVN 路径
    SVN_PATH = 'G:\Product_9_26'
    
    # 发布之后网站打包到的该路径文件夹下
    ZIP_PATH = r'G:\Publish'
    
    # WebService工程名称
    WEBSERVICE_PROJECT_NAME = r'DBC.Ors.Services.Web.Host'
    
    # WebService工程路径
    WEBSERVICE_PROJECT_PATH = r'G:\Projects\太平鸟\DBC.Ors.Services.Web.Host'
    
    # WebService工程发布路径
    WEBSERVICE_PUBLISH_PATH = r'G:\Publish\WebService'
    
    # ERP工程名称
    ERP_PROJECT_NAME = r'DBC.Ors.UI.Web.Mvc.ERP'
    
    # ERP工程路径
    ERP_PROJECT_PATH = r'G:\Projects\太平鸟\DBC.Ors.UI.Web.Mvc.ERP'
    
    # ERP工程发布路径
    ERP_PUBLISH_PATH = r'G:\Publish\ERP'


    # 1. 更新工程文件
    #state = os.system('svn update ' + SVN_PATH)
    #if state != 0:
        #exit(1)
##        state = os.system('svn cleanup' + SVN_PATH)
##        if(state != 0):
##            exit(1)
##        else:
##            state = os.system('svn update' + SVN_PATH)
##            if(state != 0):
##                exit(2)
    # 2. 创建WebService 工程实例
    webService = Project(WEBSERVICE_PROJECT_NAME ,WEBSERVICE_PROJECT_PATH ,WEBSERVICE_PUBLISH_PATH,'Debug')
    # 3. WebService工程发布
    if webService.release():
        pass
        # 3.1 处理config文件（删除 httpHandlers 和httpModules）
        #webService.proc_config();
        # 3.2 打包发布网站
        #webService.zip(ZIP_PATH)
    # 4. 创建ERP 工程实例
    erp = Project(ERP_PROJECT_NAME ,ERP_PROJECT_PATH ,ERP_PUBLISH_PATH)
    # 5. ERP 网站发布
    if erp.release():
        pass
        # 5.1 打包ERP网站
        #erp.zip(ZIP_PATH)
#deprecated
class ConfigReader:
    def __init__(self, filename):
        self.FileName = filename
        self.inited = False
        self.handler = None
        self.config = None
        self.Init()
    def Init(self):
        self.config = ConfigParser()
        self.file = open(self.FileName)
        self.config.read_file(self.file)
        self.inited = True
        return self.inited
    def Destroy(self):
        if(self.inited):
            self.file.close()
    def GetValue(self, Section, Key, Default=""):
        try:
            value = self.config.get(Section,Key)
        except:
            value = Default
        return value
    def __del__(self):
        self.Destroy()
    def SectionIterator(self,handler):
        sections = self.config.sections()
        for section in sections:
            handler(section)
#deprecated
def ReadFromConfig(filename):
    reader = ConfigReader(filename)
    svnpaths = []
    projects = []
    for section in reader.config.sections():
        if(section == "General"):
            options = reader.config.options(section)
            for option in options:
                if("svnpath" in option):
                    svnpaths.append(reader.GetValue(section, option))
        elif("Project" in section):
            options = reader.config.options(section)
            name = ""
            path = ""
            publishPath = ""
            config = 'Release'
            for option in options:
                if(option == "name"):
                    name = reader.GetValue(section, option)
                elif(option == "path"):
                    path = reader.GetValue(section, option)
                elif(option=="publishpath"):
                    publishPath = reader.GetValue(section, option)
                elif(option=="config"):
                    config = reader.GetValue(section, option)
                    if(config==''):
                        config='Release'
            projects.append(Project(name ,path ,publishPath,'Debug'))
    for path in svnpaths:
        os.system('svn update ' + path)
    for project in projects:
        project.release()


if __name__ == '__main__':
    path = "E:\Publish\WebService"
    PublishHelper.ZipFile(path,  "aaa",  "E:\Publish\WebService")
    
