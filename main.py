import easyocr
import os
import time
import winsound
import sys
import torch
import warnings
import ctypes

from getfunction import Electrical, Farmer, printC, printM, isKeyPressed, Display

warnings.filterwarnings('ignore')

def stated(reader):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        printC("[+] 1. ElectricalRepair")
        printM("[+] 2. FarmerMake")
        printM("[+] 3. to Close...")

        try:
            inputNum = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if inputNum == 1:
            print("Found!")
            time.sleep(0.1)
            Display("ElectricalRepair")
            while True:
                if isKeyPressed(0x14):
                    Electrical(reader)
                    Display("ElectricalRepair")
                elif isKeyPressed(0x58):
                    break
        elif inputNum == 2:
            time.sleep(0.1)
            Farmer(reader)
        elif inputNum == 3:
            for i in range(20):
                print("ERROR")
                os.system('cls')
                time.sleep(0.3)
            winsound.Beep(750, 300)
            sys.exit(0)
        else:
            for i in range(20):
                print("ERROR")
                os.system('cls')
                time.sleep(0.3)
            winsound.Beep(750, 300)
            sys.exit(0)
        time.sleep(0)

def ProjectSetUp():
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    hwnd = kernel32.GetConsoleWindow()
    if hwnd:
        user32.SetWindowTextW(hwnd, "RCN | first project")
        user32.SetWindowLongW(hwnd, -20, user32.GetWindowLongW(hwnd, -20) | 0x80000) 
        user32.SetLayeredWindowAttributes(hwnd, 0, 255, 0x00000001)
        GWL_STYLE = -16
        WS_MAXIMIZEBOX = 0x00010000
        WS_THICKFRAME = 0x00040000
        WS_SYSMENU = 0x00080000
        WS_CAPTION = 0x00C00000
        current_style = user32.GetWindowLongW(hwnd, GWL_STYLE)
        user32.SetWindowLongW(hwnd, GWL_STYLE, current_style & ~WS_MAXIMIZEBOX & ~WS_THICKFRAME & ~WS_SYSMENU)
        user32.SetWindowPos(hwnd, None, 100, 100, 800, 600, 0x0040)
    else:
        print("ERROR Hwnd")

if __name__ == "__main__":
    os.system('cls')
    ProjectSetUp()
    printC("Loading...")
    reader = easyocr.Reader(['en'], gpu=True)
    os.system('cls')
    winsound.Beep(750, 300)
    printC("RCN loaded successfully.")
    printM(f"CUDA Available: {torch.cuda.is_available()}")
    printM(f"Number of GPUs: {torch.cuda.device_count()}")
    time.sleep(1)
    print("Ok")
    time.sleep(0.7)
    os.system('cls')
    stated(reader)