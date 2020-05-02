#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import floor
a,b,n = map(int,input().split())
x = ((b//n)*n)-1
print ( max((floor((a*x/b) - a*(floor(x/b)))),(floor((a*n/b) - a*(floor(n/b))))) )
