for S in range (1, 10):
    for E in range(0, 10):
        for N in range(0, 10):
            for D in range(0, 10):
                for M in range(1, 10):
                    for O in range(0, 10):
                        for R in range(0, 10):
                            if S != E and S != N and S != D and S != M and S != O and S != R and \
                                E != N and E != D and E != M and E != O and E != R and \
                                 N != D and N != M and N != O and N != R and \
                                     D != M and D != O and D != R and \
                                          M != O and M != R and \
                                               O != R  :
                                                    SEND = str(S) + str(E) + str(N) + str(D)
                                                    MORE = str(M) + str(O) + str(R) + str(E)
                                                    sum = int(SEND) + int(MORE)
                                                    sum = str(sum)
                                                    Y = sum[-1]
                                                    if (len(sum) == 5 and sum[0] == str(M) and sum[1] == str(O) and
                                                            sum[2] == str(N) and sum[3] == str(E) \
                                                            and Y != str(S) and Y != str(E) and Y != str(N) and\
                                                                 Y != str(D) and Y != str(M)  and Y != str(O) and \
                                                                   Y != str(R)):
                                                                            print(SEND)
                                                                            print(MORE)
                                                                            print(sum)


