def quedanFichas(F:int,R:int)->bool:
    if F - R == 0:
        quedan = False
    elif F - R != 0:
        quedan = True
    return quedan