
def f(n):
    n = int(input())
    c = 0
    for i in range(0, n + 1):
        while n > 0:
            n -= i
            c += 1
        if c * i == n:
            s = str(i)*c
        else:
            s = str(i)*c + str(n - i * c)
        print(s)




  
