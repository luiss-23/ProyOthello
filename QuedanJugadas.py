def QuedanJugadas(A:[int],B:[int],turno:int)->bool:
    Quedan = False
    for i in range(0,8):
        for j in range (0,8):
            if A[i][j] == 0:
                if esValida(A, B, i, j, turno):
                    Quedan = True
                else:
                    pass
            elif A[i][j] == 1 or A[i][j] == 2:
                pass
    return Quedan