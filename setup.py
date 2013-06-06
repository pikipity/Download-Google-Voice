#encoding=utf-8
from distutils.core import setup
import py2exe

setup(windows=["main.py",{"script":"main.py","icon_resources":[(1,"icon//Voice.ico")]}],\
      data_files=[\
    ("icon",["icon//Voice.ico"]),\
    ("store",[])])
