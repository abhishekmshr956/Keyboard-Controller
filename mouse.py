import time 
from pynput.mouse import Controller

mouse_controller = Controller()

# set the movement direction (1 for right, -1 for left)
movement_direction = 1

i = 0
while i<1000:
    # move the cursor by a certain amount in the chosen direction
    mouse_controller.move(movement_direction * 10, 0)
    i += 1

    # add a small delay between movements
    time.sleep(0.1)

# # Move the mouse cursor left and right in a loop

# for _ in range(100):
#     mouse_controller.move(-50, 0) # Move left by 50 pixels
#     time.sleep(0.5) # Add a delay between movements
#     mouse_controller.move(50, 0) # //Move right by 50 pixels
#     time.sleep(0.5) # Add a delay between movements