for A in range(1, 10):
    for B in range(0, 10):
        AB = int(str(A) + str(B))
        sum = AB ** 2
        sum = str(sum)
        if sum[1::] == str(AB) and len(sum) == 3:
            print(sum)
