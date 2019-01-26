import os
import time
import pyautogui as pg
try:
    while True:
        #screenWidth, screenHeight = pag.size()  #获取屏幕的尺寸
        #print(screenWidth, screenHeight)
        mouse_x, mouse_y = pg.position()   #获取当前鼠标的位置
        showStr = "Position:" + str(mouse_x).rjust(4) + ',' + str(mouse_y).rjust(4)
        os.system('cls')  # 清除屏幕
        print(showStr)
        time.sleep(1)
except KeyboardInterrupt:
    print('end....')

