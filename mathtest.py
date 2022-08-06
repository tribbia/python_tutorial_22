
import math as m
 
e=m.e
pi=m.pi

y_natural= m.log(e)
y_base10 =m.log(e,10)
y_log10=m.log10(e)

# print( e, y_natural, y_base10, y_log10)

deg=180
rads=deg*m.pi/180
rads_fromfunc =m.radians(deg)
cos_fromdeg=m.cos(deg)
cos_fromrads=m.cos(rads)
print(deg, rads,cos_fromdeg, cos_fromrads)
