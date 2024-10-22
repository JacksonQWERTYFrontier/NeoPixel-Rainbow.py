import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 31, auto_write=False, brightness = 0.8)

def blue_flames(pone, ptwo, pthree, pfour):
        np.fill(pone)
        np.show()
        for i in range(ptwo):
            np[random.randint(0, np.n - 2)]= pthree
            np.show()
            time.sleep(pfour)
while True:
    blue_flames(250, 50, 34, .0000001)
