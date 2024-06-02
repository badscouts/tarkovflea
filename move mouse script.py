import pyautogui

print("Move your mouse cursor to the top-left corner of the region you want to capture and press Enter.")
input()

# Get the top-left corner coordinates
x1, y1 = pyautogui.position()

print(f"Top-left corner position: ({x1}, {y1})")

print("Move your mouse cursor to the bottom-right corner of the region you want to capture and press Enter.")
input()

# Get the bottom-right corner coordinates
x2, y2 = pyautogui.position()

print(f"Bottom-right corner position: ({x2}, {y2})")

# Calculate the left, top, width, and height of the region
left = min(x1, x2)
top = min(y1, y2)
width = abs(x2 - x1)
height = abs(y2 - y1)

print(f"Region: Left: {left}, Top: {top}, Width: {width}, Height: {height}")

# Now you have the coordinates and dimensions of the region to capture


