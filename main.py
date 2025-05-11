from multiprocessing import Value
import time
import pyautogui
import os
from dotenv import load_dotenv

load_dotenv()

GMAIL_URL = "https://mail.google.com/"
SLOWDOWN_DURATION = 0.01 # seconds
EMAILS = os.getenv("EMAIL_LIST")

def open_webbrowser():
    # Open brave
    pyautogui.press("win")
    pyautogui.write("brave")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

    # Open browser in incognito
    pyautogui.hotkey("ctrlleft", "shiftleft", "n")
    time.sleep(2)


def locate_on_screen(image):
    found = False
    tries = 0

    while not found and tries <= 5:
        try:
            location = pyautogui.locateOnScreen(image, confidence=0.9)
            return location
        except pyautogui.ImageNotFoundException:
            tries += 1

    return None

def login(email: str) -> None:
    print(f"Logging into: {email}")
    open_webbrowser()

    pyautogui.write(GMAIL_URL)
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.typewrite(email, interval=SLOWDOWN_DURATION)
    pyautogui.press("enter")
    time.sleep(2)

    continue_location = locate_on_screen("./assets/continue_button.png")
    if continue_location:
        pyautogui.moveTo(continue_location)
        pyautogui.click()
        time.sleep(1)
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(5)
    pyautogui.hotkey("ctrl", "w")
    pyautogui.hotkey("ctrl", "w")


def main():
    pyautogui.FAILSAFE = True
    input("Please login to bitwarden before beginning... (press enter when ready)")

    if EMAILS is None:
        raise ValueError("EMAIL_LIST enviornment variable is empty or missing.")
    
    for email in EMAILS.split(','):
        login(email)
    
    
if __name__ == "__main__":
    main()