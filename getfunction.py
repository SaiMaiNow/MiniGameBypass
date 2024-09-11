import pyautogui
import re
import numpy as np
from PIL import Image
import os
import time
import win32api
import math

def Display(text):
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
    return False

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
        else:
            print("Not Found!")
            new_region = adjustRegion(r)
            if new_region:
                forcheckRegion[key] = new_region
            else:
                break
        time.sleep(0.2)
    os.system('cls')

# def calculateTargetDirection(target):
#     x, y, width, height = target
#     target_x = x + width // 2
#     target_y = y + height // 2
    
#     screen_width, screen_height = pyautogui.size()
#     center_x, center_y = screen_width // 2, screen_height // 2
    
#     delta_x = target_x - center_x
#     delta_y = target_y - center_y

#     angle_rad = math.atan2(delta_y, delta_x)

#     angle_deg = math.degrees(angle_rad)

#     if angle_deg < 0:
#         angle_deg += 360
    
#     return angle_deg

# def moveMousetoDirection(target_direction, current_direction):
#     direction_diff = target_direction - current_direction

#     if direction_diff > 180:
#         direction_diff -= 360
#     elif direction_diff < -180:
#         direction_diff += 360
    
#     screen_width, screen_height = pyautogui.size()
#     center_x, center_y = screen_width // 2, screen_height // 2
#     sensitivity = 10
    
#     if abs(direction_diff) > 0:
#         move_amount = sensitivity * (direction_diff / 180)
#         if direction_diff > 0:
#             pyautogui.moveRel(move_amount, 0, duration=0.1)  # Move right
#         else:
#             pyautogui.moveRel(-move_amount, 0, duration=0.1)  # Move left

def Farmer(reader):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        printC("[+] 1. Woodcutting")
        printM("[+] 2. to Close...")

        try:
            inputNum = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if inputNum == 1:
            Display("Woodcutting")
            while True:
                if isKeyPressed(0x14):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    printC("Press [X] to StopAutoFarm...")

                    # targetDirection = [232, 121, 48, 292]
                    # while True:
                    #     for target in targetDirection:
                    #         region = (938, 69, 46, 30) # (left, top, width, height)
                    #         currentDirection  = ReadImage(region, reader)

                    #         if currentDirection is not None:
                    #            for target in targetDirection:
                    #                 target_direction = calculateTargetDirection((target, target, 48, 292))
                    #                 moveMousetoDirection(target_direction, currentDirection)

                    #     if isKeyPressed(0x58):
                    #         break
                elif isKeyPressed(0x58):
                    break
        elif inputNum == 2:
            break
        else:
            break
