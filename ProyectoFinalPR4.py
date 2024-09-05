# Gabriel Del Cid
from tkinter import * 
from tkinter import ttk

def obtenerletramen():
    montopres_calculo = intromontoprest.get()
    plazodepago = introplazo.get()
    tipodeprest = escogerpresta.get()
    if tipodeprest == "1. Hipotecario":
        cantidaddeintereses = 0.06
    elif tipodeprest == "2. Personal":
        cantidaddeintereses = 0.13
    else: 
        cantidaddeintereses = 0.09
    plazoenmeses = int(plazodepago) * 12
    calculodepago = montopres_calculo * (cantidaddeintereses / 12) / (1 - (1 + cantidaddeintereses / 12)**(-plazoenmeses))
    pagomensual.set(round(calculodepago,2))
    
def obtenerpoliza():
    edad = introedad.get()
    genero = select.get()
    genero_str = "Masculino" if genero == 1 else "Femenino"
    fuma = escogerfuma.get()
    montopres = intromontoprest.get()
    if genero_str == "Masculino":
        if edad >= 18 and edad <=40:
            tasavida = 0.003
        elif edad >= 41 and edad <= 60:
            tasavida = 0.004
        else:
            tasavida = 0.006
    else:
        if edad >= 18 and edad <= 40:
            tasavida = 0.0025
        elif edad >= 41 and edad <=60:
            tasavida = 0.0035
        else:
            tasavida = 0.005
    if fuma == "FUMADOR":
        tasavida *= 1.5
    polizadevi = tasavida * montopres
    polizadevida.set(round(polizadevi,2))

def calculartodo():
    obtenerletramen()
    obtenerpoliza()

ventana = Tk()
ventana.title("Modulo de Prestamos")

frame_titulo = Frame(ventana, bg="sky blue3")
frame_titulo.place(x=10, y=10, width=580, height=40 ) 

lbltitulo = Label(frame_titulo, text="MODULO DE PRESTAMOS", bg="sky blue3", font=("Helvetica", 14))
lbltitulo.place(x=160, y=8)

lbltipodepres = Label(ventana,text="Tipo de Prestamo: ").place(x=20, y=80)
escogerpresta = StringVar()
combotipodepres = ttk.Combobox(ventana, textvariable=escogerpresta, width=22, values=("1. Hipotecario", "2. Personal", "3. Auto")).place(x=140,y=80)

lblnombre = Label(ventana,text="Nombre: ").place(x=20, y=110)
entrynombre = Entry(ventana, width=25).place(x=140, y=110)

lbledad = Label(ventana,text="Edad: ").place(x=380, y=110)
introedad = IntVar()
entryedad = Entry(ventana, textvariable=introedad, width= 12).place(x= 450, y=110)

lblgenero = Label(ventana,text="Género: ").place(x=20, y=150)
select = IntVar()
masc = Radiobutton(ventana,text="Masculino", value=1,variable=select).place(x=130, y=150)
fem = Radiobutton(ventana,text="Femenino", value=2,variable=select).place(x=220, y=150)

lblfuma = Label(ventana,text="Condición: ").place(x=380, y=150)
escogerfuma = StringVar()
combofuma = ttk.Combobox(ventana, textvariable=escogerfuma, width=14, values=("FUMADOR","NO FUMADOR")).place(x=450, y=150)

lblmontoprest = Label(ventana,text="Monto del Préstamo: ").place(x=20, y=190)
intromontoprest = IntVar()
entrymontoprest = Entry(ventana, textvariable=intromontoprest, width= 12).place(x= 140, y=190)

lblplazo = Label(ventana,text="Plazo (en años): ").place(x=350, y=190)
introplazo = IntVar()
entryplazo = Entry(ventana, textvariable=introplazo, width= 12).place(x= 450, y=190)

lbletrames = Label(ventana,text="Letra Mensual: ").place(x=300, y=250)
pagomensual = IntVar()
entrymes = Entry(ventana, textvariable=pagomensual, width= 12).place(x= 400, y=250)


lblpolizavida = Label(ventana,text="Poliza de Vida: ").place(x=300, y=290)
polizadevida = IntVar()
entrypoliza = Entry(ventana, textvariable=polizadevida, width= 12).place(x= 400, y=290)

boton = Button(ventana, text= "    Calcular Letra Mensual    ",command=calculartodo,bg="gray61").place(x=50, y=250)

ventana.geometry("600x400")
ventana.mainloop()