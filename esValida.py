def esValida(A:[int],B:[int],i:int,j:int,turneto:int)->bool:
    Valida=False
    if A[i][j]!=0:
        pass
    elif A[i][j] == 0:
        for a in range (0,8):
            for b in range (0,8):
                B[a][b]=A[a][b]
        consumo(B, i, j,turneto)
        reflejarJugada(B,i,j,turneto)
        for a in range (0,8):
            for b in range (0,8):
                if a==i and b==j:
                    pass
                elif a!=i or b!=j:
                    if A[a][b]==B[a][b]:
                        pass
                    elif A[a][b]!=B[a][b]:
                        Valida=True 
    return Valida