for i in range(100000, 1000000):
    n = str(i)
    p = n[1::]

    c = str(i + 1)
    t = c[1::]

    z = str(i + 2)
    b = z[1:5]

    r = str(i + 3)

    if p == p[::-1] and t == t[::-1] and b == b[::-1] and r == r[::-1]:
        print(i)


