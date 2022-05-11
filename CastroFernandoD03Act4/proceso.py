class Proceso(object):

    def __init__(self, id, tiempo, transcurrido, operacion, operacion_resultado ):
        self.id = id
        self.tiempo = tiempo
        self.transcurrido = transcurrido
        self.operacion = operacion
        self.operacion_resultado = operacion_resultado

    def __str__(self):
        return "Programa No.: %s\nTiempo Estimado: %s\nTranscurrido %s" % (self.id, self.tiempo, self.transcurrido)

    #def darproceso(self):
        #return "ID: %s\nTiempo: %s\nOperacion: %s" % (self.id, self.tiempo, self.operacion)

    def dartiempo(self):
        return self.tiempo
    
    def darnumeroproceso(self):
        return self.id
    
    def daroperacion(self):
        return self.operacion

    def dartranscurrido(self):
        return self.transcurrido

    def darresultado(self):
        return self.operacion_resultado

    def establecertranscurrido(self, transcurrido):
        self.transcurrido = transcurrido
    
    def establecerresultado(self, operacion_resultado):
        self.operacion_resultado = operacion_resultado

    def darprocesosespera(self):
        print("Programa No.: %s\nTiempo Estimado: %s\nTranscurrido %s" % (self.id, self.tiempo, self.transcurrido))



