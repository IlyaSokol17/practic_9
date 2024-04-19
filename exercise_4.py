N = int(input('Введите количество веревок: '))
c = 0
while N != 0:
    if N >=4 and N % 2 == 0:
        c += 1
    N = int(input('Введите количество веревок: '))
print(c)
