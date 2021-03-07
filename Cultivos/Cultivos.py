class Cultivos():
    identificador = '' #Identificador alfanumerico UNICO del cultivo.
    posibleSuelo = [] #Lista de los suelos en los que es posible plantar el cultivo.
    areaMinima = 0 #Area minima necesaria para plantar el cultivo.
    canTransformar = False #Indica la propiedad del cultivo para modificar el tipo de terreno.
    nuevoSuelo = '' #En el caso de que modifique el tipo de suelo; el tipo al que cambia el suelo.
    duracionCultivo = 1 #Cantidad de días necesario para que se pueda cosechar lo cultivado.
    
    def __init__(self,identificador, posibleSuelo, areaMinima, canTransformar, nuevoSuelo, duracionCultivo): #Se trata del construtor de la clase
        self.identificador = identificador
        self.posibleSuelo = posibleSuelo
        self.areaMinima = areaMinima
        self.canTransformar = canTransformar
        self.nuevoSuelo = nuevoSuelo
        self.duracionCultivo = duracionCultivo
    
    def _str__(self): #Impresión que se mostrará a imprimir la clase
        return "El cultivo con el ID {0} tiene un area de {2} hecatreas, se puede cultivar en parcelas de los tipos {1}. Su duración es de {3} días.".format(self.identificador, self.posibleSuelo, self.areaMinima, self.duracionCultivo)
        
    def diasTranscurridos(self, factorDecremento = 1): #Método mediante el cual restaremos la cantidad de días deseada a los cultivos. Por defecto, el decremento de días será 1.
        self.duracionCultivo -= 1
