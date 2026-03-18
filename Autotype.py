"""
autotype.py — Automated text entry using PyAutoGUI + PyPerClip
--------------------------------------------------------------
FAIL-SAFE FEATURE:
    Move your mouse cursor to any corner of the screen to immediately
    stop the script (raises FailSafeException). Enabled by default.

UNICODE / EMOJI / BANGLA SUPPORT:
    pyautogui.typewrite() only handles ASCII. For full Unicode support
    (Bangla, emoji, etc.) we copy the text to the clipboard and paste
    it with Ctrl+V instead.

USAGE:
    1. pip install pyautogui pyperclip
    2. Run the script and follow the prompts.
    3. Quickly click into your target window before the countdown ends.
"""

import time
import pyautogui
import pyperclip

# ── Safety settings ────────────────────────────────────────────────────────────
pyautogui.FAILSAFE = True   # Move mouse to any screen corner to abort
DELAY = 0.1                 # Seconds between each action
pyautogui.PAUSE = DELAY

# ── User input ─────────────────────────────────────────────────────────────────
TEXT   = input("Enter the text to type : ")
REPEAT = int(input("How many times to repeat: "))

# ── Unicode paste helper ───────────────────────────────────────────────────────
def paste_text(text: str) -> None:
    """Copy text to clipboard, then paste — supports any Unicode character."""
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

# ── Main ───────────────────────────────────────────────────────────────────────
def main() -> None:
    print("\nStarting in 5 seconds — switch to your target window now!")
    for remaining in range(5, 0, -1):
        print(f"  {remaining}...")
        time.sleep(1)
    print("Going!\n")

    for i in range(1, REPEAT + 1):
        print(f"[{i}/{REPEAT}] Typing: {TEXT!r}")
        paste_text(TEXT)                # Paste via clipboard (Unicode-safe)
        time.sleep(DELAY)               # Short pause before Enter
        pyautogui.press("enter")       # Press Enter
        time.sleep(DELAY)               # Pause before next iteration

    print("\nDone!")

if __name__ == "__main__":
    main()