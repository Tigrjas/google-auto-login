# Google Auto Login

A Python script that automates logging into multiple Google accounts.  
The purpose of this script is to prevent account deletion due to inactivity by periodically signing into each account.

---

## Requirements

- [Bitwarden](https://bitwarden.com/) must be set up with the passkeys or login credentials for each account.
- All target Google accounts should have passkey login enabled and configured in Bitwarden.
- This script uses `pyautogui` to control your browser, so make sure your display is not locked or asleep while it's running.

---

## Setup

1. Create a virtual environment and then install dependencies using `requirements.txt`:
   ```bash
   python3 -m venv .venv
   pip install -r requirements.txt
   ```
2. Populate `emails.txt` with your emails, making sure that each email is on a new line
   ```txt
   johndoe@gmail.com
   janedoe@gmail.com
   johnsmith@gmail.com
   ```

## How to Use
1. Run the script:
   ```bash
   python main.py
   ```
2. When prompted, ensure you are logged into Bitwarden and press `Enter` to continue.
3. The script will open an incognito window in Brave, navigate to Gmail, and log into each email listed in the emails.txt file
