# -*- coding:gb2312 -*-
from cx_Freeze import setup,Executable 
base = None
includefiles = []
packages = ["subprocess"]
includes = []
import sys
if(sys.platform == "win32"):
    base = "Win32GUI"
setup(
    name = "Publisher", 
    version = "1", 
    description = "�Զ�����c#��վ",
    options = {"build_exe": 
        {"includes":includes, "include_files": includefiles, "packages": packages}
        },
    executables = [Executable("start.py", base = base)]
)
