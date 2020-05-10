#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c,k = map(int,input().split())
ans = 0
if k <= a:
    ans = k
elif a < k and k <= a+b:
    ans = a
elif a+b < k and k <= a+b+c:
    ans = a-(k-(a+b))
else:
    pass

print (ans)
