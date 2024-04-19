N, d, R = map(int, input('введите данные(N колец, d толщина, R внутренний радиус):').split())
if N % 2 == 0:
    sum_length = ((d + R) * 2) * (N / 2) + ((R - d) * 2) * (N / 2)
else:
    sum_length = ((d + R) * 2) * ((N // 2) + 1) + ((R - d) * 2) * (N // 2)
print(sum_length)
