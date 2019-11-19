def consumoDiagonal(A:[int], i:int, j:int, turno:int) -> 'void':
    k = i
    l = j
    if i != 0 and j != 7:
        while i > 0 or j < 7:
            if A[i-1][j+1] != turno and A[i-1][j+1] != 0:
                i = i - 1
                j = j + 1
            elif A[i-1][j+1] == 0:
                i = 0
                j = 7
            elif A[i-1][j+1] == turno:
                i = k
                for r in range(l,j+1):
                    A[i][r] = turno
                    i = i - 1
                i = 0
                j = 7
    elif i == 0 and j == 7:
        pass
    
    i = k
    j = l

    if i != 7 and j != 7:
        while i < 7 or j < 7:
            if A[i+1][j+1] != turno and A[i+1][j+1] != 0:
                i = i + 1
                j = j + 1
            elif A[i+1][j+1] == 0:
                i = 7
                j = 7
            elif A[i+1][j+1] == turno:
                i = k
                for r in range(l,j+1):
                    A[i][r] = turno
                    i = i + 1
                i = 7
                j = 7
    elif i == 7 and j == 7:
        pass
    
    
    i=k
    j=l

    if i != 7 and j != 0:
        while i < 7 or j > 0:
            if A[i+1][j-1] != turno and A[i+1][j-1] != 0:
                i = i + 1
                j = j - 1
            elif A[i+1][j-1] == 0:
                i = 7
                j = 0
            elif A[i+1][j-1] == turno:
                j = l
                for r in range(k,i+1):
                    A[r][j] = turno
                    j = j - 1
                i = 7
                j = 0
    elif i == 7 and j == 0:
        pass
    
    i=k
    j=l

    if i != 0 and j != 0:
        while i > 0 or j > 0:
            if A[i-1][j-1] != turno and A[i-1][j-1] != 0:
                i = i - 1
                j = j - 1
            elif A[i-1][j-1] == 0:
                i = 0
                j = 0
            elif A[i-1][j-1] == turno:
                for r in range(i-1,k):
                    A[r][j-1] = turno
                    j = j + 1
                i = 0
                j = 0
    elif i == 0 and j == 0:
        pass

