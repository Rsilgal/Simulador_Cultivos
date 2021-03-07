class Info_Sistema():

    # def stateParcelas(self,diccionarioParcelas): #Muestra el estado de las parcelas
    #     self.mostrar_valores_diccionario(diccionarioParcelas)
    
    # def pendCultivo(self,diccionarioAsignaciones,diccionarioCultivos): #Indica los cultivos pendientes de realizarse
    #     self.mostrar_valores_diccionario(self.comparador_dicccionarios(diccionarioAsignaciones,diccionarioCultivos)
    
    # def histProduccion(self,diccionarioRegistro): #Imprime un historico de la producción realizada
    #     self.mostrar_valores_diccionario(diccionarioRegistro)

    # def mostrar_valores_diccionario(self,diccionario):
    #     lista_diccionario = list(diccionario.keys()) # Obtenemos una lista con las claves del diccionario de entrada

    #     for key in lista_diccionario:
    #         print(diccionario[key].__str__())  # Usando un bucle accedemos a todos los elementos del diccionario para imprimir su informacion.

    def comparador_dicccionarios(self,diccionario_1,diccionario_2):
        '''
        Este metodo compara dos diccionarios y te devuelve los valores existentes en diccionario_2 que 
        no existen en diccionario_1.
        '''
        lista_diccionario_1 = list(diccionario_1.values())
        lista_diccionario_2 = list(diccionario_2.keys())
        diccionario_diferencias = {}
        
        for elemento in lista_diccionario_2:        # Recorremos cada uno de los elementos presentes en la lista_2 
            if not elemento in lista_diccionario_1: # En el caso de que el elemento, de la lista_2, no este presente en la lista_1 
                diccionario_diferencias[elemento] = diccionario_2.get(elemento) # Agregaremos este elemento al diccionario de las diferencias

        return diccionario_diferencias