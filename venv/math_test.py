# import math
# math.
import pyautogui as pg 
import time
time.sleep(5)
try:
    while True:
        pg.click(button='right')
except KeyboardInterrupt:
    print('done')