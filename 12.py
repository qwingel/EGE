res = 0

def deliteli(x):
    mn = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            mn.add(i)
            mn.add(x // i)
                
    return mn
            
def is_prostoe(x):
    if x == 1:
        return False
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
        
    return True

count = 0
for n in range(3, 1000):
    s = '3' + '5' * n
    while ('25' in s) or ('355' in s) or ('555' in s):
        if '25' in s:
            s = s.replace('25', '32', 1)
        
        if '355' in s:
            s = s.replace('355', '25', 1)
            
        if '555' in s:
            s = s.replace('555', '3', 1)
        
    if s.count('2') == 5:
        count = n


print(count)