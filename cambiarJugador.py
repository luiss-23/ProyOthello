def cambiarJugador(turn:int) -> "void":
    if turn==1:
        turn=2
    elif turn==2:
        turn=1
    
turno=2
cambiarJugador(turno)
print(turno)