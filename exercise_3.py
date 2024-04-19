N = int(input('Введите количество мороженного: '))
for i in range(2, N + 1):
    if N % i == 0:
        print(i)
        break