#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h,w = map(int,input().split())
grid = [list(input()) for i in range(h)]

print ("#"*(w+2))
for line in grid:
    print ("#",end="")
    print(''.join(map(str, line)),end="")
    print ("#")
print ("#"*(w+2))
