f = open('9-210.csv')
k = 0
for i in f:
    a = list(map(int, i.split(';')))
    a.sort()
    
    d = dict()
    for x in a:
        if x not in d.keys():
            d[x] = 1
        else:
            d[x] += 1
            
    flag1 = False
    flag2 = False
    flag3 = False
    
    if d[a[0]] == 1:
        flag1 = True
    
    summ = 0
    for x in d.keys():
        if d[x] > 1:
            flag2 = True
            summ += x * d[x]
    
    if (a[0] + a[-1]) < summ:
        flag3 = True
        
    if flag1 and flag2 and flag3:
        k += 1

print(k)
        
        