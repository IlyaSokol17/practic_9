n = int(input('введите максимальное значение на плитке: '))
a = []
d = []
for i in range(0, n + 1):
     for t in range(0, n + 1):
         plit = str(i) + str(t)
         if plit[::-1] not in a:
            a.append(plit)
            d.append(i)
            d.append(t)
print(a)
print(len(a))
print(d)
print(sum(d))


