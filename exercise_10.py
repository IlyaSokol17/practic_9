n = int(input())
c = 0
for q in range(n ):
    for w in range(n):
        for e in range(n):
            for r in range(n ):
                for t in range(n ):
                    for y in range(n ):
                        for u in range(n ):
                            for i in range(n ):
                                for o in range(n ):
                                    for p in range(n ):
                                        for z in range(n ):
                                            for x in range(n ):
                                                for c in range(n ):
                                                    for v in range(n ):
                                                        for b in range(n ):
                                                            if q+w+e+r+t+y+u+i+o+p+z+x+c+v+b == n :
                                                                m = str(q)+str(w)+str(e)+str(r)+str(t)+str(y)+ \
                                                                    str(u) +str(i)+str(o)+str(p)+str(z)+ \
                                                                    str(x) +str(c)+str(v)+str(b)
                                                                n =m.count('0')
                                                                print(n)
                                                                while n != 0:
                                                                     m.replace('0', '1 ')
                                                                     n -=1
                                                                print(m)




