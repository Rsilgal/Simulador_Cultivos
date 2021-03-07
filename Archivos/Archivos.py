class Archivos():

    def crear_fichero(self,direccion):
        try:
            fichero = open(direccion,'w')
        except IOError as e:
            print('Error' + e.__doc__)
        finally:
            fichero.close()


    def guardar(self, ruta, diccionario, accion = 0):
        '''
        diccionario - Dicccionario que se quiere guardar en el archivo
        accion - 0 (Parcela), 1 (Cultivo), 2 (Registro), 3 (Asiganciones)
        '''
        try:
            fichero = open(ruta,'w')
            for elemento in diccionario:
                if accion == 0:
                    print("Parcela")
                    fichero.write(self.formateo_datos_Parcela(diccionario[elemento]) + '\n')
                if accion == 1:
                    print("Cultivo")
                    fichero.write(self.formateo_datos_Cultivo(diccionario[elemento]) + '\n')
                if accion == 2:
                    print("Registro")
                    fichero.write(self.formateo_datos_Registro(diccionario) + '\n')
                if accion == 3:
                    print("Asignaciones")
                    fichero.write(self.formateo_datos_Asignaciones(diccionario) + '\n')

        except BaseException as e:
            print(e.__doc__)

        finally:
            fichero.close()

    def cargar(self, ruta):
        try:
            fichero = open(ruta,'r')
            lineas = fichero.readlines()
            return lineas                

        except BaseException as e:
            print(e.__doc__)

        finally:
            fichero.close()


    def formateo_datos_Parcela(self,objeto):
        return "{0}/{1}/{2}/".format(objeto.identificador,objeto.tipoSuelo,objeto.areaParcela)

    def formateo_datos_Cultivo(self,objeto):
        return "{0}/{1}/{2}/{3}/{4}/{5}/".format(objeto.identificador,objeto.posibleSuelo,objeto.areaMinima,objeto.canTransformar,objeto.nuevoSuelo,objeto.duracionCultivo)

    def formateo_datos_Registro(self,elemento):
        clave = list(elemento.keys())[0]
        return "{0}/{1}/".format(clave, elemento[clave])


    def formateo_datos_Asignaciones(self, elemento):
        clave = list(elemento.keys())[0]
        return "{0}/{1}/".format(clave, elemento[clave])