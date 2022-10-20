import pandas as pd
import time, datetime
import os
import win32com.client
import datetime
import subprocess



def win32_module():
    global Workbook
    # win32com kullanarak Excel yazılımını açma
    File = win32com.client.Dispatch("Excel.Application") 

    # Belirlenen Excel'i açma
    Workbook = File.Workbooks.open("C:/Users/mulus/OneDrive/Masaüstü/exchange.xlsx")



# def openfile():
#     prog = r"C:/Users/mulus/OneDrive/Masaüstü/exchange.xlsx"
#     try:
#         open_program = subprocess.Popen([prog])
#     except Exception as e:
#         print(e)


def stopfile():
    try:
        Workbook.Close(True)     # save the workbook
        time.sleep(2)            # 2 sec wait 
    except Exception as e:
        print(e)



def same_value():
    global is_same
    df = pd.read_excel("C:/Users/mulus/OneDrive/Masaüstü/exchange.xlsx")
    if df["Alış"].to_dict()[0] == temp:
        print("Values are equal. Program should be restart.")
        print(temp)
        stopfile()                           # Program closed and wait operation
        win32_module()                       # Program restart
    else:
        print("Successful")

        

        



def main():
    global temp
    df = pd.read_excel("C:/Users/mulus/OneDrive/Masaüstü/exchange.xlsx")
    temp = df["Alış"].to_dict()[0]
    print(temp)
    print("----------------------------------------------------")
    time.sleep(70)
    Workbook.Save()










# is_same = True
while True:
    win32_module()
    # time.sleep(3)
    main()
    same_value()

 
    



