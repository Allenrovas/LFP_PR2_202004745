from ast import Pass
import csv
from Jornada import Jornada
from os import system, startfile
from Partidos import Partidos
import codecs


ListaJornadas = []
# Función para abrir el archivo y leerlo, cargar los datos en la lista
with open('LaLigaBot-LFP.csv',encoding="utf-8") as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    Contador = 0
    for row in reader:
        if Contador == 0:
            pass
        else:
            NuevaJornada = Jornada(row[1],row[2],row[3],row[4],row[5],row[6])
            ListaJornadas.append(NuevaJornada)
        Contador += 1

def GenerarHtmlJornada(ListaJornadaAuxiliar, nombreArchivo):

    CuerpoHtml= """<!DOCTYPE html>
    <html lang=es>
    <head>
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
    <h1 style = "color: black; ">REPORTE JORNADA</h1></div><br></br>
    <table align="center">
    <tr>
    <th colspan="5" style="background-color: black; color: white;">Jornada """+str(ListaJornadaAuxiliar[0].jornada)+" de la Temporada "+str(ListaJornadaAuxiliar[0].temporada)
    CuerpoHtml+="""</th>
    </tr>
    <tr>
    <th colspan="1"style="background-color: black; color: white;">Equipo Local</th>
    <th colspan="1"style="background-color: black; color: white;">Equipo Visitantes</th>
    <th colspan="1"style="background-color: black; color: white;">Goles Local</th>
    <th colspan="1"style="background-color: black; color: white;">Goles Visitante</th>
    </tr>
    </tr>"""
    for jornada in ListaJornadaAuxiliar:
        CuerpoHtml+= """<tr class = "table-primary">"""
        CuerpoHtml+= """<th>"""+str(jornada.equipo1)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(jornada.equipo2)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(jornada.goles1)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(jornada.goles2)+"""</th>"""
        CuerpoHtml+= """</tr>"""
    CuerpoHtml+="""</table>
    </div>
    </body>
    </html>"""
    ruta = nombreArchivo
    archivo = open(ruta,'w')
    archivo.write(CuerpoHtml)
    startfile(nombreArchivo)
    print("Se ha generado el html con los reportes.")
    
def GenerarHtmlTabla(ListaEquipos, nombreArchivo,Temporada):
    
    tamaño=len(ListaEquipos)
    i=0
    while i < tamaño - 1:
        j=0
        while j < tamaño - 1:
            if ListaEquipos[j].puntos < ListaEquipos[j+1].puntos:
                temp = ListaEquipos[j+1]
                ListaEquipos[j+1] = ListaEquipos[j]
                ListaEquipos[j] = temp
            j+=1
        i+=1

    CuerpoHtml= """<!DOCTYPE html>
    <html lang=es>
    <head>
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
    <h1 style = "color: black; ">REPORTE TABLA</h1></div><br></br>
    <table align="center">
    <tr>
    <th colspan="2" style="background-color: black; color: white;">Temporada """+str(Temporada)
    CuerpoHtml+="""</th>
    </tr>
    <tr>
    <th colspan="1"style="background-color: black; color: white;">Equipo</th>
    <th colspan="1"style="background-color: black; color: white;">Puntos</th>
    </tr>
    </tr>"""
    for equipo in ListaEquipos:
        CuerpoHtml+= """<tr class = "table-primary">"""
        CuerpoHtml+= """<th>"""+str(equipo.equipo)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(equipo.puntos)+"""</th>"""
        CuerpoHtml+= """</tr>"""
    CuerpoHtml+="""</table>
    </div>
    </body>
    </html>"""
    ruta = nombreArchivo
    archivo = open(ruta,'w')
    archivo.write(CuerpoHtml)
    startfile(nombreArchivo)
    print("Se ha generado el html con los reportes.")

def GenerarHtmlPartidos(ListaPartidos, nombreArchivo, Temporada, Equipo):
    CuerpoHtml= """<!DOCTYPE html>
    <html lang=es>
    <head>
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
    <h1 style = "color: black; ">REPORTE PARTIDOS</h1></div><br></br>
    <table align="center">
    <tr>
    <th colspan="5" style="background-color: black; color: white;">Temporada """+str(Temporada)+" del equipo "+str(Equipo)
    CuerpoHtml+="""</th>
    </tr>
    <tr>
    <th colspan="1"style="background-color: black; color: white;">Jornada</th>
    <th colspan="1"style="background-color: black; color: white;">Equipo Local</th>
    <th colspan="1"style="background-color: black; color: white;">Equipo Visitante</th>
    <th colspan="1"style="background-color: black; color: white;">Goles Local</th>
    <th colspan="1"style="background-color: black; color: white;">Goles Visita</th>
    </tr>
    </tr>"""
    for equipo in ListaPartidos:
        CuerpoHtml+= """<tr class = "table-primary">"""
        CuerpoHtml+= """<th>"""+str(equipo.jornada)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(equipo.equipo1)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(equipo.equipo2)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(equipo.goles1)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(equipo.goles2)+"""</th>"""
        CuerpoHtml+= """</tr>"""
    CuerpoHtml+="""</table>
    </div>
    </body>
    </html>"""
    ruta = nombreArchivo
    archivo = open(ruta,'w')
    archivo.write(CuerpoHtml)
    startfile(nombreArchivo)
    print("Se ha generado el html con los reportes.")

