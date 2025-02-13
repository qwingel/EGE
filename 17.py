f = open('D:\\Downloads\\17-370.txt')
a = [int(i) for i in f]
f.close()

k = 0
minn = 10 ** 20
min_sum = 10 ** 20
for i in range(len(a)):
    if abs(a[i]) % 10 == 3 and a[i] < minn and abs(a[i]) > 99 and abs(a[i]) < 1000:
        minn = a[i]

for i in range(len(a) - 1):
    if ((abs(a[i]) > 999 and abs(a[i]) < 10000) +\
        (abs(a[i + 1]) > 999 and abs(a[i + 1]) < 10000) == 1)\
        and \
        (a[i] ** 2 + a[i + 1] ** 2) % minn == 0:
        k += 1
        if a[i] ** 2 + a[i + 1] ** 2 < min_sum:
            min_sum = a[i] ** 2 + a[i + 1] ** 2

print(k, min_sum)
# sum(map(int, str(a[i]))) - сумма цифр
