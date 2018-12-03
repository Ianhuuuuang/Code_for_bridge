import pyautogui, time
# cooEdit = pyautogui.locateCenterOnScreen('edit.png')
# pyautogui.click(cooEdit[0], cooEdit[1])
time.sleep(1)
coos = pyautogui.locateAllOnScreen('match.png')
for coo in coos:
    x = coo[0]+coo[2]/2
    y = coo[1]+coo[3]/2
    pyautogui.click(x, y)
cooSave = pyautogui.locateCenterOnScreen('save.png')
print(cooSave)
pyautogui.click(cooSave[0], cooSave[1])
time.sleep(1)
cooConfirm = pyautogui.locateCenterOnScreen('confirm.png')
pyautogui.click(cooConfirm[0], cooConfirm[1])