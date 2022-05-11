class Proceso(object):

    def __init__(self, id, tiempo, transcurrido, operacion, operacion_resultado, tiempo_bloqueado, tiempo_de_llegada, tiempo_de_finalizacion, tiempo_de_retorno, tiempo_de_respuesta, tiempo_de_espera, tiempo_de_servicio, hora_inicial, tiempo_que_lleva_bloqueado):
        self.id = id
        self.tiempo = tiempo
        self.transcurrido = transcurrido
        self.operacion = operacion
        self.operacion_resultado = operacion_resultado
        self.tiempo_bloqueado = tiempo_bloqueado
        self.tiempo_de_llegada = tiempo_de_llegada
        self.tiempo_de_finalizacion = tiempo_de_finalizacion
        self.tiempo_de_retorno = tiempo_de_retorno
        self.tiempo_de_respuesta = tiempo_de_respuesta
        self.tiempo_de_espera = tiempo_de_espera
        self.tiempo_de_servicio = tiempo_de_servicio
        self.hora_inicial = hora_inicial
        self.tiempo_que_lleva_bloqueado = tiempo_que_lleva_bloqueado

    def darnuevo(self):
        return "Programa No.: %s\nTiempo Estimado: %s\nTiempo Transcurrido: %s" % (self.id, self.tiempo, self.transcurrido)
    
    def darid(self):
        return self.id
    
    def dartiempo(self):
        return self.tiempo

    def dartranscurrido(self):
        return self.transcurrido
    
    def daroperacion(self):
        return self.operacion

    def darresultado(self):
        return self.operacion_resultado

    def darbloqueado(self):
        return self.tiempo_bloqueado

    def darhorainicial(self):
        return self.hora_inicial
    
    def dartiempoquellevabloqueado(self):
        return self.tiempo_que_lleva_bloqueado

    def darllegada(self):
        return self.tiempo_de_llegada

    def establecertranscurrido(self, transcurrido):
        self.transcurrido = transcurrido

    def establecertiempobloqueado(self, bloqueado):
        self.tiempo_bloqueado = bloqueado

    def establecerresultado(self, resultado):
        self.operacion_resultado = resultado

    def establecerllegada(self, llegada):
        self.tiempo_de_llegada = llegada

    def establecerfinalizacion(self, finalizacion):
        self.tiempo_de_finalizacion = finalizacion
    
    def establecerretorno(self, retorno):
        self.tiempo_de_retorno = retorno

    def establecerrespuesta(self, respuesta):
        self.tiempo_de_respuesta = respuesta
    
    def establecerespera(self, espera):
        self.tiempo_de_espera = espera

    def establecerservicio(self, servicio):
        self.tiempo_de_servicio = servicio

    def establecerhorainicial(self, inicial):
        self.hora_inicial = inicial

    def establecertiempoquellevabloqueado(self, bloque):
        self.tiempo_que_lleva_bloqueado = bloque

    def __str__(self):
        return "Programa No.: %s\nTiempo Estimado: %s\nTranscurrido: %s" % (self.id, self.tiempo, self.transcurrido)

    def darfinalizacion(self):
        return "Programa No.: %s\nEstado: Terminado\nTiempo Estimado: %s\nTranscurrido: %s\nOperacion: %s\nRespuesta: %s\nTiempos\nLlegada: %s\nFinalizacion: %s\nRetorno: %s\nRespuesta: %s\nEspera: %s\nServicio: %s\n" % (self.id, self.tiempo,self.transcurrido,self.operacion, self.operacion_resultado,self.tiempo_de_llegada,self.tiempo_de_finalizacion, self.tiempo_de_retorno, self.tiempo_de_respuesta, self.tiempo_de_espera, self.tiempo_de_servicio)
    
    def darfinal(self):
        return "Programa No.: %s\nTiempo Estimado: %s\nTranscurrido: %s\nOperacion: %s\nRespuesta: %s\nTiempos\nLlegada: %s\nFinalizacion: %s\nRetorno: %s\nRespuesta: %s\nEspera: %s\nServicio: %s\n" % (self.id, self.tiempo,self.transcurrido,self.operacion, self.operacion_resultado,self.tiempo_de_llegada,self.tiempo_de_finalizacion, self.tiempo_de_retorno, self.tiempo_de_respuesta, self.tiempo_de_espera, self.tiempo_de_servicio)

    def darteclat(self):
        if self.tiempo_de_llegada==-1:
            return "Programa No.: %s\nEstado: Nuevo\nOperacion: %s\nResultado: NULL\nLlegada: NULL\nFinalizacion: NULL\nRetorno: NULL\nEspera: NULL\nEspera: NULL\nServicio: NULL\nRestante: NULL\nRespuesta: NULL\n" % (self.id, self.operacion)
        elif self.tiempo_bloqueado>0:
            return "Programa No.: %s\nEstado: Bloqueado\nOperacion: %s\nResultado: NULL\nLlegada: %s\nFinalizacion: NULL\nRetorno: NULL\nEspera: NULL\nEspera: %s\nServicio: NULL\nRespuesta: %s\nTiempo Bloqueado: %s\n" % (self.id, self.operacion,self.tiempo_de_llegada,self.tiempo_de_espera,self.tiempo_de_respuesta,self.tiempo_que_lleva_bloqueado)
        elif self.tiempo_de_finalizacion!=0:
            return "Programa No.: %s\nEstado: Listo\n Operacion: %s\nResultado: NULL\nLlegada: %s\nFinalizacion: NULL\nRetorno: NULL\nEspera: NULL\nServicio: NULL\nRespuesta: NULL\nTiempo Bloqueado: NULL\n" % (self.id, self.operacion, self.tiempo_de_llegada)
        else:
            return "Programa No.: %s\nEstado: Terminado\nTiempo Estimado: %s\nTranscurrido: %s\nOperacion: %s\nRespuesta: %s\nTiempos\nLlegada: %s\nFinalizacion: %s\nRetorno: %s\nRespuesta: %s\nEspera: %s\nServicio: %s\n" % (self.id, self.tiempo,self.transcurrido,self.operacion, self.operacion_resultado,self.tiempo_de_llegada,self.tiempo_de_finalizacion, self.tiempo_de_retorno, self.tiempo_de_respuesta, self.tiempo_de_espera, self.tiempo_de_servicio)
        