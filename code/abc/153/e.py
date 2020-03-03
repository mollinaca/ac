#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h,n = map(int, input().split())
magic = [input().rstrip().split() for _ in range(n)]
magic_list = []
## 受けとりながら作れるんだろうなぁこれ...
for data in magic:
    data = data + [str(int(data[0])/int(data[1]))]
    magic_list += [data]

# 一番効率のいい技で限界まで殴る（0になれたら終わり）
# 端数を、次に効率のよい技で殴る⇒効率が同等なら、小さい技
## ⇒ ここを事前にうまいことソートしておきたい！！
## ['攻撃力','魔法力','ダメージ効率'] の3次元配列を、効率の降順 ⇒ 効率が同じなら魔法力の昇順 ⇒ 効率、魔法力が同じなら攻撃力の昇順 でソートしたい

l1=sorted(magic_list, key=lambda x: (x[1]))
l2=sorted(l1, key=lambda x: (x[2]), reverse=True)

magic_power_total=0
for magic in l2:
    i=0
    print("-------")
    print ("h:",h)
    print ("magic:",magic)

    if int(magic[0]) < h:
        if h%int(magic[0]) == 0:
            i=h//int(magic[0])
            print (int(magic[1])*i)
            exit (0)
        else:
            i=h//int(magic[0])
            magic_power_total+=int(magic[1])*i
            h = h-int(magic[0])*i
    else:
        if h < int(magic[0]):
            print (magic_power_total+int(magic[1]))
            exit (0)
        else:
            i=h//int(magic[0])
            magic_power_total+=int(magic[1])*i
            h = h-int(magic[0])*i
