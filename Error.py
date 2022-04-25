class Error:
    def __init__(self, descripcion: str, linea: int, columna: int) -> None:
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        pass