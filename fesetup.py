#!/usr/bin/env python 
# -*- coding: cp936 -*-
#�÷� fesetup.py build
import sys;
from cx_Freeze import setup, Executable;
 
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages"  : ["os"],
    #"includes": ["PIL"],
    # "path"      : "",
    "icon"      : "f3.ico",
     
};
#�Լ��ӵ�
new1={'includes':'atexit'}
 
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
 
setup(  name = "liuyao",
        version = "1.0",
        description = u"��س�������",
        options = {"build_exe": build_exe_options},
        executables = [Executable('liuyao.py', base=base)])
