from functools import partial
from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

from pyexpat.errors import messages

operador = ""

def clickBotonCalculadora(numero):
    global operador

    match numero:
        case "B":
            pantalla_calculadora.delete(0, END)
        case "R":
            operador = str(eval(operador.replace("x", "*")))
            pantalla_calculadora.delete(0, END)
            pantalla_calculadora.insert(END, operador)
        case _:
            operador += numero
            pantalla_calculadora.delete(0, END)
            pantalla_calculadora.insert(END, operador)

#iniciar tkinter
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry("1120x540+0+0")

#evitar maximizar
aplicacion.resizable(False, False)

#título de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")

#cambiar color de fondo de la ventana
aplicacion.config(bg="burlywood")

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief="flat")
panel_superior.pack(side="top")

#etiqueta título
titulo = Label(panel_superior,
               text="Sistema de Facturación",
               fg="azure4",
               font=("Dosis", 45),
               bg="burlywood",
               width=32)
titulo.grid(
    row=0,
    column=0)

#panel izquierdo
panel_izquierdo = Frame(aplicacion,
                        bd=1,
                        relief="flat")
panel_izquierdo.pack(side="left")

#panel de menú
panel_menu = Frame(panel_izquierdo,
                   bd=1,
                   relief="flat")
panel_menu.pack(side="top")

#panel comida
def revisar_check(contador, tipo):
    match tipo:
        case "comida":
            if variables_comida[contador].get() == 1:
                texto_comida[contador].set("")
                cuadros_comida[contador].config(state="normal")
                cuadros_comida[contador].focus()
            else:
                texto_comida[contador].set("0")
                cuadros_comida[contador].config(state="disabled")
        case "bebida":
            if variables_bebida[contador].get() == 1:
                texto_bebida[contador].set("")
                cuadros_bebida[contador].config(state="normal")
                cuadros_bebida[contador].focus()
            else:
                texto_bebida[contador].set("0")
                cuadros_bebida[contador].config(state="disabled")
        case "postre":
            if variables_postre[contador].get() == 1:
                texto_postre[contador].set("")
                cuadros_postre[contador].config(state="normal")
                cuadros_postre[contador].focus()
            else:
                texto_postre[contador].set("0")
                cuadros_postre[contador].config(state="disabled")


panel_comida = LabelFrame(panel_menu,
                          text="Comida",
                          font=("Dosis", 19, "bold"),
                          bd=1,
                          relief="flat",
                          fg="azure4")
panel_comida.pack(side="left")

lista_comidas = ["pollo", "cordero", "salmón", "merluza", "kebab", "pizza1", "pizza2", "pizza3"]
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]

#generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:
    #crear checkbuttons
    variables_comida.append("")
    variables_comida[contador] = IntVar()
    chk_comida = Checkbutton(panel_comida,
                             text=comida,
                             font=("Dosis", 19, "bold"),
                             onvalue=1,
                             offvalue=0,
                             variable=variables_comida[contador],
                             command=partial(revisar_check, contador, tipo="comida"))
    chk_comida.grid(row=contador,
                    column=0,
                    sticky="W")

    #crear inputs de cantidad
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")

    cuadros_comida[contador] = Entry(panel_comida,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state="disabled",
                                     textvariable=texto_comida[contador])

    cuadros_comida[contador].grid(row=contador,
                                  column=1,
                                  sticky="W")

    contador += 1

#panel bebida
panel_bebida = LabelFrame(panel_menu,
                          text="Bebida",
                          font=("Dosis", 19, "bold"),
                          bd=1,
                          relief="flat",
                          fg="azure4")
panel_bebida.pack(side="left")

lista_bebidas = ["agua", "soda", "jugo", "cola", "vino1", "vino2", "cerbeza1", "cerbeza2"]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]

variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0

for bebida in lista_bebidas:
    variables_bebida.append("")
    variables_bebida[contador] = IntVar()
    chk_bebida = Checkbutton(panel_bebida,
                             text=bebida,
                             font=("Dosis", 19, "bold"),
                             onvalue=1,
                             offvalue=0,
                             variable=variables_bebida[contador],
                             command=partial(revisar_check, contador, tipo="bebida"))
    chk_bebida.grid(
        row=contador,
        column=0,
        sticky="W")

    # crear inputs de cantidad
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")

    cuadros_bebida[contador] = Entry(panel_bebida,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state="disabled",
                                     textvariable=texto_bebida[contador])

    cuadros_bebida[contador].grid(row=contador,
                                  column=1,
                                  sticky="W")

    contador += 1

#panel postre
panel_postre = LabelFrame(panel_menu,
                          text="Postre",
                          font=("Dosis", 19, "bold"),
                          bd=1,
                          relief="flat",
                          fg="azure4")
panel_postre.pack(side="left")

