import pyautogui
import re
import numpy as np
from PIL import Image
import os
import time

def ReadImage(region, reader):
    left, top, width, height = region
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    img_np = np.array(screenshot)
    img_rgb = Image.fromarray(img_np, 'RGB')
    results = reader.readtext(np.array(img_rgb))

    numbers = []
    for result in results:
        text = result[1]
        found_numbers = re.findall(r'\d+', text)
        for number in found_numbers:
            digits = [int(digit) for digit in number]
            numbers.extend(digits)

    return numbers

def Electrical(reader):
    forcheckRegion = {
        1: (536, 799, 91, 130),
        2: (643, 799, 91, 130),
        3: (755, 799, 91, 130),
        4: (863, 799, 91, 130),
        5: (971, 799, 91, 130),
        6: (1079, 799, 91, 130),
        7: (1186, 799, 91, 130),
        8: (1291, 799, 91, 130),
    }

    region = (664, 742, 86, 124) # (left, top, width, height)
    checkMain = ReadImage(region, reader)
    for key, r in forcheckRegion.items():
        numbers = ReadImage(r, reader)
        if numbers:
            fonudNum = False
            for i in checkMain:    
                print(numbers[0], i)        
                if i == numbers[0] :
                    print("--->")
                    fonudNum = True
                    break
                else:
                    print("<---")
            if fonudNum:
                pyautogui.press('right')
            else:
                pyautogui.press('left') 
        else:
            print("Not Found!")
        time.sleep(0.3)
    os.system('cls')

# def CompareColors(region):
#     left, top, width, height = region
#     screenshot = pyautogui.screenshot(region=(left, top, width, height))

#     rgb = '#1986b4'

#     img_np = np.array(screenshot)
#     img_rgb = Image.fromarray(img_np, 'RGB')

#     return 

# def Electricboard():
    # forcheckRegion = {
    #     1: (739, 756, 43, 13),
    #     2: (811, 758, 43, 13),
    #     3: (880, 758, 43, 13),
    #     4: (811, 677, 43, 13),
    # }

    # for key, r in forcheckRegion.items():
    #     ButtonOn = CompareColors(r)

    #     if key == 1 & ButtonOn:
    #         pyautogui.press('right')