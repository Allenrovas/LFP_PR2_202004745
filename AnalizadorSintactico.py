from RespuestaBot import *
from prettytable import PrettyTable

class AnalizadorSintactico:
    
    def __init__(self,tokens : list) -> None:
        self.errores = []
        self.cadenaRetorno = ""
        self.tokens = tokens

    def agregarError(self,esperado,obtenido,columna):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {} en la columna {}'''.format(obtenido,esperado,columna)
        )

    def LimpiarCadena(self):
        self.cadenaRetorno = ""
    
    def LimpiarErrores(self):
        self.errores.clear()

    def sacarToken(self):
        ''' Saca el primer token y lo quita de la lista'''
        try:
            return self.tokens.pop(0)
        except:
            return None

    def observarToken(self):
        ''' Saca el primer token y lo mete de nuevo en de la lista'''
        try:
            return self.tokens[0]
        except:
            return None
    
    def analizar(self):
        self.S()

    def S(self):
        self.INICIO()

    def INICIO(self):
        # Observar el primer elemento para
        # decidir a donde ir
        temporal = self.observarToken()
        if temporal is None:
            self.agregarError("RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS  ","EOF",0)
            self.cadenaRetorno = "Se encontró un error sintáctico"
        elif temporal.tipo == 'RESULTADO':
            self.RESULTADO()
        elif temporal.tipo == 'JORNADA':
            self.JORNADA()
        elif temporal.tipo == 'GOLES':
            self.GOLES()
        elif temporal.tipo == 'TABLA':
            self.TABLA()
        elif temporal.tipo == 'PARTIDOS':
            self.PARTIDOS()
        elif temporal.tipo == 'TOP':
            self.TOP()
        elif temporal.tipo == 'ADIOS':
            self.ADIOS()
        else:
            self.agregarError("RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS",temporal.tipo, temporal.columna)
            self.cadenaRetorno = "Se encontró un error sintáctico"
    
    def RESULTADO(self):
        # Comando buscar un resultado
        # Producción
        #        ResultadoPartido	::=	RESULTADO cadena VS cadena TEMPORADA cadenaMayorMenorQue

        # Sacar token --- se espera RESULTADO
        token = self.sacarToken()
        if token.tipo == 'RESULTADO':
            Columna = token.columna
            # Sacar otro token --- se espera Cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("Cadena","EOF",Columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "cadenaComillas":
                Columna = token.columna
                # Sacar otro token --- se espera VS
                EquipoLocal = token.lexema
                token = self.sacarToken()
                if token is None:
                    self.agregarError("VS","EOF", Columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "VS":
                    Columna = token.columna
                    # Sacar otro token --- se espera Cadena
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("Cadena","EOF", Columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                        return
                    elif token.tipo == "cadenaComillas":
                        EquipoVisitante = token.lexema
                        Columna = token.columna
                        # Sacar otro token --- se espera TEMPORADA
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("TEMPORADA","EOF", Columna)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                            return
                        elif token.tipo == "TEMPORADA":
                            Columna = token.columna
                            # Sacar otro token --- se espera CadenaMayorMenorQue
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("cadenaMayorYMenorQue","EOF", Columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                return
                            elif token.tipo == "cadenaMayorYMenorQue":
                                ResultadoTemporada = token.lexema
                                # Si todo salió bien, llamar a la funcionalidad
                                self.cadenaRetorno = ResultadoBot(EquipoLocal,EquipoVisitante,ResultadoTemporada)
                            else:
                                self.agregarError("cadenaMayorYMenorQue",token.tipo, token.columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                        else:
                            self.agregarError("TEMPORADA",token.tipo, token.columna)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                    else:
                        self.agregarError("cadenaComillas",token.tipo, token.columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("VS",token.tipo, token.columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                self.agregarError("cadenaComillas",token.tipo, token.columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
        else:
            self.agregarError("RESULTADO","EOF",0)
            self.cadenaRetorno = "Se encontró un error sintáctico"
    
    def JORNADA(self):
        # Comando de buscar una jornada
        # Producción
        #   JORNADA ::= jornada numero temporada cadenamenorQuemayorQue (banderaF nombreArchivo)*

        # Sacar token --- se espera JORNADA
        token = self.sacarToken()
        if token.tipo == 'JORNADA':
            Columna = token.columna
            # Sacar otro token --- se espera Cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("Numero","EOF", Columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "Numero":
                Columna = token.columna
                NumeroJornada = token.lexema
                # Sacar otro token --- se espera TEMPORADA
                token = self.sacarToken()
                if token is None:
                    self.agregarError("TEMPORADA","EOF", Columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "TEMPORADA":
                    Columna = token.columna
                    # Sacar otro token --- se espera CadenaMayorMenorQue
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("cadenaMayorYMenorQue","EOF", Columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                        return
                    elif token.tipo == "cadenaMayorYMenorQue":
                        Temporada = token.lexema
                        token = self.sacarToken()
                        if token is None:
                            self.cadenaRetorno = JornadaBot(NumeroJornada,Temporada,"jornada.html")
                            # Si todo salió bien, llamar a la funcionalidad
                            return
                        elif token.tipo == "banderaF":
                            Columna = token.columna
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("NombreArchivo","EOF", Columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                return
                            elif token.tipo == "NombreArchivo":
                                nombreArchivo = token.lexema+".html"
                                self.cadenaRetorno = JornadaBot(NumeroJornada,Temporada,nombreArchivo)
                                # Si todo salió bien, llamar a la funcionalidad
                            else:
                                self.agregarError("NombreArchivo",token.tipo, token.columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                        else:
                            self.agregarError("banderaF",token.tipo, token.columna)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                        
                    else:
                        self.agregarError("cadenaMayorYMenorQue",token.tipo, token.columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("TEMPORADA",token.tipo, token.columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                self.agregarError("Numero",token.tipo, token.columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
        else:
            self.agregarError("JORNADA","EOF",0)
            self.cadenaRetorno = "Se encontró un error sintáctico"
    
    def GOLES(self):
        # Comando para buscar goles de un equipo
        # Producción
        #        Goles	::=	GOLES CONDICION cadena TEMPORADA cadenaMayorMenorQue

        # Sacar token --- se espera GOLES
        token = self.sacarToken()
        if token.tipo == 'GOLES':
            Columna = token.columna
            # Sacar otro token --- se espera CONDICION_GOLES
            token = self.sacarToken()
            if token is None:
                self.agregarError("CONDICION_GOLES","EOF",Columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "CONDICION_GOLES":
                Condicion = token.lexema
                Columna = token.columna
                # Sacar otro token --- se espera cadena
                token = self.sacarToken()
                if token is None:
                    self.agregarError("cadenaComillas","EOF",Columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "cadenaComillas":
                    Columna = token.columna
                    Equipo = token.lexema
                    # Sacar otro token --- se espera TEMPORADA
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("TEMPORADA","EOF",Columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                        return
                    elif token.tipo == "TEMPORADA":
                        Columna = token.columna
                        # Sacar otro token --- se espera CadenaMayorMenorQue
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("cadenaMayorYMenorQue","EOF",Columna)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                            return
                        elif token.tipo == "cadenaMayorYMenorQue":
                            Temporada = token.lexema
                            # Si todo salió bien, llamar a la funcionalidad
                            self.cadenaRetorno = GolesBot(Condicion,Equipo,Temporada)
                        else:
                            self.agregarError("cadenaMayorYMenorQue",token.tipo, token.columna)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                    else:
                        self.agregarError("TEMPORADA",token.tipo, token.columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("cadenaComillas",token.tipo, token.columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                self.agregarError("CONDICION_GOLES",token.tipo, token.columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
        else:
            self.agregarError("GOLES","EOF",0)
            self.cadenaRetorno = "Se encontró un error sintáctico"
    
    def TABLA(self):
        # Comando para la tabla de posiciones de una temporada
        # Producción
        # TABLA ::= tabla temporada cadenamenorQuemayorQue (banderaF nombreArchivo)*

        # Sacar token --- se espera GOLES
        token = self.sacarToken()
        if token.tipo == 'TABLA':
            Columna = token.columna
            # Sacar otro token --- se espera TEMPORADA
            token = self.sacarToken()
            if token is None:
                self.agregarError("TEMPORADA","EOF",Columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "TEMPORADA":
                Columna = token.columna
                # Sacar otro token --- se espera CadenaMayorMenorQue
                token = self.sacarToken()
                if token is None:
                    self.agregarError("cadenaMayorYMenorQue","EOF",Columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "cadenaMayorYMenorQue":
                    Temporada = token.lexema
                    token = self.sacarToken()
                    if token is None:
                        self.cadenaRetorno = TablaBot(Temporada,"temporada.html")
                        # Si todo salió bien, llamar a la funcionalidad
                        return
                    elif token.tipo == "banderaF":
                        Columna = token.columna
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("NombreArchivo","EOF",Columna)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                            return
                        elif token.tipo == "NombreArchivo":
                            nombreArchivo = token.lexema+".html"
                            self.cadenaRetorno = TablaBot(Temporada,nombreArchivo)
                            # Si todo salió bien, llamar a la funcionalidad
                        else:
                            self.agregarError("NombreArchivo",token.tipo, token.columna)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                    else:
                        self.agregarError("banderaF",token.tipo, token.columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("cadenaMayorYMenorQue",token.tipo, token.columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                self.agregarError("TEMPORADA",token.tipo, token.columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"

    def PARTIDOS(self):
        # Comando para la tabla de posiciones de una temporada
        # Producción
        # PARTIDOS ::= partidos cadena temporada cadenamenorQuemayorQue (banderaF nombreArchivo)* (banderaJi numero)* (banderaJf numero)*
        # Sacar token --- se espera GOLES
        token = self.sacarToken()
        if token.tipo == 'PARTIDOS':
            Columna = token.columna
            # Sacar otro token --- se espera cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("cadenaComillas","EOF", Columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "cadenaComillas":
                Equipo = token.lexema
                Columna = token.columna
                # Sacar otro token --- se espera TEMPORADA
                token = self.sacarToken()
                if token is None:
                    self.agregarError("TEMPORADA","EOF",Columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "TEMPORADA":
                    Columna = token.columna
                    # Sacar otro token --- se espera CadenaMayorMenorQue
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("cadenaMayorYMenorQue","EOF", Columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                        return
                    elif token.tipo == "cadenaMayorYMenorQue":
                        Temporada = token.lexema
                        # Si todo salió bien, llamar a la funcionalidad
                        token = self.sacarToken()
                        if token is None:
                            #Funcionalidad
                            self.cadenaRetorno = PartidosBot(Equipo,Temporada,"partidos.html",1,0)
                            return
                        elif token.tipo == "banderaF":
                            Columna = token.columna
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("NombreArchivo","EOF", Columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                return
                            elif token.tipo == "NombreArchivo":
                                nombreArchivo = token.lexema+".html"
                                token = self.sacarToken()
                                if token is None:
                                    #funcionalidad
                                    self.cadenaRetorno = PartidosBot(Equipo,Temporada,nombreArchivo,1,0)
                                    return
                                elif token.tipo == "banderaJi":
                                    Columna = token.columna
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("Numero","EOF", Columna)
                                        self.cadenaRetorno = "Se encontró un error sintáctico"
                                        return
                                    elif token.tipo == "Numero":
                                        NumeroJi = token.lexema
                                        token = self.sacarToken()
                                        if token is None:
                                            #funcionalidad
                                            self.cadenaRetorno = PartidosBot(Equipo,Temporada,nombreArchivo,NumeroJi,0)
                                            return
                                        elif token.tipo == "banderaJf":
                                            Columna = token.columna
                                            token = self.sacarToken()
                                            if token is None:
                                                self.agregarError("Numero","EOF", Columna)
                                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                                return
                                            elif token.tipo == "Numero":
                                                NumeroJf = token.lexema
                                                #funcionalidad
                                                self.cadenaRetorno = PartidosBot(Equipo,Temporada,nombreArchivo,NumeroJi,NumeroJf)
                                                return
                                            else:
                                                self.agregarError("Numero",token.tipo, token.columna)
                                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                        else:
                                            self.agregarError("banderaJf",token.tipo, token.columna)
                                            self.cadenaRetorno = "Se encontró un error sintáctico"
                                    else:
                                        self.agregarError("Numero",token.tipo, token.columna)
                                        self.cadenaRetorno = "Se encontró un error sintáctico"
                                elif token.tipo == "banderaJf":
                                    Columna = token.columna
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("Numero","EOF", Columna)
                                        self.cadenaRetorno = "Se encontró un error sintáctico"
                                        return
                                    elif token.tipo == "Numero":
                                        NumeroJf = token.lexema
                                        #funcionalidad
                                        self.cadenaRetorno = PartidosBot(Equipo,Temporada,nombreArchivo,1,NumeroJf)
                                        return
                                    else:
                                        self.agregarError("Numero",token.tipo, token.columna)
                                        self.cadenaRetorno = "Se encontró un error sintáctico"
                                else:
                                    self.agregarError("banderaJi | bandera Jf",token.tipo, token.columna)
                                    self.cadenaRetorno = "Se encontró un error sintáctico"
                            else:
                                self.agregarError("NombreArchivo",token.tipo, token.columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                        elif token.tipo == "banderaJi":
                            Columna = token.columna
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("Numero","EOF", Columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                return
                            elif token.tipo == "Numero":
                                NumeroJi = token.lexema
                                token = self.sacarToken()
                                if token is None:
                                    #funcionalidad
                                    self.cadenaRetorno = PartidosBot(Equipo,Temporada,"partidos.html",NumeroJi,0)
                                    return
                                elif token.tipo == "banderaJf":
                                    Columna = token.columna
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("Numero","EOF", Columna)
                                        self.cadenaRetorno = "Se encontró un error sintáctico"
                                        return
                                    elif token.tipo == "Numero":
                                        NumeroJf = token.lexema
                                        #funcionalidad
                                        self.cadenaRetorno = PartidosBot(Equipo,Temporada,"partidos.html",NumeroJi,NumeroJf)
                                        return
                                    else:
                                        self.agregarError("Numero",token.tipo, token.columna)
                                        self.cadenaRetorno = "Se encontró un error sintáctico"
                                else:
                                    self.agregarError("banderaJf",token.tipo, token.columna)
                                    self.cadenaRetorno = "Se encontró un error sintáctico"
                            else:
                                self.agregarError("Numero",token.tipo, token.columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"

                        elif token.tipo == "banderaJf":
                            Columna = token.columna
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("Numero","EOF", Columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                return
                            elif token.tipo == "Numero":
                                NumeroJf = token.lexema
                                #funcionalidad
                                self.cadenaRetorno = PartidosBot(Equipo,Temporada,"partidos.html",1,NumeroJf)
                                return
                            else:
                                self.agregarError("Numero",token.tipo, token.columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                        else:
                            self.agregarError("banderaF | banderaJi | bandera JF",token.tipo, token.columna)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                    else:
                        self.agregarError("cadenaMayorYMenorQue",token.tipo, token.columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("TEMPORADA",token.tipo, token.columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                    self.agregarError("cadenaComillas",token.tipo, token.columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
        else:
            self.agregarError("PARTIDOS",token.tipo, token.columna)
            self.cadenaRetorno = "Se encontró un error sintáctico"

    def TOP(self):
        # Comando para el top de equipos de una temporada
        # Producción
        #TOP ::= top CONDICION_TOP temporada cadenamenorQuemayorQue (banderaN numero)*
        # Sacar token --- se espera TOP
        token = self.sacarToken()
        if token.tipo == "TOP":
            Columna = token.columna
            # Sacar token --- se espera CONDICION_TOP
            token = self.sacarToken()
            if token is None:
                self.agregarError("CONDICION_TOP","EOF",Columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "CONDICION_TOP":
                Condicion = token.lexema
                Columna = token.columna
                # Sacar token --- se espera temporada
                token = self.sacarToken()
                if token is None:
                    self.agregarError("TEMPORADA","EOF", Columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "TEMPORADA":
                    Columna = token.columna
                    # Sacar token --- se espera cadenamenorQuemayorQue
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("cadenaMayorYMenorQue","EOF", Columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                        return
                    elif token.tipo == "cadenaMayorYMenorQue":
                        Temporada = token.lexema
                        # Sacar token --- se espera banderaN 
                        token = self.sacarToken()
                        if token is None:
                            self.cadenaRetorno = TopBot(Condicion,Temporada,5)
                            return
                        elif token.tipo == "banderaN":
                            Columna = token.columna
                            # sacar otro token --- se espera numero
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("Numero","EOF", Columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                return
                            elif token.tipo == "Numero":
                                Numero = token.lexema
                                self.cadenaRetorno = TopBot(Condicion,Temporada,Numero)
                                return
                            else:
                                self.agregarError("Numero",token.tipo, token.columna)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                        else:
                            self.agregarError("banderaN",token.tipo, token.columna)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                    else:
                        self.agregarError("cadenaMayorYMenorQue",token.tipo, token.columna)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("TEMPORADA",token.tipo, token.columna)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                self.agregarError("CONDICION_TOP",token.tipo, token.columna)
                self.cadenaRetorno = "Se encontró un error sintáctico"
        else:
            self.agregarError("TOP",token.tipo, token.columna)
            self.cadenaRetorno = "Se encontró un error sintáctico"

    def ADIOS(self):
        # Comando para salir del programa
        # Producción
        #ADIOS ::= adios
        # Sacar token --- se espera ADIOS
        token = self.sacarToken()
        if token.tipo == "ADIOS":
            self.cadenaRetorno = "Adios"
            return
        else:
            self.agregarError("ADIOS",token.tipo,token.columna)
            self.cadenaRetorno = "Se encontró un error sintáctico"

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion"]
        for error_ in self.errores:
            x.add_row([error_])
        print(x)
        