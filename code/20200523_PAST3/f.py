#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
n = int(input())
s = ""

for _ in range(n):
    s += input()

if n%2 == 1:
    x = n-1
else:
    x = n

c = (collections.Counter(s))

total = 0
for k,v in c.items():
    total += v//2

if x//2 <= total:
    """
    # 長さ n の回文を作成
    # nが偶数なら、2個以上ある要素を n/2 個詰めた文字列を作って、前から+後ろから出力
    # nが基数なら、2個以上ある要素を n/2 個詰めた文字列を作って、前から+1個だけの要素を一つ+後ろから出力
    # 1個だけの要素が、2個以上ある要素の最後の1個の可能性があるので、どの文字を使って、どの文字が残ってるか？を管理しておく必要がある
    # -> c でそのまま管理する
    """
    a = ""
    left = n//2
    for k,v in c.items():
#        print (k,v)
        if 2 <= v:
            if v//2 <= left:
                # v文字では全部埋まらないので、v文字だけ全部つめる
                a += k*(v//2)
                c[k] = 0 #全部使った
                left = left - v//2
            else:
                # 残り必要文字数が v より小さい
                a += k*left
                c[k] = c[k] - v//2
                left = 0

        if left == 0: #全部埋まった
            if n%2 == 0: #偶数文字
                print (a+a[::-1])
                exit ()
            else: #奇数文字
                # 真ん中にいれる適当な一文字を選択
                for k,v in c.items():
                    if v>=1:
                        x = k
                print (a+x+a[::-1])
                exit ()
else:
    print (-1)
