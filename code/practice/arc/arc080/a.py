#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))
count1 = len([x for x in l if x%2 != 0])
count2 = len([x for x in l if (x%4 != 0) and (x%2 == 0)])
count4 = len([x for x in l if x%4 == 0])
print ("Yes") if (n - (count4*2) <= count2) or count4 >= n//2 else print ("No")
