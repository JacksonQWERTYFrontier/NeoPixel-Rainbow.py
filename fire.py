import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 31, auto_write=False, brightness = 0.8)

def flames(pone, ptwo, pthree, pfour):
        np.fill(pone)
        np.show()
        for i in range(ptwo):
            np[random.randint(0, np.n - 2)]= pthree
            np.show()
            time.sleep(pfour)
while True:
    flames((250, 80, 0), 50, (200, 34, 0), .0000001)