def ResultadoBot(EquipoLocal,EquipoVisitante,ResultadoTemporada):
    
    EquipoLocalFuncion = ""
    EquipoVisitanteFuncion = ""
    ResultadoTemporadaFuncion = ""
    TemporadaExiste = False
    Resultado = False
    
    for Caracter in EquipoLocal:
        if Caracter == '"':
            pass
        else: 
            EquipoLocalFuncion += Caracter
    
    for Caracter in EquipoVisitante:
        if Caracter == '"':
            pass
        else: 
            EquipoVisitanteFuncion += Caracter
    
    for Caracter in ResultadoTemporada:
        if Caracter == '<' or Caracter == '>':
            pass
        else: 
            ResultadoTemporadaFuncion += Caracter
    
    for Jornada in ListaJornadas:
        if Jornada.temporada == ResultadoTemporadaFuncion:
            TemporadaExiste = True
            if Jornada.equipo1 == EquipoLocalFuncion and Jornada.equipo2 == EquipoVisitanteFuncion:
                Resultado = True
                Cadena ="El resultado de este partido fue: "+Jornada.equipo1+" "+str(Jornada.goles1)+" - "+Jornada.equipo2+" "+str(Jornada.goles2)
                return Cadena
            else:
                CadenaEquipo = "No se encontró algún resultado para el partido de "+EquipoLocalFuncion+" vs "+EquipoVisitanteFuncion
        else:
            CadenaTemporada = "No se encontró alguna Temporada"
    
    if TemporadaExiste == False:
        return CadenaTemporada
    
    if Resultado == False and TemporadaExiste == True:
        return CadenaEquipo
       
def JornadaBot(NumeroJornada,Temporada,nombreArchivo):
    
    ListaJornadaAuxiliar = []
    ResultadoTemporadaFuncion = ""
    JornadaEncontrada = False
    TemporadaExiste = False

    for Caracter in Temporada:
        if Caracter == '<' or Caracter == '>':
            pass
        else: 
            ResultadoTemporadaFuncion += Caracter
    
    for Jornada in ListaJornadas:
        if Jornada.temporada == ResultadoTemporadaFuncion:
            TemporadaExiste = True
            if Jornada.jornada == NumeroJornada:
                CadenaGenerar = "Generando archivo de resultados jornada "+str(NumeroJornada)+"de la temporada "+Jornada.temporada
                ListaJornadaAuxiliar.append(Jornada)
                JornadaEncontrada = True
            else: 
                pass
        else:
            pass
    
    if JornadaEncontrada == True:
        GenerarHtmlJornada(ListaJornadaAuxiliar,nombreArchivo)
        ListaJornadaAuxiliar.clear()
        return CadenaGenerar
    
    if JornadaEncontrada == False and TemporadaExiste == True:
        Cadena = "No se encontró alguna jornada"
        return Cadena
    
    if TemporadaExiste == False:
        Cadena = "No se encontró alguna temporada"
        return Cadena

