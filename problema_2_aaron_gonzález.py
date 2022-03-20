combinaciones_de_victoria = [
    0b000000111,
    0b000111000,
    0b111000000,
    0b100100100,
    0b010010010,
    0b001001001,
    0b100010001,
    0b001010100
]
def gana_tic_tac_toe(f1, f2, f3):
    """
    Revisa el ganador de un juego de tic tac toe

    Parametros
    ----------
        - f1: primera fila del tablero
        - f2: segunda fila del tablero
        - f3: tercera fila del tablero
    """
    full = (f1 << 3 | f2) <<3 | f3
    i = 0
    while i < 8:
        if (full & combinaciones_de_victoria[i]) == combinaciones_de_victoria[i]:
            return 1
        i += 1
    return 0



# el número debería ser convertido a binario aquí, en lugar de 1 0b001 y así
# para que el código funcione, sino será código no funcional
print(gana_tic_tac_toe(1,11,110))
