import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness = 0.3)
i = 0

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

color_list = [magenta]
flash = 3
def flash():
    np[i] = random.choice(color_list)
    np.show()
    time.sleep(0.0)

def lightning():
    for i in range(flash):
        time.sleep(0.2)
        flash()
        time.sleep(0.1)
    
while True:
    for i in range(np.n):
        np[i] = random.choice(color_list)
        np.show()
        time.sleep(0.0)
        lightning(9)
