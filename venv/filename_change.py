import pyautogui as pg
import time
import pyperclip as pl
time.sleep(2)
pg.click(276, 261, button='left')
time.sleep(0.5)
pl.copy('正')
pg.press('f2')
pg.hotkey('ctrl','v')
time.sleep(0.5)
pg.press('enter')
time.sleep(0.5)
pg.press('home')
pl.copy('侧')
pg.press('f2')
time.sleep(0.5)
pg.hotkey('ctrl','v')
pg.press('enter')
time.sleep(0.5)
pg.press('home')
for i in range(1, 75):
    pg.press('f2')
    pg.typewrite('0'+str(i))
    pg.press('enter')
    pg.press('right')
print('done')

