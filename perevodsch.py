def func(number:int, system:int):
    a = '0123456789ABCDEF'
    if number < system:
        return a[number]
    
    else:
        return func(number // system, system) + a[number % system]
    
print(func(1F, 2))


# s = sum(map(int, stroka)) <-- сумма цифр в любой системе счисления