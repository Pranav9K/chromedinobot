import pyautogui
import time


target_coordinate = (286, 475)  
target_color = (83, 83, 83)  


def is_target_color(coord):
    actual_color = pyautogui.pixel(coord[0], coord[1])
    return actual_color == target_color


try:
    while True:
        if is_target_color(target_coordinate):
            pyautogui.press('space')
            print("Space key pressed!")
            time.sleep(0.01) 
except KeyboardInterrupt:
    print("Script terminated by user.")