lista_postres = ["helado", "fruta", "brownie", "flán", "mousse", "pastel1", "pastel2", "pastel3"]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0

for postre in lista_postres:
    variables_postre.append("")
    variables_postre[contador] = IntVar()
    chk_postre = Checkbutton(panel_postre,
                             text=postre,
                             font=("Dosis", 19, "bold"),
                             onvalue=1,
                             offvalue=0,
                             variable=variables_postre[contador],
                             command=partial(revisar_check, contador, tipo="postre"))
    chk_postre.grid(
        row=contador,
        column=0,
        sticky="W")

    # crear inputs de cantidad
    cuadros_postre.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set("0")

    cuadros_postre[contador] = Entry(panel_postre,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state="disabled",
                                     textvariable=texto_postre[contador])

    cuadros_postre[contador].grid(row=contador,
                                  column=1,
                                  sticky="W")

    contador += 1

#panel de costos
panel_costos = Frame(panel_izquierdo,
                     bd=1,
                     relief="flat",
                     bg="azure4")
panel_costos.pack(side="bottom")

#costo comida
etiqueta_costo_comida = Label(panel_costos,
                              text="Costo Comida",
                              fg="white",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              padx=50)
etiqueta_costo_comida.grid(
    row=0,
    column=0)

var_costo_comida = StringVar()

texto_costo_comida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

#costo bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text="Costo Bebida",
                              fg="white",
                              font=("Dosis", 12, "bold"),
                              bg="azure4")
etiqueta_costo_bebida.grid(
    row=1,
    column=0)

var_costo_bebida = StringVar()

texto_costo_bebida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

#costo postre
etiqueta_costo_postre= Label(panel_costos,
                              text="Costo Postre",
                              fg="white",
                              font=("Dosis", 12, "bold"),
                              bg="azure4")
etiqueta_costo_postre.grid(
    row=2,
    column=0)

var_costo_postre = StringVar()

texto_costo_postre = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

#subtotal
var_subtotal = StringVar()

etiqueta_subtotal= Label(panel_costos,
                         text="Subtotal",
                         fg="white",
                         font=("Dosis", 12, "bold"),
                         bg="azure4")
etiqueta_subtotal.grid(
    row=0,
    column=2)

texto_subtotal = Entry(panel_costos,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_subtotal)
texto_subtotal.grid(
    row=0,
    column=3, padx=41)

#impuestos
var_impuestos = StringVar()

etiqueta_impuestos= Label(panel_costos,
                         text="Impuestos",
                         fg="white",
                         font=("Dosis", 12, "bold"),
                         bg="azure4")
etiqueta_impuestos.grid(
    row=1,
    column=2)

texto_impuestos = Entry(panel_costos,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_impuestos)
texto_impuestos.grid(
    row=1,
    column=3, padx=41)

#total
var_total = StringVar()

etiqueta_total= Label(panel_costos,
                         text="Total",
                         fg="white",
                         font=("Dosis", 12, "bold"),
                         bg="azure4")
etiqueta_total.grid(
    row=2,
    column=2)

texto_total = Entry(panel_costos,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_total)
texto_total.grid(
    row=2,
    column=3, padx=41)

#panel derecho
panel_derecho = Frame(aplicacion,
                      bd=1,
                      relief="flat")
panel_derecho.pack(side="right")

#panel calculadora
panel_calculadora = Frame(panel_derecho,
                          bd=1,
                          relief="flat",
                          bg="burlywood")
panel_calculadora.pack(side="top")

pantalla_calculadora = Entry(panel_calculadora,
                             font=("Dosis", 16, "bold"),
                             bd=1,
                             width=38)
pantalla_calculadora.grid(row=0, column=0, columnspan=4)

botones = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", "R", "B", "0", "/"]
row = 1
column = 0

for boton in botones:
    texto_boton = boton

    boton = Button(panel_calculadora,
                   text=boton,
                   font=("Dosis", 16, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=8,
                   command=partial(clickBotonCalculadora, texto_boton))
    boton.grid(row=row, column=column)

    if column == 3:
        row += 1
        column = 0
    else:
        column += 1

#panel recibo
panel_recibo = Frame(panel_derecho,
                     bd=1,
                     relief="flat",
                     bg="burlywood")
panel_recibo.pack(side="top")

texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    bd=1,
                    width=51,
                    height=12)
texto_recibo.grid(row=0, column=0)

