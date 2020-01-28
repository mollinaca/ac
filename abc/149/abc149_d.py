#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n, k = (int(i) for i in input().split())
r, s, p = (int(i) for i in input().split())
t=str(input())
hands=[]
results=[]

for i in range(0,n):
    if t[i] == "r":
        hand = "p"
    elif t[i] == "s":
        hand = "r"
    else :
        hand = "s"
    result=True

    if i - k >= 0:
        if hand == hands[i-k]:
            if i+k < n:
                if t[i] == t[i+k]:
                    # あいこ
                    if t[i+k] == "r":
                        hand = "r"
                    if t[i+k] == "s":
                        hand = "s"
                    if t[i+k] == "p":
                        hand = "p"
                    result=False
                else:
                    # 負け
                    if t[i+k] == "r":
                        hand = "s"
                    if t[i+k] == "s":
                        hand = "p"
                    if t[i+k] == "p":
                        hand = "r"
                    result=False

    results.append(result)
    hands.append(hand)

score=0
i=0
for hand in hands:
    if results[i]:
        if hand == "r":
            score+=r
        elif hand == "s":
            score+=s
        else:
            score+=p
    i+=1
print (score)