import time
from pynput.keyboard import Key, Controller

time.sleep(2.0) # just adding a small delay in the beginning
keyboard_controller = Controller()

i = 0
while i<100:
    keyboard_controller.press('a') # Simulate pressing the 'a' key
    keyboard_controller.release('a') # Simulate releasing the 'a' key
    i+=1
    time.sleep(0.1) # add a small delay (in seconds) between key presses
keyboard_controller.press('b') # Simulate pressing the 'b' key

keyboard_controller.press(Key.left) # Simulate pressing the left key
keyboard_controller.press(Key.left) # Simulate pressing the left key

