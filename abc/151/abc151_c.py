n,m=map(int, input().split())
l=[]
for _ in range (0,m):
    l.append(input())
wa_total=0
ac_total=0
ac_list=[]
 
for value in l:
    if str(value.split()[1]) == "AC":
        if not str(value.split()[0]) in ac_list:
            ac_list.append(str(value.split()[0]))
            for i in range(0,l.index(value)):
                if l[i].split()[0] == value.split()[0]:
                    if l[i].split()[1] == "WA":
                        wa_total+=1
            l.remove(value)
 
print (len(ac_list), wa_total)