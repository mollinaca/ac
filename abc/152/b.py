#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b=map(str, input().split())
aa=""
bb=""
for _ in range(int(a)):
    bb+=b
for _ in range(int(b)):
    aa+=a

if int(aa) >= int(bb):
    print (aa)
else:
    print (bb)
