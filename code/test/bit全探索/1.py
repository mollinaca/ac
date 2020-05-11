#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://qiita.com/gogotealove/items/11f9e83218926211083a
# みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。
# 財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。 

money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)

#print (item)
for i in range(2 ** n):
#    print (i)
#    print("pattern {}: ".format(i), end="")
    bag = []
    total = 0

    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            #print (j)
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
            total += item[j][1]
#    print(bag)
    if (total <= money):
        print (total, bag)