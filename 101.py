def foo(n, k = None):
    if k is None:
        k = n

    if n == 0:
        return []

    result = []
    if n <= k:
        result.append([n])
    for i in range(1, 1+min(n, k)):
        for l in foo(n-i, i):
            result.append(l + [i])

    return result

print(*foo(12), sep='\n')