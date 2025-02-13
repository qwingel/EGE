from functools import lru_cache

@lru_cache
def f(n):
    if n < 3:
        return 1

    elif n > 2 and n % 2 == 0:
        return g(n) + f(n - 1)
    
    elif n > 2 and n % 2 != 0:
        return f(n - 2) - 2 * g(n + 1)

@lru_cache
def g(n):
    if n < 3:
        return 1
    
    elif n > 2 and n % 2 == 0:
        return f(n - 3) + f(n - 2)
    
    elif n > 2 and n % 2 != 0:
        return f(n = 1) - g(n - 1)

for i in range(130, 0, -1):
    f(i)
    g(i)

print(g(120))