import os
import shutil
allList = os.listdir(u"D:\\notes\\python\\资料\\")
for i in allList:
    aa, bb = i.split(".")
    if 'python' in aa.lower():
        oldName = u"D:\\notes\\python\\资料\\"+aa+"."+bb
        newName = u"d:\\copy\\newname"+aa+"."+bb
        shutil.copyfile(oldname,newname)