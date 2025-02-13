f = open('27-A_12934.txt')

K = int(f.readline())
N = int(f.readline())

a = [int(i) for i in f]

max_len = 0

for i in range(N):
    sum = 0
    count = 0
    for j in range(i, N):
        if sum + a[j] <= K:
            count += 1
            sum += a[j]

        else:
            break
    
    if count > max_len:
        max_len = count


print(max_len)