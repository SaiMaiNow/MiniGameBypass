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

def adjustRegion(region):
    left, top, width, height = region
    if width < 130:
        width += 10  # Increase width by 10 units
        return (left, top, min(width, 130), height)
    return region

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

    region = (664, 742, 90, 130) # (left, top, width, height)
    checkMain = ReadImage(region, reader)
    keys = list(forcheckRegion.keys())
    index = 0
    indexC = 0
    while index < len(keys):
        key = keys[index]
        r = forcheckRegion[key]
        numbers = ReadImage(r, reader)
        if numbers:
            foundNum = False
            for i in checkMain:
                print(numbers[0], i)
                if i == numbers[0] :
                    print("--->")
                    foundNum = True
                    break
                else:
                    print("<---")
                    
            if foundNum:
                pyautogui.press('right')
            else:
                pyautogui.press('left') 
            
            index += 1
            indexC = 0
        else:
            print("Not Found!")
            new_region = adjustRegion(r)
            forcheckRegion[key] = new_region
            indexC += 1
            if indexC <= 20:
                index += 1
        time.sleep(0.3)


    # for key, r in forcheckRegion.items():
    #     numbers = ReadImage(r, reader)
    #     if numbers:
    #         fonudNum = False
    #         for i in checkMain:    
    #             print(numbers[0], i)        
    #             if i == numbers[0] :
    #                 print("--->")
    #                 fonudNum = True
    #                 break
    #             else:
    #                 print("<---")
    #         if fonudNum:
    #             pyautogui.press('right')
    #         else:
    #             pyautogui.press('left') 
    #     else:
    #         print("Not Found!")
    #         new_region = adjust_region(r)
    #         forcheckRegion[key] = new_region

    #     time.sleep(0.3)
    os.system('cls')

def HomeRepairs():
    print("HomeRepairs")