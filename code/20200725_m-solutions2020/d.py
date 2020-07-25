#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
l = []

for i in range(n):
    if i == 0:
        l.append(0)
    elif i == n-1:
        l.append(0)
    elif A[i-1] < A[i]:
        l.append(1)
    elif A[i-1] > A[i]:
        l.append(-1)
    else:
        l.append(0)

print (l)
exit ()

m = 1000
k = 0



for i in range(n):
    print ("a",i,m,k,A[i],A[i::],min(A),max(A))
    if 0 < k and i == n-1: # 最後で持ってるなら売る
        m = m + A[i]*k
    elif A[i] <= m and A[i] < A[i+1]: # 次と比較して上がるなら買う
        k = m//A[i]
        m = m - A[i]*k
    elif # 次と比較して下がるなら売る

    if A[i] <= m and A[i] == min(A) and i != n-1:
        # 最後でなくて、全体で最安なら買い
        k = m//A[i]
        m = m- A[i]*k
    elif A[i] < m and A[i] < max(A[i::]) and i != n-1:
        # 最後でなくて、今後、現在の株価より高い株価があれば買い
        k = m//A[i]
        m = m - A[i]*k
    elif 0 < k and A[i] == max(A):
        # 全体で最高なら売り
        m = m + A[i]*k
        k = 0
    elif 0 < k and A[i] != min(A[i::]):
        # 今後、現在の株価より安い株価があれば売り
        m = m + A[i]*k
        k = 0
    elif 0 < k and A[i] == max(A[i::]):
        # 今後、現在より高い株価がなければ売り
        m = m + A[i]*k
        k = 0
    else:
        pass

    print ("b",i,m,k)

print (m)
