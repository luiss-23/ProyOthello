def cambiarJugador(turn:int) -> 'void':
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    return turn
    
