#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int, input().split())
l = list(map(int, input().split()))

l_minus = [i for i in l if i < 0]
l_plus = [i for i in l if i > 0]
l_zero = [i for i in l if i == 0]
m_num = len(l_minus)
p_num = len(l_plus) 
z_num = len(l_zero) 

# 全部のペアの数
pairs_num = (n*(n-1))//2
# マイナスのペアの数はマイナスの数×プラスの数
m_pairs_num = m_num*p_num
# プラスのペアの数
p_pairs_num = ((m_num*(m_num-1))//2) + ((p_num*(p_num-1))//2)
# 0のペアの数
z_pairs_num = z_num*p_num + z_num*m_num + ((z_num*(z_num-1))//2)

# 0なら、0を出力して終了
if m_pairs_num < k and k < p_pairs_num:
    print (0)
    exit (0)

seki_list = []
# マイナスなら、マイナスのリストを作成して出力して終了
if k <= m_pairs_num:
    for i in l_minus:
        for j in l_plus:
            seki_list.append(i*j)
    print (sorted(seki_list)[k-1])
    exit (0)

# プラスなら、プラスのリストを作成して出力して終了
else:
    for i in range(m_num):
        for j in range(m_num):
                if i == j:
                    pass
                elif j < i:
                    pass
                else:
                    seki_list.append(l_minus[i]*l_minus[j])

    for i in range(p_num):
        for j in range(p_num):
                if i == j:
                    pass
                elif j < i:
                    pass
                else:
                    seki_list.append(l_plus[i]*l_plus[j])

    print (sorted(seki_list)[(k-1)-(m_pairs_num+z_pairs_num)])
    exit (0)
