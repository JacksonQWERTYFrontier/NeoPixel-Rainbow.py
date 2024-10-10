import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness = 0.3)
i = 0

for i in range(1,51)
purple = (255, 111, 255)
green = (144, 255, 144)


color_list = [purple, green]
def fade_in(color):
    fade_ratio = color
    
def fade_out():
    while True:
        for i in range(np.n):
            time.sleep(0.2)
            np[i] = random.choice(color_list)
            np.show()


fade_out()
fade_in()