def pintaRecibo():
    texto_recibo.delete(1.0, END)
    numero_recibo =f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} {fecha.hour}:{fecha.minute}"

    texto_recibo.insert(END, f"Datos:\t{numero_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"{'*' * 57}\n")
    texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, f"{'-' * 62}\n")

    contador = 0
    total_comida = 0
    total_bebida = 0
    total_postre = 0
    lista_comanda = []

    for comida in variables_comida:
        if comida.get() == 1:
            total_comida += float(texto_comida[contador].get()) * precios_comida[contador]
            lista_comanda.append({"nombre": lista_comidas[contador], "cantidad": texto_comida[contador].get(), "costo": float(texto_comida[contador].get()) * precios_comida[contador]})

        contador += 1

    contador = 0

    for bebida in variables_bebida:
        if bebida.get() == 1:
            total_bebida += float(texto_bebida[contador].get()) * precios_bebida[contador]
            lista_comanda.append({"nombre": lista_bebidas[contador], "cantidad": texto_bebida[contador].get(), "costo": float(texto_bebida[contador].get()) * precios_bebida[contador]})

        contador += 1

    contador = 0

    for postre in variables_postre:
        if postre.get() == 1:
            total_postre += float(texto_postre[contador].get()) * precios_postres[contador]
            lista_comanda.append({"nombre": lista_postres[contador], "cantidad": texto_postre[contador].get(), "costo": float(texto_postre[contador].get()) * precios_postres[contador]})

        contador += 1

    for item in lista_comanda:
        texto_recibo.insert(END, f"{item["nombre"]}\t\t{item["cantidad"]}\t$ {item["costo"]}\n")

    subtotal = total_comida + total_bebida + total_postre
    impuestos = subtotal * 0.07
    total = subtotal + impuestos

    texto_recibo.insert(END, f"{'-' * 62}\n")
    texto_recibo.insert(END, f"Sub-total: \t\t\t$ {round(subtotal, 2)}\n")
    texto_recibo.insert(END, f"Impuestos: \t\t\t$ {round(impuestos, 2)}\n")
    texto_recibo.insert(END, f"Total: \t\t\t$ {round(total, 2)}\n")
    texto_recibo.insert(END, f"{'*' * 57}\n")
    texto_recibo.insert(END, "Lo esperamos pronto")

def guardaRecibo():
    fichero = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    fichero.write(texto_recibo.get(1.0, END))

    fichero.close()
    messagebox.showinfo("Información", "Su recibo ha sido guardado")

def reseteaPantalla():
    texto_recibo.delete(1.0, END)
    pantalla_calculadora.delete(0, END)

    contador = 0

    for comida in variables_comida:
        if comida.get() == 1:
            comida.set(0)
            texto_comida[contador].set("0")
            cuadros_comida[contador].config(state="disabled")

        contador += 1

    contador = 0

    for bebida in variables_bebida:
        if bebida.get() == 1:
            bebida.set(0)
            texto_bebida[contador].set("0")
            cuadros_bebida[contador].config(state="disabled")

        contador += 1

    contador = 0

    for postre in variables_postre:
        if postre.get() == 1:
            postre.set(0)
            texto_postre[contador].set("0")
            cuadros_postre[contador].config(state="disabled")

        contador += 1

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postre.set("")

    var_subtotal.set("")
    var_impuestos.set("")
    var_total.set("")

def clickBotonBotonera(boton):
    match boton:
        case "total":
            total_comida = 0
            total_bebida = 0
            total_postre = 0
            contador = 0

            for comida in variables_comida:
                if comida.get() == 1:
                    total_comida += float(texto_comida[contador].get()) * precios_comida[contador]

                contador += 1

            var_costo_comida.set(f"$ {round(total_comida, 2)}")

            contador = 0

            for bebida in variables_bebida:
                if bebida.get() == 1:
                    total_bebida += float(texto_bebida[contador].get()) * precios_bebida[contador]

                contador += 1

            var_costo_bebida.set(f"$ {round(total_bebida, 2)}")

            contador = 0

            for postre in variables_postre:
                if postre.get() == 1:
                    total_postre += float(texto_postre[contador].get()) * precios_postres[contador]

                contador += 1

            var_costo_postre.set(f"$ {round(total_postre, 2)}")

            subtotal = total_comida + total_bebida + total_postre
            var_subtotal.set(f"$ {round(subtotal, 2)}")

            impuestos = subtotal * 0.07
            var_impuestos.set(f"$ {round(impuestos, 2)}")

            total = subtotal + impuestos
            var_total.set(f"$ {round(total, 2)}")
        case "recibo":
            pintaRecibo()
        case "guardar":
            guardaRecibo()
        case "resetear":
            reseteaPantalla()

#panel botones
panel_botones = Frame(panel_derecho,
                      bd=1,
                      relief="flat",
                      bg="burlywood")
panel_botones.pack(side="top")

botones = ["total", "recibo", "guardar", "resetear"]
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis", 14, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=9,
                   command=partial(clickBotonBotonera, boton))
    boton.grid(row=0, column=columnas)
    columnas += 1

#evitar que la pantalla se cierre
aplicacion.mainloop()