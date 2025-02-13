f = open('26_11681.txt')
N, K = map(int, f.readline().split())
a = [[int(i.split()[0]), int(i.split()[1])] for i in f]
# a = []
# b = []
#
# for i in f:
#     x, y = map(int, i.split())
#     b.append(x * (1 - (y / 100)))
f.close()

a.sort(key=lambda x: (-x[0] * (x[1] / 100)))

summ = 0

for i in range(K):
    summ += a[i][0] * (1 - (a[i][1] / 100))

for i in range(K, len(a)):
    summ += a[i][0]

print(summ, 0)