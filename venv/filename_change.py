import pyautogui as pg
import time
time.sleep(2)
x, y = pg.position()
pg.click(x, y, button='left')
for i in range(1, 12):
    pg.press('f2')
    pg.typewrite('0'+str(i))
    pg.press('enter')
    pg.press('right')

