#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
ans = 0

if 1 <= n <= 6:
    print (n*15)
elif 6 < n <= 10:
    print (100)
else:
    ans += n//10 * 100
    n = n - (10*(n//10))
    if n == 0:
        pass
    elif 1 <= n <= 6:
        ans += n*15
    else:
        ans += 100

    print (ans)
