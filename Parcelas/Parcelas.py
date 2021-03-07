class Parcelas():
    identificador = ""  # Este valor será alfanumerico y no se puede repetir
    tipoSuelo = '' # El suelo de una parcela será de uno de estos 5: A,B,C,D o E
    areaParcela = 0 # El area de la parcela, en hectareas
    
    def __init__(self, identificador, tipoSuelo, areaParcela): #Creamos el constructor de la clase. En él se definiran los atributos del objeto
        self.identificador = identificador
        self.tipoSuelo = tipoSuelo
        self.areaParcela = areaParcela
    
    def __str__(self): #Es el mensaje por defecto si imprimios la clase.
        return "La parcela cuyo ID es {0} tiene una area de {2} hectareas y un suelo del tipo {1}".format(self.identificador, self.tipoSuelo, self.areaParcela)
        
    def transformacionSuelo(self, nuevoTipo): #Este método intercambia el tipo de suelo de la parcela por el indicado.
        self.tipoSuelo = nuevoTipo