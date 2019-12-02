def consumoVertical(A:[int], i:int, j:int, turno:int) -> 'void':
    k = int
    k = i
    if i != 7:
        while i < 7:
            if A[i+1][j] != turno and A[i+1][j] != 0:
                i = i + 1
            elif A[i+1][j] == 0:
                i = 7
            elif A[i+1][j] == turno:
                for t in range(k,i+1):
                    A[t][j] = turno  
                i=7        
    elif i == 7:
        pass
    i = k
    if i != 0:
        while i > 0:
            if A[i-1][j] != turno and A[i-1][j] != 0:
                i = i - 1
            elif A[i-1][j] == 0:
                i = 0
            elif A[i-1][j] == turno:
                for z in range(i-1,k):
                    A[z][j] = turno
                i=0
    elif i == 0:
        pass 
        