def GolesBot(Condicion,Equipo,Temporada):

    ResultadoTemporadaFuncion = ""
    EquipoFuncion = ""
    EquipoEncontrado = False
    TemporadaExiste = False
    GolesLocal = 0
    GolesVisitante = 0
    GolesTotal = 0

    for Caracter in Temporada:
        if Caracter == '<' or Caracter == '>':
            pass
        else: 
            ResultadoTemporadaFuncion += Caracter
    
    for Caracter in Equipo:
        if Caracter == '"':
            pass
        else: 
            EquipoFuncion += Caracter
    
    if Condicion == "LOCAL":
        for Jornada in ListaJornadas:
            if Jornada.temporada == ResultadoTemporadaFuncion:
                TemporadaExiste = True
                if Jornada.equipo1 == EquipoFuncion:
                    EquipoEncontrado = True
                    GolesLocal += int(Jornada.goles1)
                    Cadena = "El equipo "+EquipoFuncion+" tiene "+str(GolesLocal)+" goles de local en la temporada "+str(Jornada.temporada)
                else:
                    pass
            else:
                pass

        if EquipoEncontrado == True:
            return Cadena
        
        if EquipoEncontrado == False and TemporadaExiste == True:
            Cadena = "No se encontró algún equipo"
            return Cadena
        
        if TemporadaExiste == False:
            Cadena = "No se encontró alguna temporada"
            return Cadena


    elif Condicion == "VISITANTE":
        for Jornada in ListaJornadas:
            if Jornada.temporada == ResultadoTemporadaFuncion:
                TemporadaExiste = True
                if Jornada.equipo2 == EquipoFuncion:
                    EquipoEncontrado = True
                    GolesVisitante += int(Jornada.goles2)
                    Cadena = "El equipo "+EquipoFuncion+" tiene "+str(GolesVisitante)+" goles de visitante en la temporada "+str(Jornada.temporada)
                else:
                    pass
            else:
                pass
            
        if EquipoEncontrado == True:
            return Cadena
        
        if EquipoEncontrado == False and TemporadaExiste == True:
            Cadena = "No se encontró algún equipo"
            return Cadena
        
        if TemporadaExiste == False:
            Cadena = "No se encontró alguna temporada"
            return Cadena


    elif Condicion == "TOTAL":
        for Jornada in ListaJornadas:
            if Jornada.temporada == ResultadoTemporadaFuncion:
                TemporadaExiste = True
                if Jornada.equipo1 == EquipoFuncion:
                    EquipoEncontrado = True
                    GolesLocal = Jornada.goles1
                    GolesTotal += int(GolesLocal)
                    Cadena = "El equipo "+EquipoFuncion+" tiene "+str(GolesTotal)+" goles totales en la temporada "+str(Jornada.temporada)
                elif Jornada.equipo2 == EquipoFuncion:
                    EquipoEncontrado = True
                    GolesVisitante = Jornada.goles2
                    GolesTotal += int(GolesVisitante)
                    Cadena = "El equipo "+EquipoFuncion+" tiene "+str(GolesTotal)+" goles totales en la temporada "+str(Jornada.temporada)
                else:
                    pass
            else:
                pass
            
        if EquipoEncontrado == True:
            return Cadena
        
        if EquipoEncontrado == False and TemporadaExiste == True:
            Cadena = "No se encontró algún equipo"
            return Cadena
        
        if TemporadaExiste == False:
            Cadena = "No se encontró alguna temporada"
            return Cadena

    else:
        Cadena = "No se encontró alguna condición válida"
        return Cadena
    
def TablaBot(Temporada, NombreArchivo):
    
    ResultadoTemporadaFuncion = ""
    TemporadaExiste = False
    ListaEquipos = []
    for Caracter in Temporada:
        if Caracter == '<' or Caracter == '>':
            pass
        else: 
            ResultadoTemporadaFuncion += Caracter
    
    for Jornada in ListaJornadas:
        if Jornada.temporada == ResultadoTemporadaFuncion:
            TemporadaExiste = True
            if Jornada.jornada == "1":
                ListaEquipos.append(Partidos(Jornada.equipo1,0))
                ListaEquipos.append(Partidos(Jornada.equipo2,0))
                Cadena = "Generando tabla de posiciones de la temporada "+str(Jornada.temporada)

    for Jornada in ListaJornadas:
        if Jornada.temporada == ResultadoTemporadaFuncion:
            if int(Jornada.goles1) > int(Jornada.goles2):
                for equipo in ListaEquipos:
                    if equipo.equipo == Jornada.equipo1:
                        equipo.puntos += 3
            elif int(Jornada.goles1) < int(Jornada.goles2):
                for equipo in ListaEquipos:
                    if equipo.equipo == Jornada.equipo2:
                        equipo.puntos += 3
            else:
                for equipo in ListaEquipos:
                    if equipo.equipo == Jornada.equipo1:
                        equipo.puntos += 1
                    if equipo.equipo == Jornada.equipo2:
                        equipo.puntos += 1
        else:
            pass

    if TemporadaExiste == True:
        GenerarHtmlTabla(ListaEquipos, NombreArchivo, ResultadoTemporadaFuncion)
        return Cadena
    else:
        Cadena = "No se encontró alguna temporada"
        return Cadena

