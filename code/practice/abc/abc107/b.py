#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h,w = map(int,input().split())
grid = [list(input()) for i in range(h)]
if h == 1:
    print ("#"*(grid.count("#")))
    exit ()
exit ()
print (grid)
print (list(map(list, zip(*grid))))
exit ()

#ans = []
#
#for i in range(h):
#    if not grid[i] == ['.' for i in range(w)]:
#        ans.append(grid[i])
#
#print (ans)
#tate = []
#for i in range(w):
#    for j in range(h):
#        if not grid[j][i] == '.':
#            break
#        else:
#            tate.append(i):
#
