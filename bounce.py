import board
import time
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write=False, brightness=1)

red = (255,00,0)
green = (0,255,0)
blue = (0,0,255)
magenta = (106, 49, 81)
orange = (255, 60, 0)
purple = (128, 0, 128)
white = (255,255,255)

palete_list = [red, yellow, green, cyan, blue, purple]

def bouncey(fg, bg, bounces = 10):
    g = 0
    b = 1
    bc = 0
    while bc < bounces:
        np.fill(fg)
        np[g+0] = bg
        np[g-1] = bg
        np[g-2] = bg
        np.show()
        g += b
        if g >= (np.n-1) or g <=0:
            b *= -1
            bc += 1
        time.sleep(0.03)
        if g >= (np.n+1) or g == 0:
            b *= 1
            bc += 1
        time.sleep(0.03)

           
while True:
    bouncey(magenta, orange)
