import Parcelas.Parcelas as pcl
import Cultivos.Cultivos as clt
import Simulacion.Simulacion as sim
import Info_Sistemas.Info_Sistemas as inf #TODO: Existe la posibilidad de eliminar el paquete Info_Sistemas
import Archivos.Archivos as arc
from tkinter import filedialog

diccionarioParcelas = {}
diccionarioCultivos = {}
diccionarioAsignaciones = {}
diccionarioRegistro = {}
ruta_archivo = [r"\Parcelas.txt",r"\Cultivos.txt",r"\Registro.txt",r"\Asignaciones.txt"]

def añadir_Parcela(identificador, area, suelo):
    p = pcl.Parcelas(identificador,suelo, int(area))
    diccionarioParcelas[p.identificador] = p

def identificador_unico_Parcela(identificador):
    claves = list(diccionarioParcelas.keys())
    if not identificador in claves:
        return True
    else:
        return False

def añadir_Cultivo(identificador, suelo, area, duracion, transforma = False, nuevoSuelo = ''):
    c = clt.Cultivos(identificador, suelo, int(area), bool(transforma), nuevoSuelo, int(duracion))
    diccionarioCultivos[c.identificador] = c

def identificador_unico_Cultivo(identificador):
    claves = list(diccionarioCultivos.keys())
    if not identificador in claves:
        return True
    else:
        return False

def ejecutar_Asignacion():
    s = sim.Simulacion()
    s.asignarCultivos(diccionarioParcelas,diccionarioCultivos,diccionarioAsignaciones)

def registro_Asignaciones():
    return diccionarioAsignaciones

def ejecutar_Simulacion_Dias(dias):
    s = sim.Simulacion()
    s.simDuracion(dias,diccionarioParcelas,diccionarioCultivos,diccionarioAsignaciones,diccionarioRegistro)

def registro_Simulacion_Dias():
    s = sim.Simulacion()
    return s.enviarDatosSimulacion(diccionarioCultivos,diccionarioAsignaciones)

def enviar_estado_Parcelas():
    return diccionarioParcelas

def enviar_estado_Cultivos():
    return diccionarioCultivos

def enviar_cultivos_Pendientes():
    return inf.Info_Sistema().comparador_dicccionarios(diccionarioAsignaciones,diccionarioCultivos)

def enviar_historico_Registros():
    return diccionarioRegistro

def guardar(carpeta):
    a = arc.Archivos()
    a.guardar(carpeta + ruta_archivo[0],diccionarioParcelas,accion=0)
    a.guardar(carpeta + ruta_archivo[1],diccionarioCultivos,accion=1)
    a.guardar(carpeta + ruta_archivo[2],diccionarioRegistro,accion=2)
    a.guardar(carpeta + ruta_archivo[3],diccionarioAsignaciones,accion=3)

def cargar(carpeta):
    a = arc.Archivos()
    crear_parcela_cargada(a.cargar(carpeta + ruta_archivo[0]))
    crear_cultivo_cargado(a.cargar(carpeta + ruta_archivo[1]))
    crear_asignacion_cargada(a.cargar(carpeta + ruta_archivo[3]))
    crear_registro_cargado(a.cargar(carpeta + ruta_archivo[2]))

def crear_parcela_cargada(datos_lectura):
    for dato in datos_lectura:
        dato = dato.split('/')
        añadir_Parcela(dato[0],dato[2],dato[1])

def crear_cultivo_cargado(datos_lectura):
    for dato in datos_lectura:
        dato = dato.split('/')
        añadir_Cultivo(dato[0],list(dato[1]),dato[2],dato[5],dato[3],dato[4])

def crear_asignacion_cargada(datos_lectura):
    for dato in datos_lectura:
        dato = dato.split('/')
        diccionarioAsignaciones[dato[0]] = dato[1]

def crear_registro_cargado(datos_lectura):
    for dato in datos_lectura:
        dato = dato.split('/')
        diccionarioRegistro[dato[0]] = dato[1]

def direccion_directorio():
    carpeta = filedialog.askdirectory()
    if carpeta != "":
        return carpeta
    else:
        return ""