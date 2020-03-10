#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,x = map(int,input().split())
print (abs((a//x)-(b//x))+1) if a%x == 0 else print (abs((a//x)-(b//x)))