from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists = True)
p1 = APoint(5000, 0)
p2 = APoint(0,5000)
acad.model.Addline(p1,p2)
