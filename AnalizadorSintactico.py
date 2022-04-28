from RespuestaBot import *
from prettytable import PrettyTable

class AnalizadorSintactico:
    
    def __init__(self,tokens : list) -> None:
        self.errores = []
        self.cadenaRetorno = ""
        self.tokens = tokens

    def agregarError(self,esperado,obtenido):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {}'''.format(obtenido,esperado)
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
            self.agregarError("RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS  ","EOF")
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
            self.agregarError("RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS",temporal.tipo)
            self.cadenaRetorno = "Se encontró un error sintáctico"
    
    def RESULTADO(self):
        # Comando buscar un resultado
        # Producción
        #        ResultadoPartido	::=	RESULTADO cadena VS cadena TEMPORADA cadenaMayorMenorQue

        # Sacar token --- se espera RESULTADO
        token = self.sacarToken()
        if token.tipo == 'RESULTADO':
            # Sacar otro token --- se espera Cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("Cadena","EOF")
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "cadenaComillas":
                # Sacar otro token --- se espera VS
                EquipoLocal = token.lexema
                token = self.sacarToken()
                if token is None:
                    self.agregarError("VS","EOF")
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "VS":
                    # Sacar otro token --- se espera Cadena
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("Cadena","EOF")
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                        return
                    elif token.tipo == "cadenaComillas":
                        EquipoVisitante = token.lexema
                        # Sacar otro token --- se espera TEMPORADA
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("TEMPORADA","EOF")
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                            return
                        elif token.tipo == "TEMPORADA":
                            # Sacar otro token --- se espera CadenaMayorMenorQue
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("cadenaMayorYMenorQue","EOF")
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                return
                            elif token.tipo == "cadenaMayorYMenorQue":
                                ResultadoTemporada = token.lexema
                                # Si todo salió bien, llamar a la funcionalidad
                                self.cadenaRetorno = ResultadoBot(EquipoLocal,EquipoVisitante,ResultadoTemporada)
                            else:
                                self.agregarError("cadenaMayorYMenorQue",token.tipo)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                        else:
                            self.agregarError("TEMPORADA",token.tipo)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                    else:
                        self.agregarError("cadenaComillas",token.tipo)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("VS",token.tipo)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                self.agregarError("cadenaComillas",token.tipo)
                self.cadenaRetorno = "Se encontró un error sintáctico"
        else:
            self.agregarError("RESULTADO","EOF")
            self.cadenaRetorno = "Se encontró un error sintáctico"
    
    def JORNADA(self):
        # Comando de buscar una jornada
        # Producción
        #   JORNADA ::= jornada numero temporada cadenamenorQuemayorQue (banderaF nombreArchivo)*

        # Sacar token --- se espera JORNADA
        token = self.sacarToken()
        if token.tipo == 'JORNADA':
            # Sacar otro token --- se espera Cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("Numero","EOF")
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "Numero":
                NumeroJornada = token.lexema
                # Sacar otro token --- se espera TEMPORADA
                token = self.sacarToken()
                if token is None:
                    self.agregarError("TEMPORADA","EOF")
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "TEMPORADA":
                    # Sacar otro token --- se espera CadenaMayorMenorQue
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("cadenaMayorYMenorQue","EOF")
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
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("NombreArchivo","EOF")
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                                return
                            elif token.tipo == "NombreArchivo":
                                nombreArchivo = token.lexema+".html"
                                self.cadenaRetorno = JornadaBot(NumeroJornada,Temporada,nombreArchivo)
                                # Si todo salió bien, llamar a la funcionalidad
                            else:
                                self.agregarError("NombreArchivo",token.tipo)
                                self.cadenaRetorno = "Se encontró un error sintáctico"
                        else:
                            self.agregarError("banderaF",token.tipo)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                        
                    else:
                        self.agregarError("cadenaMayorYMenorQue",token.tipo)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("TEMPORADA",token.tipo)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                self.agregarError("Numero",token.tipo)
                self.cadenaRetorno = "Se encontró un error sintáctico"
        else:
            self.agregarError("JORNADA","EOF")
            self.cadenaRetorno = "Se encontró un error sintáctico"
    
    def GOLES(self):
        # Comando para buscar goles de un equipo
        # Producción
        #        Goles	::=	GOLES CONDICION cadena TEMPORADA cadenaMayorMenorQue

        # Sacar token --- se espera GOLES
        token = self.sacarToken()
        if token.tipo == 'GOLES':
            # Sacar otro token --- se espera CONDICION_GOLES
            token = self.sacarToken()
            if token is None:
                self.agregarError("CONDICION_GOLES","EOF")
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "CONDICION_GOLES":
                Condicion = token.lexema
                # Sacar otro token --- se espera cadena
                token = self.sacarToken()
                if token is None:
                    self.agregarError("cadenaComillas","EOF")
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "cadenaComillas":
                    Equipo = token.lexema
                    # Sacar otro token --- se espera TEMPORADA
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("TEMPORADA","EOF")
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                        return
                    elif token.tipo == "TEMPORADA":
                        # Sacar otro token --- se espera CadenaMayorMenorQue
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("cadenaMayorYMenorQue","EOF")
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                            return
                        elif token.tipo == "cadenaMayorYMenorQue":
                            Temporada = token.lexema
                            # Si todo salió bien, llamar a la funcionalidad
                            self.cadenaRetorno = GolesBot(Condicion,Equipo,Temporada)
                        else:
                            self.agregarError("cadenaMayorYMenorQue",token.tipo)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                    else:
                        self.agregarError("TEMPORADA",token.tipo)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("cadenaComillas",token.tipo)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                self.agregarError("CONDICION_GOLES",token.tipo)
                self.cadenaRetorno = "Se encontró un error sintáctico"
        else:
            self.agregarError("GOLES","EOF")
            self.cadenaRetorno = "Se encontró un error sintáctico"
    
    def TABLA(self):
        # Comando para la tabla de posiciones de una temporada
        # Producción
        # TABLA ::= tabla temporada cadenamenorQuemayorQue (banderaF nombreArchivo)*

        # Sacar token --- se espera GOLES
        token = self.sacarToken()
        if token.tipo == 'TABLA':
            # Sacar otro token --- se espera TEMPORADA
            token = self.sacarToken()
            if token is None:
                self.agregarError("TEMPORADA","EOF")
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "TEMPORADA":
                # Sacar otro token --- se espera CadenaMayorMenorQue
                token = self.sacarToken()
                if token is None:
                    self.agregarError("cadenaMayorYMenorQue","EOF")
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
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("NombreArchivo","EOF")
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                            return
                        elif token.tipo == "NombreArchivo":
                            nombreArchivo = token.lexema+".html"
                            self.cadenaRetorno = TablaBot(Temporada,nombreArchivo)
                            # Si todo salió bien, llamar a la funcionalidad
                        else:
                            self.agregarError("NombreArchivo",token.tipo)
                            self.cadenaRetorno = "Se encontró un error sintáctico"
                    else:
                        self.agregarError("banderaF",token.tipo)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("cadenaMayorYMenorQue",token.tipo)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                self.agregarError("TEMPORADA",token.tipo)
                self.cadenaRetorno = "Se encontró un error sintáctico"

    def PARTIDOS(self):
        # Comando para la tabla de posiciones de una temporada
        # Producción
        # PARTIDOS ::= partidos cadena temporada cadenamenorQuemayorQue (banderaF nombreArchivo)* (banderaJi numero)* (banderaJf numero)*
        # Sacar token --- se espera GOLES
        token = self.sacarToken()
        if token.tipo == 'PARTIDOS':
            # Sacar otro token --- se espera cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("cadenaComillas","EOF")
                self.cadenaRetorno = "Se encontró un error sintáctico"
                return
            elif token.tipo == "cadenaComillas":
                Equipo = token.lexema
                # Sacar otro token --- se espera TEMPORADA
                token = self.sacarToken()
                if token is None:
                    self.agregarError("TEMPORADA","EOF")
                    self.cadenaRetorno = "Se encontró un error sintáctico"
                    return
                elif token.tipo == "TEMPORADA":
                    # Sacar otro token --- se espera CadenaMayorMenorQue
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("cadenaMayorYMenorQue","EOF")
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                        return
                    elif token.tipo == "cadenaMayorYMenorQue":
                        Temporada = token.lexema
                        # Si todo salió bien, llamar a la funcionalidad
                        self.cadenaRetorno = PartidosBot(Equipo,Temporada)
                    else:
                        self.agregarError("cadenaMayorYMenorQue",token.tipo)
                        self.cadenaRetorno = "Se encontró un error sintáctico"
                else:
                    self.agregarError("TEMPORADA",token.tipo)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
            else:
                    self.agregarError("cadenaComillas",token.tipo)
                    self.cadenaRetorno = "Se encontró un error sintáctico"
        else:
            self.agregarError("PARTIDOS",token.tipo)
            self.cadenaRetorno = "Se encontró un error sintáctico"
            

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion"]
        for error_ in self.errores:
            x.add_row([error_])
        print(x)