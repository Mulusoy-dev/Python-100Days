import os
import subprocess
import time

def openfile():
    global open_program
    prog = r"C:/Program Files (x86)/Dev-Cpp/devcpp.exe"
    try:
        open_program = subprocess.Popen([prog])
    except Exception as e:
        print(e)

def stopfile():
    prog = r"C:/Program Files (x86)/Dev-Cpp/devcpp.exe"
    try:
        open_program.terminate()
    except Exception as e:
        print(e)

while 1:
    openfile()
    time.sleep(5)
    stopfile()
