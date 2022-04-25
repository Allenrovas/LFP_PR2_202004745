class Token:
    def __init__(self, lexema: str, tipo :str, linea: int, columna: int) -> None:
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        pass