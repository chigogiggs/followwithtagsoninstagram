import cx_Freeze
import pygame
import sys


base = None


if sys.platform == 'win32':
    base = "Win32GUI"

executables=[cx_Freeze.Executable("DatabaseClass.py",base=base)]
cx_Freeze.setup(name='chat_app',
                options={"build_exe":{"packages": ["tkinter","MySQLdb","time","uuid","hashlib","socket","threading","PIL"],
                                      "include_files":["chatgirlgif.gif","tick.jpg","circle.png","avatar.jpg"]}},
                version="0.01",
                description="Chat with friends",
                executables = executables
      )


"""
from cx_Freeze import setup, Executable
import sys

productName = "ProductName"
if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\InstallDir\\' + productName]
    sys.argv += ['--install-script', 'install.py']

exe = Executable(
      script="main.py",
      base="Win32GUI",
      targetName="Product.exe"
     )
setup(
      name="Product.exe",
      version="1.0",
      author="Me",
      description="Copyright 2012",
      executables=[exe],
      scripts=[
               'install.py'
               ]
      )
"""