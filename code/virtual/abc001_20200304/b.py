#!/usr/bin/env python3
# -*- coding: utf-8 -*-
m=int(input())
if m < 100:
    ans = "00"
elif 100 <= m and m <= 5000:
    ans = m//100
    if ans < 10:
        ans = "0"+str(ans)
elif 6000 <= m and m <= 30000:
    ans = m//1000 + 50
elif 35000 <= m and m <= 70000:
    ans = (m//1000 - 30)//5 + 80
else:
    ans = 89
print (ans)