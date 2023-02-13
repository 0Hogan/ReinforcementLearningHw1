"""
File: venv_setup.py

Purpose:
This file is used to create a .venv in the root of
this project, and import the necessary requirements.

This file can be executed locally from the root directory.

Example:

ReinforcementLearningHw1# python ./quality/venv_setup.py


Process:
After executing this script, be sure to update your
python path to the location of python, which is installed
in .venv, note that VSCode should automatically detect
the .venv once it is created.
"""
import os
import platform


if __name__ == '__main__':
    print('\nExecuting Virtual Environment Setup\n')

    if platform.system() == 'Linux':
        print('\nLinux Virtual Environment Setup\n')
        os.system("sudo python3.9 -m venv .venv")
        os.system("sudo .venv/bin/python3.9 -m pip install --upgrade pip")
        os.system("sudo .venv/bin/python3.9 -m pip install -r quality/requirements.txt")

    if platform.system() == 'Windows':
        print('\nWindows Virtual Environment Setup\n')
        os.system("python -m venv .venv")
        os.system(".\\.venv\\Scripts\\python -m pip install  --upgrade pip")
        os.system(".\\.venv\\Scripts\\python -m pip install -r quality\\requirements.txt")
