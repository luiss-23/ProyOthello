def consumoVertical(A:[int], i:int, j:int, turno:int) -> 'void':
    for i in range(0,8):
        if ( A[i][j] == turno ):
            if ( A[i+1][j] != 0 and A[i+1][j] != turno ):
                A[i+1][j] = turno
                consumoVertical(A, i + 1, j, turno)
            elif ( A[i-1][j] != 0 and A[i-1][j] != turno):
                A[i-1][j] == turno
                consumoVertical(A, i - 1, j, turno)
            elif ( A[i+1][j] == 0 or A[i+1][j] == turno ):
                pass
            elif ( A[i-1][j] == 0 or A[i-1][j] == turno):
                pass


        

        
    
