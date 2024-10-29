import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write= False, brightness=.2)
i = 0

# These are the main colors used in my code
magenta = (255,0,255)
white = (255,255,255)
orange = (255, 135, 30)
lightorange = (200, 34, 0)

#    flames(magenta, 50, (200, 34, 0), .0000001)
#    fade_in(orange, 0.01)
#    fade_out(magenta,.01)
#    rainbow_led = random.choice(palet_list)

#Sparkleween is the legnth of which something will repeat
sparkleween = 5

#Palet_list is a full list of my colors
palet_list = [orange, magenta, white, lightorange]

# This is my flame function which makes the set leds move like a flame
def flames(pone, ptwo, pthree, pfour):
    np.fill(pone)
    np.show()
    for i in range(ptwo):
        np[random.randint(0, np.n - 2)]= pthree
        np.show()
        time.sleep(pfour)

# THe two functions fade in and fade out can be used to mimic even lightning strikes
def fade_in(color,speed):
    np.show()
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
        
def fade_out(color,speed):
    np.show()
    ratio_orange = color[2]/50
    orig_orange = color[2]
    ratio_magenta = color[2]/50
    orig_magenta = color[0]
    ratio_white = color[2]/50
    orig_white = color[1]
    for i in range(1,51):
        r = int(orig_orange - i * ratio_orange)
        g = int(orig_magenta - i * ratio_magenta)
        b = int(orig_white - i * ratio_white)
        np.fill((r,g,b))
        np[0]
        np.show()
        time.sleep(speed)


# This set code is what makes our amazing lightshow
while True:
    anything = random.choice(palet_list)
    for i in range(sparkleween):
        flames(anything, 50, (lightorange), .0006)
    fade_in(anything, 0.006)
    fade_out(magenta,.006)
    for i in range(sparkleween):
        flames(anything, 50, lightorange, .0006)
