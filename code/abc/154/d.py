#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n, k = map(int, input().split())
p = list(map(int,input().split()))

# １からNまでの値をもつサイコロを振ったときの期待値
def ex(x:int):
    return (x*(x+1)/2)/x

kitaichi = []
kitaichi_goukei = []
for i in range(len(p)):
    kitaichi.append(ex(p[i]))
    if i+1 >= k:
        kitaichi_goukei.append(sum(kitaichi[i+1-k:i+1]))
print (max(kitaichi_goukei))