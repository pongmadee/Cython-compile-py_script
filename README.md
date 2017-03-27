# Cython: How to compile with python script for Windows10
Python script will be translated python code to pyd by Microsoft C/C++ compiler x64 (Visual Studio Community 2015).

# Information : 
http://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compilation
https://en.wikipedia.org/wiki/Cython

# Software:
OS : Windows10 64-bit Version 1607

Anaconda 4.3(Python 3.6, Cython 0.25.2) 64-bit For Windows 64-bit

Compiler : Microsoft C/C++ compiler x64 ( Visual Studio 2015 Community Based on 64-bit)

# Step by step:
1.Set path for RC.exe --> "C:\Program Files (x86)\Windows Kits\10\bin\x64"

2.Set path for Compiler CL.exe --> "F:\software\vs2015\VC\bin\amd64" (default: "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\amd64")

3.Command for compile: python setup.py build_ext --inplace

