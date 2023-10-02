import time
import pyautogui
import os

# Request the position on the screen
print("Position the mouse where you want to click and wait")
time.sleep(3)  # Wait for 3 seconds to allow time for the click
x, y = pyautogui.position()
print(f"Position on the screen: x={x}, y={y}")

# Request the number of captures
num_captures = int(input("Enter the number of captures you want to take: "))
num_captures = num_captures - 1 # When taking the first capture, the last one is omitted

# Create a subfolder named "captures"
subfolder = "captures"
if not os.path.exists(subfolder):
    os.makedirs(subfolder)

# Wait for 3 seconds before the first capture
print("Wait for 3 seconds before the first capture...")
time.sleep(3)

# Capture the screen before the first click
initial_capture = pyautogui.screenshot()
initial_capture_path = os.path.join(subfolder, "capture_0.png")
initial_capture.save(initial_capture_path)
print("Initial capture saved in", initial_capture_path)

# Get the exact size of the initial capture
initial_capture_width, initial_capture_height = initial_capture.size

# Perform clicks and take screenshots
for i in range(num_captures):
    pyautogui.click(x, y)
    time.sleep(1)  # Wait for 1 second before taking the screenshot

    # Take a screenshot and save the image
    capture = pyautogui.screenshot()
    capture_path = os.path.join(subfolder, f"capture_{i+2}.png")
    capture.save(capture_path)
    print(f"Capture {i+1} saved in {capture_path}")

print("Process completed.")
