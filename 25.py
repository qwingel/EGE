def deliteli(x):
    a = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            a.add(i)
            a.add(x // i)

    return sorted(list(a))

count = 0
for i in range(460 * 10 ** 6 + 1, 10 ** 20):
    if count >= 5:
        break

    deli = deliteli(i)
    if len(deli) < 5:
        continue

    
    print(i // deli[4])
    count += 1