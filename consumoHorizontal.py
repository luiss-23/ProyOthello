def consumoHorizontal(A:[int], i:int, j:int, turno:int) -> 'void':
    for j in range(0,8):
        if ( A[i][j] == turno ):
            if ( A[i][j+1] != 0 and A[i][j+1] != turno ):
                A[i][j+1] = turno
                consumoHorizontal(A, i, j+1, turno)
            elif ( A[i][j-1] != 0 and A[i][j-1] != turno ):
                A[i][j-1] == turno
                consumoHorizontal(A, i, j-1, turno)
            elif ( A[i][j+1] == 0 or A[i][j+1] == turno ):
                break
            elif ( A[i][j-1] == 0 or A[i][j-1] == turno):
                break
        else:
            break