# s = sum(map(int, stroka)) <-- сумма цифр в любой системе счисления


from itertools import product
print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f1 = (not (y <= x)) or (z <= w) or (not z)
    if f1 == 0:
        print(x, y, z ,w)