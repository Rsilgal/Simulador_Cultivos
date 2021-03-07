class Simulacion():
    def asignarCultivos(self,diccionarioParcelas, diccionarioCultivos,diccionarioAsignaciones): #Realiza la asiganción de los cultivos a la parcela correspondiente
        self.diccionarioParcelas = diccionarioParcelas
        self.diccionarioCultivos = diccionarioCultivos
        self.diccionarioAsignaciones = diccionarioAsignaciones
        # Recorremos todas las parcelas que tenemos guardadas en el sistema
        for parcela in diccionarioParcelas:
            id_cultivo_aux = 'NA'
            dif_parcela_cultivo = 99999999
            # Comprobamos cada uno de los cultivos
            for cultivo in diccionarioCultivos:
                # Recisamos la existencia del identificador del cultivo en la lista de valores del diccionario de asignaciones.
                # Si no está asignado, continuamos.
                if not (diccionarioCultivos[cultivo].identificador in list(diccionarioAsignaciones.values())):
                    # Comprobamos si el cultivo se puede plantar en el tipo de suelo de la parcela.
                    if(diccionarioParcelas[parcela].tipoSuelo in diccionarioCultivos[cultivo].posibleSuelo):
                        # Comprobación de si la parcela tiene espacio suficiente para albergar el cultivo.
                        if(diccionarioParcelas[parcela].areaParcela >= diccionarioCultivos[cultivo].areaMinima):
                            # Si la diefrencia de tamaño entre parcela y cultivo es menor que las comprobaciones anteriores
                            if((int(diccionarioParcelas[parcela].areaParcela) - int(diccionarioCultivos[cultivo].areaMinima)) < dif_parcela_cultivo):
                                # Guardamos el identificador del cultivo que mejor se adapta a la parcela
                                id_cultivo_aux = diccionarioCultivos[cultivo].identificador
                                # Guardamos un registro de la diferencias de tamaños para comprobar si hay otro cultivo que se adapte mejor
                                dif_parcela_cultivo = int(diccionarioParcelas[parcela].areaParcela) - int(diccionarioCultivos[cultivo].areaMinima)
                            
            if (id_cultivo_aux != 'NA'):
                diccionarioAsignaciones[diccionarioParcelas[parcela].identificador] = id_cultivo_aux
                print(diccionarioAsignaciones[diccionarioParcelas[parcela].identificador])
        
        for elemento in diccionarioAsignaciones:
            print("Para la parcela " + elemento + " ha sido asinado el cultivo " + diccionarioAsignaciones[elemento] + ".")
        
    def simDuracion(self, tiempoSimulacion,diccionarioParcelas, diccionarioCultivos,diccionarioAsignaciones,diccionarioRegistro): #Simulamos el paso del tiempo en cada uno de las parcelas
        self.diccionarioParcelas = diccionarioParcelas
        self.diccionarioCultivos = diccionarioCultivos
        self.diccionarioAsignaciones = diccionarioAsignaciones
        self.diccionarioRegistro = diccionarioRegistro    
        #Obtenemos la lista de claves del diccionario Asignaciones.
        dA = list(diccionarioAsignaciones.keys()) # Entrega las claves de las parcelas
        
        # Creamos un bucle en el que iteraremos hasta consumir los días a simular
        for dia in range(0,tiempoSimulacion):
            # Añadimos un bucle en el que recorreremos las parcelas para restar los días a los cultivos
            for parcela in dA:
                try:
                    # Accedemos al cultivo desde el identificador de la parcela y restamos un día al cultivo
                    diccionarioCultivos[diccionarioAsignaciones[parcela]].duracionCultivo = int(diccionarioCultivos[diccionarioAsignaciones[parcela]].duracionCultivo) - 1
                    
                    if (int(diccionarioCultivos[diccionarioAsignaciones[parcela]].duracionCultivo) == 0):
                        # Si el cultivo con el que estamos trabajando transforma el suelo de la parcela
                        if (diccionarioCultivos[diccionarioAsignaciones[parcela]].canTransformar):
                            # Cambiamos el tipo de suelo de la parcela
                            diccionarioParcelas[parcela].tipoSuelo = diccionarioCultivos[diccionarioAsignaciones[parcela]].nuevoSuelo
                        # Añadimos el cultivo al registro de cultivos que han sido producidos
                        diccionarioRegistro[parcela] = diccionarioAsignaciones[parcela]
                        # Eliminamos el cultivo producido del registro de control actual
                        del diccionarioCultivos[diccionarioAsignaciones[parcela]]
                        # Borramos la asignación de la parcela con el cultivo producido
                        del diccionarioAsignaciones[parcela]
                except KeyError:
                    pass

    def enviarDatosSimulacion(self, diccionarioCultivos, diccionarioAsignaciones):
        self.diccionarioCultivos = diccionarioCultivos
        self.diccionarioAsignaciones = diccionarioAsignaciones
        #Obtenemos la lista de claves del diccionario Asignaciones.
        dA = list(diccionarioAsignaciones.keys()) # Entrega las claves de las parcelas
        diccionarioRetorno = {}

        # Añadimos un bucle en el que recorreremos las parcelas para restar los días a los cultivos
        for parcela in dA:
            diccionarioRetorno[parcela] = diccionarioCultivos[diccionarioAsignaciones[parcela]].duracionCultivo
        return diccionarioRetorno
