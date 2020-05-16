#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
d = []
for i in range(1,n+1):
    city, score = input().split()
    d.append({'id':i, 'restaurant':{'city':city, 'score':int(score)}})

sorted_d = sorted(
    d,
    key = lambda x: (x['restaurant']['city'], -x['restaurant']['score'])
)

for l in sorted_d:
    print (l['id'])
