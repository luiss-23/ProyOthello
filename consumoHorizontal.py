def consumoHorizontal(A:[int], i:int, j:int, turno:int) -> 'void':
    k=int
    k=j
    if j!=7:
        while j<7:
            if A[i][j+1]!=turno and A[i][j+1]!=0:
                j=j+1
            elif A[i][j+1]==0:
                j=7
            elif A[i][j+1]==turno:
                for t in range (k,j+1):
                    A[i][t]=turno  
                j=7         
    elif j==7:
        pass
    j=k
    if j!=0:
        while j>0:
            if A[i][j-1]!=turno and A[i][j-1]!=0:
                j=j-1
            elif A[i][j-1]==0:
                j=0
            elif A[i][j-1]==turno:
                for z in range (j-1,k):
                    A[i][z]=turno
                j=0
    elif j==0:
        pass 


