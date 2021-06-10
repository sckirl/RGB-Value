from PIL import ImageGrab
from pymouse import PyMouse
import numpy as np
import cv2
import pygame
import keyboard

win = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Color")
clock = pygame.time.Clock()
mouse = PyMouse()
choose = True

while(True):
    if choose:
        _x, _y = mouse.position()
        _x, _y = _x*2, _y*2
    # screen capture the whole screen
    img = ImageGrab.grab(bbox=None, include_layered_windows=False) #bbox specifies specific region (bbox= left_x, top_y, right_x, bottom_y)
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    # showing cv2
    try:
        cv2.rectangle(frame, (_x, _y), (_x + 20, _y + 20), (0, 0, 255), 2)
        Rframe = cv2.resize(frame, (960, 540))
        cv2.imshow("capture", Rframe)

        # get rgb value & display
        win.fill(img.getpixel((_x, _y)))
        pygame.display.update()

        if keyboard.is_pressed('right alt'):
            choose = True
        if keyboard.is_pressed('right ctrl'):
            choose = False
            print(_x, _y)
            print(img.getpixel((_x, _y)))
    except: pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()