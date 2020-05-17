#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""
余弦定理
a**2=b**2+c**2−2*b*c*cosA

角度をx、2辺をa,b,とすると解は
math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(math.radians(x))))
"""
a,b,h,m = map(int,input().split())

# 2辺の角度
## 長針は60分かけて360度を回る
l_rad = 360*(m/60)
## 短針は12時間かけて360度を回る+60分かけて360*(1/12)進む
s_rad = 360*(h/12) + 30*(m/60)

## 角度は
x = abs(s_rad-l_rad)
if x > 180:
    x = 360 - x

import math
print (math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(math.radians(x)))))
