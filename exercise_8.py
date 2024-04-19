n = int(input('введите натуральное число: '))
a = []
for i in range(1, n):

    if i ** 2 < n:

            p = (n - (i ** 2)) ** 0.5
            s = int(p)
            if s == p  and p not in a:
               a.append(i)
               a.append(p)
print(a)
print(int(len(a)/2))
