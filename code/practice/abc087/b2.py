#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
for i in range(a+1):
    for j in range(b+1):
        tmp = (x-((500*i)+(100*j)))
#        print (i,j,tmp)
        if tmp == 0:
            ans += 1
        elif tmp > 0:
            if tmp%50 == 0 and tmp//50 <= c:
                ans += 1
        else:
            # tmp < 0
            pass            
print (ans)
