import cv2
import numpy as np
import pyautogui

start_point = None
end_point = None
drawing = False

def draw_rectangle(event, x, y, flags, param):
    global start_point, end_point, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)

# ฟังก์ชันสำหรับเริ่ม debug mode
def start_debug_mode():
    global start_point, end_point

    screen_width, screen_height = pyautogui.size()

    # สร้างหน้าต่างที่สามารถ resize ได้
    cv2.namedWindow("Debug Mode", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Debug Mode", draw_rectangle)

    while True:
        # จับภาพหน้าจอ
        screenshot = np.array(pyautogui.screenshot())
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

        # วาดกรอบสี่เหลี่ยมที่เลือก
        if start_point and end_point:
            cv2.rectangle(screenshot, start_point, end_point, (0, 255, 0), 2)

        # แสดงภาพหน้าจอแบบเรียลไทม์
        cv2.imshow("Debug Mode", screenshot)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

    if start_point and end_point:
        # คำนวณ left, top, width, height จากจุดที่เลือก
        left = min(start_point[0], end_point[0])
        top = min(start_point[1], end_point[1])
        width = abs(end_point[0] - start_point[0])
        height = abs(end_point[1] - start_point[1])

        return (left, top, width, height)
    else:
        return None

if __name__ == "__main__":
    print("เริ่ม Debug Mode... กด 'q' เพื่อออกจากโหมด")
    region = start_debug_mode()

    if region:
        print(f"กำหนดบริเวณที่เลือก: left={region[0]}, top={region[1]}, width={region[2]}, height={region[3]}")
    else:
        print("ไม่ได้เลือกบริเวณใด ๆ")