def QuedanJugadas(A:[int],B:[int],turno:int)->bool:
    Quedan=False
    for x in range(0,8):
        for y in range (0,8):
            if A[x][y]==0:
                esValida(A,B,x,y,turno)
                if esValida(A,B,x,y,turno):
                    Quedan=True
                else:
                    pass
            elif A[x][y]==1 or A[x][y]==2:
                pass
    return Quedan