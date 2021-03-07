import tkinter as tk
from tkinter import ttk
import General.General as gnrl
from tkinter import messagebox

mostrar_parcelas = False
mostrar_cultivos = False
mostrar_historico = False
mostrar_sim_asignar = False

class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #Creamos la ventana principal, los *args es una forma por defecto de introducir todos los elementos que puede pedir el método

        self.title("Este es el titulo de la ventana") # Indicamos el texto que aparecerá como titulo de la ventana
        self.geometry("650x350") # De esta manera configuramos el tamaño de la ventana

        # Una vez definidas las propiedades basicas de la ventana, vamos a configurar el Contenedor en el cual crearemos los objetos
        #con los que trabajaremos.

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # Creamos un diccionario vacío en el que almacenaremos los Frames en los que diseñaremos las ventanas.

        for F in (a,b,c,d,e,f,g,h,i,j,k):
            nombre_pagina = F.__name__ # Obtenemos el nombre de la clase en la que definimos el Frame
            frame = F(parent=container, controller=self) # Creamos un frame cuyo padre es el contenedor creado anteriormente y es controlador mediante "VentanaPrincipal"
            self.frames[nombre_pagina] = frame # Añadimos un nuevo elemento al diccionario; cuyo 'key' es el nombre de la clase Frame y el 'value' es el frame creado en la línea anterior.
            frame.grid(row=0,column=0,sticky="nsew") # El Frame lo posicionamos en la celda (0,0) del Grid y los objetos que se introducen estas celdas seran escalados en todas las direcciones.

        self.mostrar_Frame("h") # Hacemos la llamada a la pagina principal. Cuando iniciamos la ejecución por defecto se llamará a esta pagina.

    def mostrar_Frame(self,nombre_pagina):
        frame = self.frames[nombre_pagina] # Extramos el objeto tipo Frame que tenemos almacenado en el diccionario 'frames'; el cual es generados y configurado al inicio de la ejecución de la aplicación.
        frame.tkraise() # Con esta función lo que hacemos es traer a la primera capa, o vista, el Frame con el que deseamos trabajar.

#----------------- Funciones de la pantalla

