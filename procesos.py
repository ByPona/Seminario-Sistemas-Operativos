class Proceso(object):

    def __init__(self, nombre, operacion, id_lote, tiempo):
        self.nombre = nombre
        self.operacion = operacion
        self.tiempo = tiempo
        self.id_lote = id_lote

    def darnombre(self):
        return self.nombre
    
    def dartiempo(self):
        return self.tiempo

    def daroperacion(self):
        return self.operacion

    def __str__(self):
        return "Nombre: %s\nOperacion: %s\nTiempo: %s\nID: %s" % (self.nombre, self.operacion, self.tiempo, self.id_lote)

class Proceso_Resultado(object):
    
    def __init__(self, numero, operacion, resultado,fila):
        self.numero = numero
        self.operacion = operacion
        self.resultado = resultado
        self.fila = fila

    def darfila(self):
        return self.fila

    def __str__(self):
        #return "Programa No.: %s        Operacion: %s          Resultado: %s,%s"%(self.numero, self.operacion, self.resultado, self.fila)
        return "Programa No.: %s        Operacion: %s          Resultado: %s"%(self.numero, self.operacion, self.resultado)
