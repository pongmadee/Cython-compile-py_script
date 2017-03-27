# Python script will be translated python code to pyd by Microsoft C/C++ compiler x64 (Visual Studio Community 2015).
#
# Information : 
# http://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compilation
# https://en.wikipedia.org/wiki/Cython
#
# Software:
# OS : Windows10 64-bit Version 1607
# Anaconda 4.3(Python 3.6, Cython 0.25.2) 64-bit For Windows 64-bit
# Compiler : Microsoft C/C++ compiler x64 ( Visual Studio 2015 Community Based on 64-bit)
# 
# Step by step:
# 1.Set path for RC.exe --> "C:\Program Files (x86)\Windows Kits\10\bin\x64"
# 2.Set path for Compiler CL.exe --> "F:\software\vs2015\VC\bin\amd64" (default: "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\amd64")
# 3.Command for compile: python setup.py build_ext --inplace
#

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

#Include header
ucrt_include = r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.10586.0\ucrt'
shared_include = r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.10586.0\shared'
vc_include = r'F:\software\vs2015\VC\include'  # default: "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include"

#Library
ucrt_lib = r'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10586.0\ucrt\x64'
um_lib = r'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10586.0\um\x64'
msvcrt_lib = r'F:\software\vs2015\VC\lib\amd64' # default: "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\amd64"

ext = Extension("hello", ["hello.pyx"],
                include_dirs=[ucrt_include ,shared_include ,vc_include], library_dirs=[ucrt_lib ,msvcrt_lib ,um_lib])
setup(
  name = 'Hello world app',
  ext_modules = cythonize([ext])
)
