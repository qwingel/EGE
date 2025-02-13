f = open('27-A_12934 (2).txt')

K = int(f.readline())
N = int(f.readline())

a = [int(i) for i in f]

max_count = 0

for i in range(N):
    count = 0
    sum = 0
    for j in range(i, N):
        if sum + a[j] <= K:
            count += 1
            sum += a[j]

        else:
            break
        
    if count > max_count:
        max_count = count


print(max_count)
















# f = open('27A_13622.txt')

# K = int(f.readline())
# N = int(f.readline())

# a = [int(i) for i in f]

# count = 0

# for i in range(N):
#     if a[i] > (K / 2):
#         count += 1

# print(count)
            
