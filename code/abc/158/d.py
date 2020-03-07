#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
未完成
・値を受け取るときに、以下の処理をして計算量を減らす、という作戦で実装してたけど普通に実装がだめでできなかった
 - リストの要素数が1以下なら、普通に append する
 - リストの要素数が2以上で
   - リストの末尾が "1" なら、
     - 入力も "1" なら、末尾の "1" を削り、入力も追加しない
     - 入力が "2" なら、入力2の指令を反転し、入力を追加、リスト末尾の"1"を削る  
"""
s = input()
q = int(input())
query_l = []
for i in range(q):
#    print ("i:",i)
    query = list(input().split())
#    print ("input query:",query)
    if len(query_l) <= 1:
        # リストが1要素以下なら、そのままappendする
        query_l.append(query)
        continue
    else:
        # リストが2要素以上あれば、末尾が1なら削っていく
        if query_l[-1] == list('1'):
            # 末尾が1で次の入力も1なら、末尾を削って入力も追加しない
            if query[0] == '1':
#                print ("deb1")
                del query_l[-1]
                continue
            # 末尾が1で次の入力は2なら、末尾を削って2の指令を反転する
            if query[0] == list('2'):
                if query[1] == '1':
                    query[1] = '2'
#                    print ("deb2")
                    del query_l[-1]
                    query_l.append(query)
                else:
                    query[1] = '1'
#                    print ("deb3")
                    del query_l[-1]
                    query_l.append(query)
        else:
            # 末尾が1でなければ、普通に追加
            query_l.append(query)
#    print ("query_l:",query_l)

#print ("----")
#print (query_l)

for query in query_l:
    if int(query[0]) == 1:
        s = s[::-1]
    else:
        if int(query[1]) == 1:
            s = query[2] + s
        else:
            s = s + query[2]
print (s)