from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter import messagebox
from AnalizadorLexico import AnalizadorLexico
from os import system, startfile
from AnalizadorSintactico import AnalizadorSintactico


lexico = AnalizadorLexico()
global listaGlobalTokens
global listaGlobalErroresLexicos
global listaGlobalErroresSintacticos
global MensajeInicial
listaGlobalTokens = []
listaGlobalErroresLexicos = []
listaGlobalErroresSintacticos = []


def Enviar():
    global listaGlobalTokens
    global MensajeInicial
    global listaGlobalErroresLexicos
    global listaGlobalErroresSintacticos


    Entrada.config(state=NORMAL)
    Entrada.delete(1.0, END)
    
    CadenaAnalizar = EntradaComando.get()
    MensajeInicial +=  "\n"+"Usuario: "+CadenaAnalizar+"\n" 
    
    
    lexico.AnalizadorLexico(CadenaAnalizar)
    lexico.imprimirErrores()
    lexico.imprimirTokens()

    listaTokens = lexico.listaTokens
    listaGlobalTokens += listaTokens
    

    listaErroresLexico = lexico.listaErrores
    listaGlobalErroresLexicos += listaErroresLexico
    

    sintactico = AnalizadorSintactico(listaTokens)
    sintactico.analizar()
    sintactico.imprimirErrores()

    Cadena = sintactico.cadenaRetorno

    MensajeInicial +=  "\n"+"LaLigaBot: "+Cadena+"\n"
    Entrada.insert(1.0,MensajeInicial)
    Entrada.config(state=DISABLED)

    listaErroresSintacticos = sintactico.errores
    listaGlobalErroresSintacticos += listaErroresSintacticos

    sintactico.LimpiarCadena()
    sintactico.LimpiarErrores()
    lexico.LimpiarErrores()
    lexico.LimpiarTokens()
    

def ReporteErrores():
    global listaGlobalErroresLexicos
    global listaGlobalErroresSintacticos
    print("Botón reporte de errores")
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
    <th colspan="5" style="background-color: black; color: white;">Errores Léxicos</th>
    </tr>
    <tr>
    <th colspan="1"style="background-color: black; color: white;">Descripcion</th>
    <th colspan="1"style="background-color: black; color: white;">Linea</th>
    <th colspan="1"style="background-color: black; color: white;">Columna</th>
    </tr>
    </tr>"""
    for error in listaGlobalErroresLexicos:
        CuerpoHtml+= """<tr class = "table-primary">"""
        CuerpoHtml+= """<th>"""+str(error.descripcion)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(error.linea)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(error.columna)+"""</th>"""
        CuerpoHtml+= """</tr>"""
    CuerpoHtml+="""</table> <br> </br>
    <table align="center">
    <tr>
    <th colspan="1" style="background-color: black; color: white;">Errores Sintácticos</th>
    </tr>
    <tr>
    <th colspan="1"style="background-color: black; color: white;">Descripcion</th>
    </tr>"""
    for error in listaGlobalErroresSintacticos:
        CuerpoHtml+= """<tr class = "table-primary">"""
        CuerpoHtml+= """<th>"""+str(error)+"""</th>"""
        CuerpoHtml+= """</tr>"""
    CuerpoHtml+="""</table></div>
    </body>
    </html>"""
    ruta = 'ReporteErrores.html'
    archivo = open(ruta,'w')
    archivo.write(CuerpoHtml)
    startfile('ReporteErrores.html')
    print("Se ha generado el html con los reportes.")

def LimpiarErrores():
    global listaGlobalErroresLexicos
    global listaGlobalErroresSintacticos
    print("Botón limpiar errores")
    listaGlobalErroresLexicos.clear()
    listaGlobalErroresSintacticos.clear()

def ReporteTokens():
    global listaGlobalTokens
    print("Botón reporte de tokens")
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
    for token in listaGlobalTokens:
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

def LimpiarTokens():
    global listaGlobalTokens
    print("Botón limpiar tokens")
    listaGlobalTokens.clear()

def ManualUsuario():
    print("Botón manual de usuario")
    startfile('Documentacion\ManualUsuario.pdf')

def ManualTecnico():
    print("Botón manual técnico")
    startfile('Documentacion\ManualTecnico.pdf')


  

VentanaPrincipal = Tk()
VentanaPrincipal.geometry("1200x825")
VentanaPrincipal.title("La Liga Bot")
VentanaPrincipal.config(bg="SkyBlue1")

botonEnviar = Button(VentanaPrincipal, text="Enviar", width=15, height=1, font=("Arial", 12, "italic"), command= Enviar)
botonReporteErrores = Button(VentanaPrincipal, text="Reporte de Errores", width=15, height=1, font=("Arial", 12, "italic"), command= ReporteErrores)
botonLimpiarErrores = Button(VentanaPrincipal, text="Limpiar Errores", width=15, height=1, font=("Arial", 12, "italic"), command= LimpiarErrores)
botonReporteTokens = Button(VentanaPrincipal, text="Reporte de Tokens", width=15, height=1, font=("Arial", 12, "italic"), command= ReporteTokens)
botonLimpiarTokens = Button(VentanaPrincipal, text="Limpiar Tokens", width=15, height=1, font=("Arial", 12, "italic"), command= LimpiarTokens)
botonManualUsuario = Button(VentanaPrincipal, text="Manual de Usuario", width=15, height=1, font=("Arial", 12, "italic"), command= ManualUsuario)
botonManualTecnico = Button(VentanaPrincipal, text="Manual de Técnico", width=15, height=1, font=("Arial", 12, "italic"), command= ManualTecnico)

EntradaComando = Entry(VentanaPrincipal, width=50, font=("Arial", 12, "italic"))



Titulo = Label(VentanaPrincipal, text = "La Liga Bot", font=("Arial", 16, "italic"),  bg="SkyBlue1")
Entrada = Text(VentanaPrincipal, font=("Arial", 12, "italic"))
MensajeInicial = "LaLigaBot: Bienvenido a la interfaz de la Liga Bot.\nLaLigaBot: Para comenzar, ingrese un comando en el cuadro de texto.  "
Entrada.insert(1.0, MensajeInicial)
Entrada.config(state=DISABLED)
BarraVertical = Scrollbar(Entrada)
BarraHorizontal = Scrollbar(Entrada ,orient=HORIZONTAL)
Entrada.config(yscrollcommand=BarraVertical.set,wrap = "none",xscrollcommand=BarraHorizontal.set)
BarraHorizontal.pack(side = BOTTOM, fill = X)
BarraHorizontal.config(command=Entrada.xview)
BarraVertical.pack(side = RIGHT, fill = Y)
BarraVertical.config(command=Entrada.yview)

Titulo.place(x=300,y=25,width=600)
botonReporteErrores.place(x=950,y=90,width=200,height=50)
botonLimpiarErrores.place(x=950,y=160,width=200,height=50)
botonReporteTokens.place(x=950,y=230,width=200,height=50)
botonLimpiarTokens.place(x=950,y=300,width=200,height=50)
botonManualUsuario.place(x=950,y=370,width=200,height=50)
botonManualTecnico.place(x=950,y=440,width=200,height=50)

EntradaComando.place(x=25,y=725,width=850,height=50)

botonEnviar.place(x=950, y=725,width=200,height=50)
Entrada.place(x= 25,y=90,width=850,height=600 )

VentanaPrincipal.mainloop()
