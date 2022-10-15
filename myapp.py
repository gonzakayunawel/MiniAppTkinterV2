# Importamos la libreria Tkinter y nuestra archivo donde tenemos las funciones del boot
import tkinter, mybot

# Creamos el objeto ventana con titulo y tamaño
ventana = tkinter.Tk()
ventana.geometry("900x600")
ventana.title("My Bot App v2")
ventana.iconbitmap("./hola.ico")

# Creamos un marco o Frame para color de fondo
fondo = tkinter.Frame(ventana, width=520, height=480)
fondo.pack(fill='both', expand=True)
fondo.config(bg = "#87E534")


# Título
title = tkinter.Label(fondo, bg="lightgreen", font = "Helvetica 20", text="Welcome, please write your name and press Greet")
title.pack(fill = tkinter.X)


# Creamos la una caja de entrada de texto
cajaTexto = tkinter.Entry(fondo, font = "Helvetica 20",)
cajaTexto.pack()


# Creamos una etiqueta donde mostrar el texto ingresado
etiqueta = tkinter.Label(fondo, bg="yellow", font = "Helvetica 20")
etiqueta.pack(fill = tkinter.X)

# Definimos la función para obtener el texto ingresado en la caja y que nos genere un saludo
def saludar():
    text_input = cajaTexto.get() # Obtiene el texto de cajaTexto
    cajaTexto.delete(0, "end") # Elmina el texto en la caja
    etiqueta["text"] = "Hi "+text_input+", how are you today?" # Le indica a etiqueta el texto usando "text"

# Creamos un botón para mostrar el texto ingresado llamando a la función creada
button_greet = tkinter.Button(fondo, text = "Greet", command = saludar)
button_greet.pack()

# Instrucciones de como usar
howToUse_text = tkinter.Label(fondo, bg="lightgreen", font = "Helvetica 20", text="Please, write some word and select you option")
howToUse_text.pack(fill = tkinter.X)

# Creamos una caja para ingresar texto
cajaTexto1 = tkinter.Entry(fondo, font = "Helvetica 20",)
cajaTexto1.pack()

# Creamos una función para obtener el texto ingresado
def textoCaja():
    text_input = cajaTexto1.get() # Obtiene el texto de cajaTexto1
    cajaTexto1.delete(0, "end") # Elmina el texto en la caja
    return str(text_input) # Devuelve un string del texto ingresado

# Creamos botones para llamar a las funciones creadas en nuestro bot, estas aceptan parámetros desde la función textoCaja

button_google = tkinter.Button(fondo, text = "Google Docs", command = lambda: mybot.documentogoogle(textoCaja()))
button_google.pack()

button_youtube = tkinter.Button(fondo, text = "Youtube", command = lambda: mybot.youtube(textoCaja()))
button_youtube.pack()

# Colocar una imagen

imagen = tkinter.PhotoImage(file="./robot.png")

etiqueta_imagen = tkinter.Label(fondo, image=imagen, bd=0)
etiqueta_imagen.pack()

# Nuestro loop de ejecución
ventana.mainloop()