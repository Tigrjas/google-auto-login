from typing import List
import time
import pyautogui

GMAIL_URL = "https://mail.google.com/"
SLOWDOWN_DURATION = 0.01 # seconds
EMAILS_FILE_NAME = "emails.txt"

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

def get_emails() -> List[str]:
    try:
        with open(EMAILS_FILE_NAME, 'r') as file:
            file_contents = file.readlines()
            return [line.rstrip('\n') for line in file_contents]
    except FileNotFoundError:
        return []
    

def main():
    pyautogui.FAILSAFE = True
    input("Please login to bitwarden before beginning... (press enter when ready)")
    
    emails = get_emails()
    for email in emails:
        login(email)

    
if __name__ == "__main__":
    main()