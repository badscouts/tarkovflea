import keyboard
from PIL import Image
import pytesseract
import pyautogui
import re # Test
import time
import os
'''
current_directory = os.getcwd()

if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = current_directory + r'\Tesseract-OCR-Windows\tesseract.exe'
else:
    pytesseract.pytesseract.tesseract_cmd = r'\Tesseract-OCR-Linux\tesseract'
'''

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_and_read_text():
    global text

    # Define the region to capture (left, top, width, height)
    region = (1305, 374, 128, 29)  # Adjust these values as needed

    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region)

    # Perform OCR on the captured screenshot
    text = pytesseract.image_to_string(screenshot)

    # Print the extracted text
    # Remove 'P' from the end of the text if it exists
    text = re.sub(r'\D', '', text)
    print("Extracted Text:", text)
    return text

print("Press F10 to capture the screen region and perform OCR.")
keyboard.add_hotkey('F10', capture_and_read_text)
while True:
    capture_and_read_text()


