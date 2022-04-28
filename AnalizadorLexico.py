from prettytable import PrettyTable
from os import system, startfile
from Token import Token
from Error import Error

class AnalizadorLexico:
    
    def __init__(self) -> None:
        self.listaTokens  = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.i = 0

    def LimpiarTokens (self):
        self.listaTokens.clear()
    
    def LimpiarErrores (self):
        self.listaErrores.clear()
    
    def AnalizadorLexico(self, Entrada):
        '''Analiza el archivo de entrada'''
        
        
        linea = 1
        columna = 1
        buffer = ''
        centinela = '¬'
        estado = 0
        Entrada += centinela

        i = 0
        while i< len(Entrada):
            c = Entrada[i]

            if estado == 0:
                if c == '<':
                    buffer += c
                    columna += 1
                    estado = 3
                elif  c == '"':
                    buffer += c
                    columna += 1
                    estado = 1
                elif  c == '-':
                    buffer += c
                    columna += 1
                    estado = 4
                elif c.isalpha():
                    buffer += c
                    columna += 1
                    estado = 2
                elif c.isdigit():
                    buffer += c
                    columna += 1
                    estado = 6
                elif c == '\n':
                    linea += 1
                    columna = 1
                elif c in ['\t',' ']:
                    columna += 1
                elif c == '\r':
                    pass
                elif c == centinela:
                    print('Se aceptó la cadena!')
                    break
                else:
                    buffer += c
                    self.listaErrores.append(Error('Caracter ' + buffer + ' no reconocido en el lenguaje.', linea, columna))
                    buffer = ''
                    columna += 1
            
            
            elif estado == 1:
                if  c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer, "cadenaComillas", linea, columna))
                    buffer = ""
                    columna += 1
                    estado = 0
                elif c == ' ':
                    buffer += c
                    columna += 1
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1
                pass
                    
            elif estado ==4:
                if c.isalpha():
                    buffer += c
                    columna += 1
                else: 
                    if buffer == '-f':
                        self.listaTokens.append(Token(buffer, "banderaF", linea, columna))
                        estado = 5
                        i += 1
                    elif buffer == '-ji':
                        self.listaTokens.append(Token(buffer, 'banderaJi', linea, columna))
                        estado = 0
                        i += 1
                    elif buffer == '-jf':
                        self.listaTokens.append(Token(buffer, 'banderaJf', linea, columna))
                        estado = 0
                        i += 1
                    elif buffer == '-n':
                        self.listaTokens.append(Token(buffer, 'banderaN', linea, columna))
                        estado = 0
                        i += 1
                    i -= 1
                    buffer = ''
                #i += 1
                    
            elif estado == 5:
                if c.isdigit() or c.isalpha():
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, "NombreArchivo", linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0

            elif estado == 6:
                if c.isdigit():
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, "Numero", linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0

            elif estado ==3:
                if c =='>': 
                    buffer += c
                    self.listaTokens.append(Token(buffer, "cadenaMayorYMenorQue", linea, columna))
                    buffer = ""
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1
                pass

            elif estado == 2:
                if c.isalpha() or c.isdigit():
                    buffer += c
                    columna += 1
                else:
                    if buffer == 'RESULTADO':
                        self.listaTokens.append(Token(buffer, 'RESULTADO', linea, columna))
                    elif buffer == 'VS':
                        self.listaTokens.append(Token(buffer, 'VS', linea, columna))
                    elif buffer == 'TEMPORADA':
                        self.listaTokens.append(Token(buffer, 'TEMPORADA', linea, columna))
                    elif buffer == 'JORNADA':
                        self.listaTokens.append(Token(buffer, 'JORNADA', linea, columna))
                    elif buffer == 'GOLES':
                        self.listaTokens.append(Token(buffer, 'GOLES', linea, columna))
                    elif buffer == 'TEMPORADA':
                        self.listaTokens.append(Token(buffer, 'TEMPORADA', linea, columna))
                    elif buffer == 'LOCAL':
                        self.listaTokens.append(Token(buffer, 'CONDICION_GOLES', linea, columna))
                    elif buffer == 'VISITANTE':
                        self.listaTokens.append(Token(buffer, 'CONDICION_GOLES', linea, columna))
                    elif buffer == 'TOTAL':
                        self.listaTokens.append(Token(buffer, 'CONDICION_GOLES', linea, columna))
                    elif buffer == 'TABLA':
                        self.listaTokens.append(Token(buffer, 'TABLA', linea, columna))
                    elif buffer == 'PARTIDOS':
                        self.listaTokens.append(Token(buffer, 'PARTIDOS', linea, columna))
                    elif buffer == 'TOP':
                        self.listaTokens.append(Token(buffer, 'TOP', linea, columna))
                    elif buffer == 'SUPERIOR':
                        self.listaTokens.append(Token(buffer, 'CONDICION_TOP', linea, columna))
                    elif buffer == 'INFERIOR':
                        self.listaTokens.append(Token(buffer, 'CONDICION_TOP', linea, columna))
                    elif buffer == 'ADIOS':
                        self.listaTokens.append(Token(buffer, 'ADIOS', linea, columna))
                    
                    i -= 1
                    estado = 0
                    buffer = ''
            i += 1
        
    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna","tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna,token.tipo])
        print(x)

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion","linea","columna"]
        for error_ in self.listaErrores:
            x.add_row([error_.descripcion, error_.linea, error_.columna])
        print(x)
            