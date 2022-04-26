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
    
    def AnalizadorLexico(self, Entrada):
        '''Analiza el archivo de entrada'''
        self.listaTokens = []
        self.listaErrores = []
        
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
                    elif buffer == 'VS ':
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
                        self.listaTokens.append(Token(buffer, 'LOCAL', linea, columna))
                    elif buffer == 'VISITANTE':
                        self.listaTokens.append(Token(buffer, 'VISITANTE', linea, columna))
                    elif buffer == 'TOTAL':
                        self.listaTokens.append(Token(buffer, 'TOTAL', linea, columna))
                    elif buffer == 'TABLA':
                        self.listaTokens.append(Token(buffer, 'TABLA', linea, columna))
                    elif buffer == 'PARTIDOS':
                        self.listaTokens.append(Token(buffer, 'PARTIDOS', linea, columna))
                    elif buffer == 'TOP':
                        self.listaTokens.append(Token(buffer, 'TOP', linea, columna))
                    elif buffer == 'SUPERIOR':
                        self.listaTokens.append(Token(buffer, 'SUPERIOR', linea, columna))
                    elif buffer == 'INFERIOR':
                        self.listaTokens.append(Token(buffer, 'INFERIOR', linea, columna))
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
    
    def reporteTokens(self):
        CuerpoHtml= """<!DOCTYPE html>
        <html lang=es>
        <head>
        <meta charset = "utf-8 ">
        <title>REPORTES</title>
        <style type = "text/css">
        body{
            margin: 0;
            font-family: Trebuchet MS, sans-serif;
            background-color: #fefbe9;
            background:linear-gradient(45deg,aqua,#02C7FF, #02A5FF , #0251FF , #022BFF, #6302FF,  #9402FF, #CA02FF ,#FF02F7);
        }
        .topnav {
            overflow: hidden;
            background-color: #DC143C;
            text-align: center;
        }
        table {
            border-collapse: collapse;
            width: 50%;
        }
        td, th {
            font-family: bahnschrift;
            border: 1px solid #000;
            text-align: center;
            padding: 8px;
        }
        h2{
            color: #000000;
        }</style>
        </head>
        <body>
        <div align="center" class="topnav"> 
            <h1 style = "color: black; ">REPORTE TOKENS</h1></div><br></br>
        <table align="center">
        <tr>
        <th colspan="5" style="background-color: black; color: white;">Tokens</th>
        </tr>
        <tr>
            <th colspan="1"style="background-color: black; color: white;">Lexema</th>
            <th colspan="1"style="background-color: black; color: white;">Linea</th>
            <th colspan="1"style="background-color: black; color: white;">Columna</th>
            <th colspan="1"style="background-color: black; color: white;">Tipo</th>
        </tr>
        </tr>"""
        for token in self.listaTokens:
            CuerpoHtml+= """<tr class = "table-primary">"""
            CuerpoHtml+= """<th>"""+str(token.lexema)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(token.linea)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(token.columna)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(token.tipo)+"""</th>"""
            CuerpoHtml+= """</tr>"""
        CuerpoHtml+="""</table>
        </div>
        </body>
        </html>"""
        ruta = 'ReporteTokens.html'
        archivo = open(ruta,'w')
        archivo.write(CuerpoHtml)
        startfile('ReporteTokens.html')
        print("Se ha generado el html con los reportes.")
    
    def reporteErrores(self):
        CuerpoHtml= """<!DOCTYPE html>
        <html lang=es>
        <head>
        <meta charset = "utf-8 ">
        <title>REPORTES</title>
        <style type = "text/css">
        body{
            margin: 0;
            font-family: Trebuchet MS, sans-serif;
            background-color: #fefbe9;
            background:linear-gradient(45deg,aqua,#02C7FF, #02A5FF , #0251FF , #022BFF, #6302FF,  #9402FF, #CA02FF ,#FF02F7);
        }
        .topnav {
            overflow: hidden;
            background-color: #DC143C;
            text-align: center;
        }
        table {
            border-collapse: collapse;
            width: 50%;
        }
        td, th {
            font-family: bahnschrift;
            border: 1px solid #000;
            text-align: center;
            padding: 8px;
        }
        h2{
            color: #000000;
        }</style>
        </head>
        <body>
        <div align="center" class="topnav"> 
            <h1 style = "color: black; ">REPORTE ERRORES</h1></div><br></br>
        <table align="center">
        <tr>
        <th colspan="5" style="background-color: black; color: white;">Errores</th>
        </tr>
        <tr>
            <th colspan="1"style="background-color: black; color: white;">Descripcion</th>
            <th colspan="1"style="background-color: black; color: white;">Linea</th>
            <th colspan="1"style="background-color: black; color: white;">Columna</th>
        </tr>
        </tr>"""
        for error in self.listaErrores:
            CuerpoHtml+= """<tr class = "table-primary">"""
            CuerpoHtml+= """<th>"""+str(error.descripcion)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(error.linea)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(error.columna)+"""</th>"""
            CuerpoHtml+= """</tr>"""
        CuerpoHtml+="""</table>
        </div>
        </body>
        </html>"""
        ruta = 'ReporteErrores.html'
        archivo = open(ruta,'w')
        archivo.write(CuerpoHtml)
        startfile('ReporteErrores.html')
        print("Se ha generado el html con los reportes.")