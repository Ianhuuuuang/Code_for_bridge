# -*- coding: UTF-8 -*-  
import math 
import clr
# 导入 RevitAPI 和 RevitAPIUI
clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
#导入dyamo中的几何图元,这里就将上个内容中提到的Geometry节点引入了进来
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *
#导入revit节点，如果要使用revit节点中的方法
clr.AddReference("RevitNodes")
from Revit.Elements import *
#涉及到revit和dynamo几何元素装换，采用下列代码
import Revit
# 导入几何体转换方法(将dynamo中输出的几何体转为revit中的几何体）
clr.ImportExtensions(Revit.GeometryConversion)
# 导入元素转换(revit转dynamo)
clr.ImportExtensions(Revit.Elements) 
#导入系统文件操作，这样才能顺利将EXCEL读取节点进行装换
import System
from System.IO import FileInfo
#导入dynamoEXCEL读取功能
clr.AddReference("DSOffice")
from DSOffice import Data
#导入列表功能节点
clr.AddReference("DSCoreNodes")
import DSCore
from DSCore import *

#这里采用圆心与半径的方法创建圆
#将EXCEL读取节点进行转换
circleExcel=FileInfo(IN[0])
circleInformation=Data.ImportExcel(circleExcel,"Sheet1",False,True)
circleList=[]
for i in range(1,10):
	x=circleInformation[i][1]
	y=circleInformation[i][2]
	z=circleInformation[i][3]
	r=circleInformation[i][4]
	center =Point.ByCoordinates(x,y,z)
	circle =Circle.ByCenterPointRadius(center,r)
	circleList.Add(circle)
OUT=circleList
