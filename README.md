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

1. Install dependencies:
   ```bash
   pip install pyautogui python-dotenv pillow
   ```
2. Create a `.env` file in the root directory and define your emails using the EMAIL_LIST variable:
   ```.env
   EMAIL_LIST=johndoe@gmail.com,janedoe@gmail.com,johnsmith@gmail.com
   ```
3. Make sure your .env file is not tracked by git
   ```.gitignore
   .env
   ```

## How to Use
1. Run the script:
   ```bash
   python main.py
   ```
2. When prompted, ensure you are logged into Bitwarden and press `Enter` to continue.
3. The script will open an incognito window in Brave, navigate to Gmail, and log into each email listed in the .env file
