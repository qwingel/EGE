a = 3 * (16 ** 2018) - 2 *(8 ** 1028) - 3 * (4 ** 1100) - 2022

mn = set()
 
for i in range(0, 4037):
    mn.add(sum(map(int, str(i))))

print(len(mn), mn)