def PartidosBot(Equipo, Temporada, nombreArchivo, JornadaInicial, JornadaFinal):
    ResultadoTemporadaFuncion = ""
    EquipoFuncion = ""
    TemporadaExiste = False
    EquipoEncontrado = False
    ListaJornadasEquipo = []
    ListaAuxiliar = []
    

    for Caracter in Temporada:
        if Caracter == '<' or Caracter == '>':
            pass
        else: 
            ResultadoTemporadaFuncion += Caracter
    
    for Caracter in Equipo:
        if Caracter == '"':
            pass
        else: 
            EquipoFuncion += Caracter
    
    JornadaInicial = int(JornadaInicial)
    
    for Jornada in ListaJornadas:
        if Jornada.temporada == ResultadoTemporadaFuncion:
            TemporadaExiste = True
            if Jornada.equipo1 == EquipoFuncion or Jornada.equipo2 == EquipoFuncion:
                EquipoEncontrado = True
                ListaJornadasEquipo.append(Jornada)
        else:
            pass
 
    
    if JornadaFinal == 0:
        JornadaFinalAux = len(ListaJornadasEquipo)
    else:
        JornadaFinalAux = int(JornadaFinal)
    
    print(JornadaFinalAux, JornadaInicial)
    
    for Jornada in ListaJornadasEquipo:
        if int(Jornada.jornada) >= JornadaInicial and int(Jornada.jornada) <= JornadaFinalAux:
            ListaAuxiliar.append(Jornada)
        else:
            pass
    
    if EquipoEncontrado == True:
        GenerarHtmlPartidos(ListaAuxiliar, nombreArchivo, ResultadoTemporadaFuncion, EquipoFuncion)
        Cadena = "Generando partidos de la temporada "+str(ResultadoTemporadaFuncion)+" del equipo "+str(EquipoFuncion)
        return Cadena
    
    if TemporadaExiste == False:
        Cadena = "No se encontró alguna temporada"
        return Cadena
    
    if TemporadaExiste == True and EquipoEncontrado == False:
        Cadena = "No se encontró algún equipo"
        return Cadena

def TopBot(Condicion, Temporada, Cantidad):
    
    ResultadoTemporadaFuncion = ""
    TemporadaExiste = False
    ListaEquipos = []
    ListaAuxiliar = []

    for Caracter in Temporada:
        if Caracter == '<' or Caracter == '>':
            pass
        else: 
            ResultadoTemporadaFuncion += Caracter
    
    for Jornada in ListaJornadas:
        if Jornada.temporada == ResultadoTemporadaFuncion:
            TemporadaExiste = True
            if Jornada.jornada == "1":
                ListaEquipos.append(Partidos(Jornada.equipo1,0))
                ListaEquipos.append(Partidos(Jornada.equipo2,0))

    for Jornada in ListaJornadas:
        if Jornada.temporada == ResultadoTemporadaFuncion:
            if int(Jornada.goles1) > int(Jornada.goles2):
                for equipo in ListaEquipos:
                    if equipo.equipo == Jornada.equipo1:
                        equipo.puntos += 3
            elif int(Jornada.goles1) < int(Jornada.goles2):
                for equipo in ListaEquipos:
                    if equipo.equipo == Jornada.equipo2:
                        equipo.puntos += 3
            else:
                for equipo in ListaEquipos:
                    if equipo.equipo == Jornada.equipo1:
                        equipo.puntos += 1
                    if equipo.equipo == Jornada.equipo2:
                        equipo.puntos += 1
        else:
            pass
    
    if Condicion == "SUPERIOR":
        tamaño=len(ListaEquipos)
        i=0
        while i < tamaño - 1:
            j=0
            while j < tamaño - 1:
                if ListaEquipos[j].puntos < ListaEquipos[j+1].puntos:
                    temp = ListaEquipos[j+1]
                    ListaEquipos[j+1] = ListaEquipos[j]
                    ListaEquipos[j] = temp
                j+=1
            i+=1
        Cadena = "Generando Top superior de la temporada "+str(ResultadoTemporadaFuncion)+":\n"
        
    elif Condicion == "INFERIOR":

        tamaño=len(ListaEquipos)
        i=0
        while i < tamaño - 1:
            j=0
            while j < tamaño - 1:
                if ListaEquipos[j].puntos > ListaEquipos[j+1].puntos:
                    temp = ListaEquipos[j+1]
                    ListaEquipos[j+1] = ListaEquipos[j]
                    ListaEquipos[j] = temp
                j+=1
            i+=1
        Cadena = "Generando Top inferior de la temporada "+str(ResultadoTemporadaFuncion)+":\n"
        
    '''Contador = 0
    for ListaEquipos in range(0, int(Cantidad)):
        Cadena += str(Contador)+ListaEquipos.equipo+"\n"
        Contador += 1'''

    Contador = 1
    Inferior = len(ListaEquipos) 
    if int(Cantidad) <=5 and int(Cantidad) > 0:
        for equipo in ListaEquipos:
            if Contador <= int(Cantidad):
                if Condicion == "SUPERIOR":
                    Cadena += str(Contador)+". "+equipo.equipo+"\n"
                elif Condicion == "INFERIOR":
                    Cadena += str(Inferior)+". "+equipo.equipo+"\n"
                    Inferior -= 1
                Contador += 1
            else:
                break
    
    else:
        Cadena = "No se puede generar el Top porque la cantidad de equipos es mayor a 5 o menor a Cero"
        return Cadena 

    if TemporadaExiste == True:    
        return Cadena
    else:
        Cadena = "No se encontró alguna temporada"
        return Cadena
    