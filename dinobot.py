import pyautogui
import time

def detect_obstacle():
    pixel = pyautogui.pixel(830, 302)
    if pixel == (83, 83, 83) or pixel == (172, 172, 172):
        return True
    else:
        return False

def jump():
    pyautogui.press('space')

def main():
    print("Automated Chrome Dino Game is starting in 3 seconds...")
    time.sleep(3)
    while True:
        if detect_obstacle():
            jump()

if __name__ == "__main__":
    main()