# Pantalla principal
class h(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        self.boton_1 = tk.Button(self, text = "Parcelas", width = 10, command = lambda: controller.mostrar_Frame("a"))#, command = "") # Creamos la instancia de un botón, definiendo ciertas caracteristicas del mismo
        self.boton_1.grid(row = 1, column = 1, columnspan = 1) # Posicionamos el botón en la fila y columna definida. Columnspan, se indica la cantidad de columnas que ocupa el botón
        self.boton_2 = tk.Button(self, text = "Cultivos", width = 10, command = lambda: controller.mostrar_Frame("b"))
        self.boton_2.grid(row = 2, column = 1, columnspan = 1)
        self.boton_3 = tk.Button(self, text = "Simular", width = 10, command = lambda: controller.mostrar_Frame("c"))
        self.boton_3.grid(row = 3, column = 1, columnspan = 1)
        self.boton_4 = tk.Button(self, text = "Info Sistema", width = 10, command = lambda: controller.mostrar_Frame("k"))
        self.boton_4.grid(row = 4, column = 1, columnspan = 1)
        self.boton_5 = tk.Button(self, text = "Datos", width = 10, command = lambda: controller.mostrar_Frame("j"))
        self.boton_5.grid(row = 5, column = 1, columnspan = 1)
        self.boton_6 = tk.Button(self, text = "Salir", width = 10, command = self.salir)
        self.boton_6.grid(row = 6, column = 1, columnspan = 1)

    def salir(self):
        respuesta = messagebox.askquestion("Salir", "¿Desea salir de al aplicación?")
        if respuesta == "yes":
            self.controller.destroy()

# Parcela
class a(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        self.varOpcion = tk.StringVar(value = "*")

        self.label_1 = tk.Label(self, text = "Identificador", justify = "center")
        self.label_1.grid(row = 1, column = 1)
        self.entrada_1 = tk.Entry(self)
        self.entrada_1.grid(row = 1, column = 2, columnspan = 5)
        self.label_1_3 = tk.Label(self, text = "Debe de ser alfanumérico y único")
        self.label_1_3.grid(row = 1, column = 7)

        self.label_2 = tk.Label(self, text = "Area", justify = "center")
        self.label_2.grid(row = 2, column = 1)
        self.entrada_2 = tk.Entry(self)
        self.entrada_2.grid(row = 2, column = 2, columnspan = 5)
        self.label_2_1 = tk.Label(self, text = "Debe de ser un valor entero")
        self.label_2_1.grid(row = 2, column = 7)

        self.label_3 = tk.Label(self, text = "Tipo de suelo", justify = "center")
        self.label_3.grid(row = 3, column = 1)
        self.radio_3_1 = tk.Radiobutton(self, text = "A", variable = self.varOpcion, value = "A")
        self.radio_3_1.grid(row = 3, column = 2)
        self.radio_3_2 = tk.Radiobutton(self, text = "B", variable = self.varOpcion, value = "B")
        self.radio_3_2.grid(row = 3, column = 3)
        self.radio_3_3 = tk.Radiobutton(self, text = "C", variable = self.varOpcion, value = "C")
        self.radio_3_3.grid(row = 3, column = 4)
        self.radio_3_4 = tk.Radiobutton(self, text = "D", variable = self.varOpcion, value = "D")
        self.radio_3_4.grid(row = 3, column = 5)
        self.radio_3_5 = tk.Radiobutton(self, text = "E", variable = self.varOpcion, value = "E")
        self.radio_3_5.grid(row = 3, column = 6)

        self.boton_4 = tk.Button(self, text = "Añadir", command =  self.añadir_parcela)
        self.boton_4.grid(row = 4, column = 5)

        self.boton_5 = tk.Button(self, text = "Menú", command = self.menu)
        self.boton_5.grid(row = 5, column = 5)

        self.update()
        
    def añadir_parcela(self):
        # Una vez ha sido llamada esta función, realizamos las siguientes acciones:
        #   1. Llamamos la función "añadir_Parcela" del paquete General.
        #   2. Cambiamos el Frame que visualizamos.
        #   3. Llamamos al método interno de la clase "limpiar_entradas"
        gnrl.añadir_Parcela(self.entrada_1.get(), self.entrada_2.get(), self.varOpcion.get())
        self.controller.mostrar_Frame("h")
        self.limpiar_entradas()
        
    def limpiar_entradas(self):
        # Eliminamos los valores residuales presentes en los campos que se pueden rellenar
        self.entrada_1.delete(0,'end')
        self.entrada_2.delete(0,'end')
        self.varOpcion.set("*")

    def menu(self):
        self.limpiar_entradas()
        self.controller.mostrar_Frame('h')

    def update(self):
        # Este método se utiliza como comprobador del estado actual de las entradas, de forma que editamos las propiedades de los widget 
        # de forma "dinamica" o "en runtime"
        id_condicion = self.entrada_1.get().isalnum() and not self.entrada_1.get().isalpha() and not self.entrada_1.get().isdecimal() and gnrl.identificador_unico_Parcela(self.entrada_1.get())
        
        if id_condicion:
            self.label_1_3.config(fg = 'green')
        else:
            self.label_1_3.config(fg = 'red')

        if self.entrada_2.get().isdecimal():
            self.label_2_1.config(fg = 'green')
        else:
            self.label_2_1.config(fg = 'red')

        if id_condicion and self.entrada_2.get().isdecimal() and not self.varOpcion.get() == '*':
            self.boton_4['state'] = tk.NORMAL
        else:
            self.boton_4['state'] = tk.DISABLED
            
        self.after(1000,self.update)

# Cultivos
class b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.varOpcion = tk.StringVar(value = "*")
        self.checkValue = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
        self.lista = []
        self.cambiaSuelo = False

        self.label_1 = tk.Label(self, text = "Identificador: ", justify = "center")
        self.label_1.grid(row = 1, column = 1)
        self.entrada_1 = tk.Entry(self)
        self.entrada_1.grid(row = 1, column = 2, columnspan = 5)
        self.label_1_3 = tk.Label(self, text = "Debe de ser alfanumérico y único")
        self.label_1_3.grid(row = 1, column = 7)

        self.label_2 = tk.Label(self, text = "Tipos de suelo: ", justify = "center")
        self.label_2.grid(row=2, column = 1)
        self.check_2_1 = tk.Checkbutton(self, text = "A", variable=self.checkValue[0], onvalue = 1, offvalue = 0, command = lambda: self.genLista(self.check_2_1,self.checkValue[0])) 
        self.check_2_1.grid(row=2,column = 2)
        self.check_2_2 = tk.Checkbutton(self, text = "B", variable=self.checkValue[1], onvalue = 1, offvalue = 0, command = lambda: self.genLista(self.check_2_2,self.checkValue[1])) 
        self.check_2_2.grid(row=2,column = 3)
        self.check_2_3 = tk.Checkbutton(self, text = "C", variable=self.checkValue[2], onvalue = 1, offvalue = 0, command = lambda: self.genLista(self.check_2_3,self.checkValue[2])) 
        self.check_2_3.grid(row=2,column = 4)
        self.check_2_4 = tk.Checkbutton(self, text = "D", variable=self.checkValue[3], onvalue = 1, offvalue = 0, command = lambda: self.genLista(self.check_2_4,self.checkValue[3])) 
        self.check_2_4.grid(row=2,column = 5)
        self.check_2_5 = tk.Checkbutton(self, text = "E", variable=self.checkValue[4], onvalue = 1, offvalue = 0, command = lambda: self.genLista(self.check_2_5,self.checkValue[4])) 
        self.check_2_5.grid(row=2,column = 6)

        self.label_3 = tk.Label(self, text = "Area mínima: ", justify = "center")
        self.label_3.grid(row = 3, column = 1)
        self.entrada_3 = tk.Entry(self)
        self.entrada_3.grid(row = 3, column = 2, columnspan = 5)
        self.label_3_1 = tk.Label(self, text = "Debe de ser un valor entero")
        self.label_3_1.grid(row = 3, column = 7)

        self.boton_4 = tk.Button(self, text = "Transforma el suelo?", command = self.puedeTransformar)
        self.boton_4.grid(row=4, column = 1)

        self.radio_5_1 = tk.Radiobutton(self, text = "A", variable = self.varOpcion, value = "A", state = tk.DISABLED)
        self.radio_5_1.grid(row = 5, column = 2)
        self.radio_5_2 = tk.Radiobutton(self, text = "B", variable = self.varOpcion, value = "B", state= tk.DISABLED)
        self.radio_5_2.grid(row = 5, column = 3)
        self.radio_5_3 = tk.Radiobutton(self, text = "C", variable = self.varOpcion, value = "C", state = tk.DISABLED)
        self.radio_5_3.grid(row = 5, column = 4)
        self.radio_5_4 = tk.Radiobutton(self, text = "D", variable = self.varOpcion, value = "D", state = tk.DISABLED)
        self.radio_5_4.grid(row = 5, column = 5)
        self.radio_5_5 = tk.Radiobutton(self, text = "E", variable = self.varOpcion, value = "E", state = tk.DISABLED)
        self.radio_5_5.grid(row = 5, column = 6)

        self.label_6 = tk.Label(self, text = "Duración del cultivo", justify = "center")
        self.label_6.grid(row = 6, column = 1)
        self.entrada_6 = tk.Entry(self)
        self.entrada_6.grid(row = 6, column = 2, columnspan = 5)
        self.label_6_1 = tk.Label(self, text = "Debe de ser un valor entero")
        self.label_6_1.grid(row = 6, column = 7)

        self.boton_7 = tk.Button(self, text = "Añadir", command = lambda: self.añadir_cultivo())
        self.boton_7.grid(row = 7, column = 5)

        self.boton_5 = tk.Button(self, text = "Menú", command = self.menu)
        self.boton_5.grid(row = 8, column = 5)

        self.update()

    def añadir_cultivo(self):
        # Una vez ha sido llamada esta función, realizamos las siguientes acciones:
        #   1. Llamamos la función "añadir_Cultivo" del paquete General.
        #   2. Cambiamos el Frame que visualizamos.
        #   3. Llamamos al método interno de la clase "limpiar_entradas"
        gnrl.añadir_Cultivo(self.entrada_1.get(),self.lista,self.entrada_3.get(),self.entrada_6.get(),self.cambiaSuelo,self.varOpcion.get())
        self.controller.mostrar_Frame("h")
        self.limpiar_entradas()

    def menu(self):
        self.limpiar_entradas()
        self.controller.mostrar_Frame('h')

    def genLista(self, obj, variable):
        # Generamos el valor de una lista en función de las opciones seleccionadas en los Radiobuttons
        if(variable.get() == 1):
            self.lista.append(obj.cget('text'))
        else:
            if(obj.cget('text') in self.lista):
                self.lista.remove(obj.cget('text'))

    def puedeTransformar(self):
        if self.radio_5_1['state'] == tk.DISABLED:
            self.radio_5_1['state'] = tk.NORMAL
            self.radio_5_2['state'] = tk.NORMAL
            self.radio_5_3['state'] = tk.NORMAL
            self.radio_5_4['state'] = tk.NORMAL
            self.radio_5_5['state'] = tk.NORMAL
            self.cambiaSuelo = True
        else:
            self.radio_5_1['state'] = tk.DISABLED
            self.radio_5_2['state'] = tk.DISABLED
            self.radio_5_3['state'] = tk.DISABLED
            self.radio_5_4['state'] = tk.DISABLED
            self.radio_5_5['state'] = tk.DISABLED
            self.cambiaSuelo = False

    def limpiar_entradas(self):
        # Eliminamos los valores residuales presentes en los campos que se pueden rellenar
        self.entrada_1.delete(0,'end')
        self.entrada_3.delete(0,'end')
        self.entrada_6.delete(0,'end')
        self.varOpcion.set("*")
        self.checkValue.clear()
    
    def update(self):
        # Este método se utiliza como comprobador del estado actual de las entradas, de forma que editamos las propiedades de los widget 
        # de forma "dinamica" o "en runtime"
        id_condicion = self.entrada_1.get().isalnum() and not self.entrada_1.get().isalpha() and not self.entrada_1.get().isdecimal() and gnrl.identificador_unico_Cultivo(self.entrada_1.get())
        
        if id_condicion:
            self.label_1_3.config(fg = 'green')
        else:
            self.label_1_3.config(fg = 'red')

        if self.entrada_3.get().isdecimal():
            self.label_3_1.config(fg = 'green')
        else:
            self.label_3_1.config(fg = 'red')

        if self.entrada_6.get().isdecimal():
            self.label_6_1.config(fg = 'green')
        else:
            self.label_6_1.config(fg = 'red')

        if id_condicion and (len(self.lista) > 0) and self.entrada_3.get().isdecimal() and self.entrada_6.get().isdecimal():
            self.boton_7['state'] = tk.NORMAL
        else:
            self.boton_7['state'] = tk.DISABLED
            
        self.after(1000,self.update)

# Simulación
class c(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.boton_1 = tk.Button(self, text = "Asignación de cultivos", command = lambda: self.asignacion_cultivos())
        self.boton_1.grid(row = 1, column = 1)

        self.boton_2 = tk.Button(self, text = "Simulacion de cultivos", command = lambda: self.simulacion_cultivos())
        self.boton_2.grid(row = 2, column = 1)

        self.boton_3 = tk.Button(self, text = "Menu", command = lambda: self.controller.mostrar_Frame('h'))
        self.boton_3.grid(row = 3, column = 1)

    def asignacion_cultivos(self):
        global mostrar_sim_asignar

        mostrar_sim_asignar = True
        gnrl.ejecutar_Asignacion()
        self.controller.mostrar_Frame("d")

    def simulacion_cultivos(self):
        self.controller.mostrar_Frame("e")

# Entrada de diccionario Asignaciones
# Simulación - Asiganción Cultivos
class d(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.cnt = 3
        
        self.boton_f = tk.Button(self,text = "Menú", command = lambda: controller.mostrar_Frame("h"))
        self.boton_f.grid(row = 1, column = 1)

        self.label_2_1 = tk.Label(self, text = "Parcela:")
        self.label_2_1.grid(row = 2, column = 1)

        self.label_2_2 = tk.Label(self, text = "Cultivo:")
        self.label_2_2.grid(row = 2, column = 2)

        self.label_2_3 = tk.Label(self, text = "Area ocupada:")
        self.label_2_3.grid(row = 2, column = 3)

        self.update()

    def update(self):
        # Este método se utiliza como comprobador del estado actual de las entradas, de forma que editamos las propiedades de los widget 
        # de forma "dinamica" o "en runtime"
        global mostrar_sim_asignar
        
        if (mostrar_sim_asignar):
            self.crear_tabla()
            mostrar_sim_asignar = False
        
        self.after(1000,self.update)

    def crear_tabla(self):
        # Creamos de forma dinámica para visualizar de la forma más clara posible los datos.
        self.registros = gnrl.registro_Asignaciones()

        for registro in self.registros:
            self.label = tk.Label(self, text = registro)
            self.label.grid(row = self.cnt, column = 1)

            self.label_1 = tk.Label(self, text = self.registros[registro])
            self.label_1.grid(row = self.cnt, column = 2)

            self.progressbar = ttk.Progressbar(self)
            self.progressbar.grid(row = self.cnt, column = 3)
            self.progressbar['maximum'] = gnrl.enviar_estado_Parcelas()[registro].areaParcela
            self.progressbar['value'] = gnrl.enviar_estado_Cultivos()[self.registros[registro]].areaMinima

            self.cnt+=1

# Simulación - Simulación
class e(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.cnt = 3
        self.barras = []
        self.diasSim = 0

        self.entrada_sim = tk.Entry(self)
        self.entrada_sim.grid(row = 1, column = 1)

        self.boton_sim = tk.Button(self, text = "Simular", command = self.crear_tabla)
        self.boton_sim.grid(row = 1, column = 2)

        self.boton_f = tk.Button(self, text = "Menú", command  = lambda: controller.mostrar_Frame("h"))
        self.boton_f.grid(row = 1, column = 3)

        self.update()

    def update(self):
        if self.entrada_sim.get().isdecimal():
            self.boton_sim['state'] = tk.NORMAL
        else:
            self.boton_sim['state'] = tk.DISABLED
        
        self.after(1000,self.update)

    def animacion(self):
        # Haciendo uso de esta función conseguimos crear una animación en la que se puede observar 
        # como "pasan" los días en nuestras parcelas.
        if self.diasSim <= int(self.entrada_sim.get()):
            for barra in self.barras:
                if barra['value'] > 0:
                    barra['value'] -= 1
            self.diasSim += 1
            self.after(100,self.animacion)
    
    def datosSimulacion(self):
        return gnrl.registro_Simulacion_Dias()

    def crear_tabla(self):
        # Creamos de forma dinámica para visualizar de la forma más clara posible los datos.
        self.registros = gnrl.registro_Simulacion_Dias()

        self.label_1 = tk.Label(self, text= "Parcela")
        self.label_1.grid(row = 2, column = 1)
        self.label_2 = tk.Label(self, text= "Dias restantes")
        self.label_2.grid(row = 2, column = 2)

        for registro in self.registros:
            self.label = tk.Label(self, text = registro)
            self.label.grid(row = self.cnt, column = 1)
            self.progressbar = ttk.Progressbar(self)
            self.progressbar.grid(row = self.cnt, column = 2)
            self.progressbar['value'] = self.registros[registro]
            self.progressbar['maximum'] = self.registros[registro]
            self.barras.append(self.progressbar)
            self.cnt += 1
            print(self.cnt)
        
        gnrl.ejecutar_Simulacion_Dias(int(self.entrada_sim.get()))

        self.animacion()

# Informacion - Estado Parcelas
class f(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cnt = 3
        self.columnaIdentificador = []

        self.boton_Menu = tk.Button(self,text = "Menu", command = lambda: controller.mostrar_Frame("h"))
        self.boton_Menu.grid(row = 1, column = 1)

        self.label_1_1 = tk.Label(self, text = "Identificador")
        self.label_1_1.grid(row = 2, column = 1)

        self.label_1_2 = tk.Label(self, text = "Tipo")
        self.label_1_2.grid(row = 2, column = 2)

        self.label_1_3 = tk.Label(self, text = "Area")
        self.label_1_3.grid(row = 2, column = 3)

        self.update()

    def entrada_datos(self):
        return gnrl.enviar_estado_Parcelas()

    def update(self):
        global mostrar_parcelas
        if mostrar_parcelas == True:
            self.datos = {}
            self.datos = gnrl.enviar_estado_Parcelas()

            for dato in self.datos:
                if not (dato in self.columnaIdentificador):
                    self.label_1_1_t = tk.Label(self, text = self.datos[dato].identificador)
                    self.label_1_1_t.grid(row = self.cnt, column = 1)

                    self.label_1_2_t = tk.Label(self, text = self.datos[dato].tipoSuelo)
                    self.label_1_2_t.grid(row = self.cnt, column = 2)

                    self.label_1_3_t = tk.Label(self, text = self.datos[dato].areaParcela)
                    self.label_1_3_t.grid(row = self.cnt, column = 3)

                    self.columnaIdentificador.append(dato)
                
                self.cnt += 1
            
            mostrar_parcelas = False
        self.after(1000,self.update)

# Informacion - Cultivos Pendientes
class g(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cnt = 3
        self.columnaIdentificador = []

        self.label_1_1 = tk.Label(self, text = "Identificador")
        self.label_1_1.grid(row = 2, column = 1)

        self.label_1_3 = tk.Label(self, text = "Area")
        self.label_1_3.grid(row = 2, column = 3)

        self.boton_Menu = tk.Button(self,text = "Menu", command = lambda: controller.mostrar_Frame("h"))
        self.boton_Menu.grid(row = 1, column = 1)

        self.update()

    def entrada_datos(self):
        return gnrl.enviar_cultivos_Pendientes()
    
    def update(self):
        global mostrar_cultivos
        if mostrar_cultivos == True:

            self.datos = self.entrada_datos()

            for dato in self.datos:
                if not (dato in self.columnaIdentificador):
                    self.label_1_1_t = tk.Label(self, text = self.datos[dato].identificador)
                    self.label_1_1_t.grid(row = self.cnt, column = 1)

                    self.label_1_2_t = tk.Label(self, text = self.datos[dato].areaMinima)
                    self.label_1_2_t.grid(row = self.cnt, column = 2)

                    self.columnaIdentificador.append(dato)

                self.cnt += 1

            mostrar_cultivos = False

        self.after(1000,self.update)

# Informacion - Histórico de Cultivos
class i(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cnt = 3
        self.columnaIdentificador = []

        self.label_1_1 = tk.Label(self, text = "Identificador cultivo realizado")
        self.label_1_1.grid(row = 2, column = 1)

        self.boton_Menu = tk.Button(self,text = "Menu", command = lambda: controller.mostrar_Frame("h"))
        self.boton_Menu.grid(row = 1, column = 1)

        self.update()

    def entrada_datos(self):
        return gnrl.enviar_historico_Registros

    def update(self):
        global mostrar_historico
        if mostrar_historico == True:

            self.datos = gnrl.enviar_historico_Registros()

            for dato in self.datos:
                if not dato in self.columnaIdentificador:
                    self.label_1_1_t = tk.Label(self, text = self.datos[dato])
                    self.label_1_1_t.grid(row = self.cnt, column = 1)

                    self.columnaIdentificador.append(dato)

                self.cnt += 1

            mostrar_historico = False

        self.after(1000,self.update)

# Cargar y Guardar datos
class j(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.directorio = ""

        self.boton_1 = tk.Button(self, text = "Direción de la carpeta", command = self.carpeta)
        self.boton_1.grid(row = 1, column = 1)

        self.boton_2 = tk.Button(self, text = "Cargar Datos", command = self.cargar)
        self.boton_2.grid(row = 2, column = 1)
        
        self.boton_3 = tk.Button(self,text = "Guardar Datos", command = self.guardar)
        self.boton_3.grid(row = 3, column = 1)

        self.boton_Menu = tk.Button(self,text = "Menu", command = lambda: controller.mostrar_Frame("h"))
        self.boton_Menu.grid(row = 10, column = 1)

        self.update()

    def guardar(self):
        respuesta = messagebox.askquestion("Guardar", "Se sobreescribiran los datos guardados. ¿Desea guardar?")
        if respuesta == "yes":
            gnrl.guardar(self.directorio)

    def cargar(self):
        gnrl.cargar(self.directorio)

    def carpeta(self):
        self.directorio = gnrl.direccion_directorio()

    def update(self):
        # Mediante el uso de esta función bloquearemos las posibilidad de cargar o guardar un archivo en un lugar no deseado; 
        # es completamente obligatorio definir la ruta en la cual desea el usuario realizar las acciones de "guarda y cargar archivos".
        if self.directorio == "":
            self.boton_2['state'] = tk.DISABLED
            self.boton_3['state'] = tk.DISABLED
        else:
            self.boton_2['state'] = tk.NORMAL
            self.boton_3['state'] = tk.NORMAL

        self.after(1000, self.update)

# Ventana selección de accion información
class k(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.boton_1 = tk.Button(self, text = "Estado Parcelas", command = self.estado_parcelas)
        self.boton_1.grid(row = 1, column = 1)
        self.boton_2 = tk.Button(self, text = "Cultivos Pendientes", command = self.estado_cultivos)
        self.boton_2.grid(row = 2, column = 1)
        self.boton_3 = tk.Button(self, text = "Historico", command = self.estado_historico)
        self.boton_3.grid(row = 3, column = 1)

        self.boton_Menu = tk.Button(self,text = "Menu", command = lambda: controller.mostrar_Frame("h"))
        self.boton_Menu.grid(row = 10, column = 1)

    def estado_parcelas(self):
        global mostrar_parcelas
        
        mostrar_parcelas = True
        self.controller.mostrar_Frame('f')

    def estado_cultivos(self):
        global mostrar_cultivos

        mostrar_cultivos = True
        self.controller.mostrar_Frame('g')

    def estado_historico(self):
        global mostrar_historico

        mostrar_historico = True
        self.controller.mostrar_Frame('i')

app = VentanaPrincipal()
app.mainloop()
