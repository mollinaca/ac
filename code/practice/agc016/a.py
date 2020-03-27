#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s=input()
ans=float('inf')
for c in set(s):
#    print (c)
    ans=min(ans,max(map(len,s.split(c))))
#    print (ans)
print(ans)