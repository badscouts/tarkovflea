import keyboard
from PIL import Image
import pytesseract
import pyautogui
import re
import time
import platform

# Specify the path to the tesseract executable if needed
# For example, on Windows:
if platform.system() == 'Windows':
    pytesseract.pytesseract.tesseract_cmd = r'*\Tesseract-OCR-Windows\tesseract.exe'
else:
    pytesseract.pytesseract.tesseract_cmd = r'*\Tesseract-OCR-Linux\tesseract'

def capture_and_read_text():
    global text

    # Define the region to capture (left, top, width, height)
    region = (1785, 210, 214, 48)  # Adjust these values as needed

    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region)

    # Perform OCR on the captured screenshot
    text = pytesseract.image_to_string(screenshot)

    # Print the extracted text
    # Remove 'P' from the end of the text if it exists
    text = re.sub(r'\D', '', text)
    print("Extracted Text:", text)
    return text

# Set up the hotkey listener


def integer_to_keys(number):
    keys = '+'.join(str(digit) for digit in str(number))
    return keys

''''
def input_price():
    pyautogui.click(1004, 846)
    time.sleep(2)
    number = int(text)
    #print("extracted number", number)
    number -= 1000
    #print("extracted number 2", number)
    keys = integer_to_keys(number)
    print(number)
    keyboard.press_and_release(keys)
'''


# Function to input the price
def input_price(event=None):  # Accept an optional event argument
    text = capture_and_read_text()  # Call the function to get the extracted text
    pyautogui.click(1004, 846)
    if text:
        number = int(text)
        number -= 1000
        keys = str(number)
        print("Keys:", keys)
        for key in keys:
            keyboard.press_and_release(key)

'''
def find_text_on_screen(x, y, w, h, text_to_find = "FILTER BY ITEM"):
    screenshot = pyautogui.screenshot()
    ocr_data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)

    for i, text2 in enumerate(ocr_data['text']):
        if text_to_find in text2:
            x, y, w, h = ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i]

            print(f"Found '{text_to_find}' at ({x}, {y}, {w}, {h})")
            #return x, y, w, h
        else:
            print(f"Text '{text_to_find}' not found on screen.")
    #return None
'''
def find_text_on_screen(x, y, w ,h, word_to_find = "FILTER BY ITEM"):
    text_filter = ''

    # Define the region to capture (left, top, width, height)
    region = (x, y, w, h)  # Adjust these values as needed
    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region)
    # Perform OCR on the captured screenshot
    text_filter = pytesseract.image_to_string(screenshot)
    #print(text_filter)
    if word_to_find in text_filter:
        print("WORD FOUND")
    else:
        print("Word not found")
    return text_filter


def test(event=None):
    find_text_on_screen(0, 343, 1480, 1096, "FILTER BY ITEM")

def click_on_sell():
    pyautogui.click(1173, 1351)


def combined(event=None):
    pyautogui.click()
    capture_and_read_text()
    input_price()
    click_on_sell()


keyboard.add_hotkey('F10', capture_and_read_text)
keyboard.on_release_key('F9', input_price)
keyboard.add_hotkey('F8', click_on_sell)
keyboard.on_release_key('F7', combined)
keyboard.on_release_key('F3', test)

print("Press F10 to capture the screen region and perform OCR.")
print("Press F9 to input price.")
print("Press F8 to click on the sell button.")
print("Press F7 to do all at once")
print("Press F3 to check for filter")
keyboard.wait('shift+esc')  # You can change this to another key to exit the script