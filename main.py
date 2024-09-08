import easyocr
import os
import time
import winsound
import win32api
import sys

from getfunction import Electrical

def Display():
    os.system('cls' if os.name == 'nt' else 'clear')
    printC("[+] 1. ElectricalRepair")
    printM("[+] 2. Electricboard")
    printM("[+] 3. to Close...")

def Display2(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    printC(f"Press [CapsLoack] {text}")
    printM("Press [X] to Close...")

def printC(text):
    columns, rows = os.get_terminal_size()
    text_length = len(text)
    padding_horizontal = (columns - text_length) // 2
    padding_vertical = (rows - 1) // 2 
    centered_text = ' ' * padding_horizontal + text
    for _ in range(padding_vertical):
        print()
    print(centered_text)

def printM(text):
    columns, _ = os.get_terminal_size()
    text_length = len(text)
    padding = (columns - text_length) // 2
    centered_text = ' ' * padding + text
    print(centered_text)

def isKeyPressed(vk_code):
    state = win32api.GetAsyncKeyState(vk_code)
    return state & 0x8000 != 0

def stated(reader):
    Display()
    while True:
        inputNum = int(input("Enter a number: "))
        if inputNum == 1:
            print("Found!")
            time.sleep(0.1)
            Display2("ElectricalRepair")
            while True:
                if isKeyPressed(0x14):
                    Electrical(reader)
                    Display2("ElectricalRepair")
                elif isKeyPressed(0x58):
                    Display()
                    break
        elif inputNum == 2:
            print("Found!")
            time.sleep(0.1)
            Display2("Electricboard")
            while True:
                if isKeyPressed(0x14):
                    # Electricboard()
                    Display2("Electricboard")
                elif isKeyPressed(0x58):
                    Display()
                    break
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

if __name__ == "__main__":
    os.system('cls')
    printC("Loading...")
    reader = easyocr.Reader(['en'], gpu=True)
    os.system('cls')
    winsound.Beep(750, 300)
    printC("RCN loaded successfully.\n")
    time.sleep(1)
    print("Ok")
    time.sleep(0.7)
    os.system('cls')
    stated(reader)