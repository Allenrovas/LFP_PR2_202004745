from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter import messagebox
import csv
from AnalizadorLexico import AnalizadorLexico
from Jornada import Jornada

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




def Enviar():
    lexico = AnalizadorLexico()
    CadenaAnalizar = EntradaComando.get()
    lexico.AnalizadorLexico(CadenaAnalizar)
    lexico.imprimirErrores()
    lexico.imprimirTokens()
    

def ReporteErrores():
    print("Botón reporte de errores")

def LimpiarErrores():
    print("Botón limpiar errores")

def ReporteTokens():
    print("Botón reporte de tokens")

def LimpiarTokens():
    print("Botón limpiar tokens")

def ManualUsuario():
    print("Botón manual de usuario")

def ManualTecnico():
    print("Botón manual técnico")

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
Entrada = Text(VentanaPrincipal, font=("Arial", 12, "italic"),state='disabled')
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
