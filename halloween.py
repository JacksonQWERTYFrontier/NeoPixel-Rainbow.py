import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write= False, brightness=.2)
i = 0


magenta = (255,0,255)
white = (255,255,255)
orange = (255, 135, 0)


palet_list = [orange, magenta, white]

def flames(pone, ptwo, pthree, pfour):
    np.fill(pone)
    np.show()
    for i in range(ptwo):
        np[random.randint(0, np.n - 2)]= pthree
        np.show()
        time.sleep(pfour)

def fade_out(color,speed):
    ratio_orange = color[2]/50
    orig_orange = color[2]
    ratio_magenta = color[0]/50
    orig_magenta = color[0]
    ratio_white = color[1]/50
    orig_white = color[1]
    for i in range(1,51):
        r = int(orig_orange - i * ratio_orange)
        g = int(orig_magenta - i * ratio_magenta)
        b = int(orig_white - i * ratio_white)
        np.fill((r,g,b))
        np[0]
        np.show()
        time.sleep(speed)

def fade_in(color,speed):
    ratio_orange = color[0]/50
    orig_orange = color[0]
    ratio_magenta = color[1]/50
    orig_magenta = color[1]
    ratio_white = color[2]/50
    orig_white = color[2]
    for i in range(1,51):
        r = int(orig_orange + i * ratio_orange)
        g = int(orig_magenta +i * ratio_magenta)
        b = int(orig_white + i * ratio_white)
        np.fill((r,g,b))
        np.show()
        time.sleep(speed)

while True:
    flames(orange, 50, (200, 34, 0), .0000001)
    rainbow_led = random.choice(palet_list)
    fade_in(orange, 0.01)
    flames(orange, 50, (200, 34, 0), .0000001)
    fade_out(magenta,.01)
    flames(orange, 50, (200, 34, 0), .0000001)

