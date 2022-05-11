import numpy as np 
import math 
import random
from proceso import Proceso
import os
import time
import keyboard
        
def evaluar_hora():
    tiempo = time.strftime('%H:%M:%S',time.localtime())
    tiempostr = str(tiempo)

    hora = tiempostr[0] + tiempostr[1]
    minuto = tiempostr[3] + tiempostr[4]
    segundo = tiempostr[6] + tiempostr[7]

    hora = int(hora)
    hora = hora*60*60
    minuto = int(minuto)
    minuto = minuto*60
    segundo = int(segundo)
    total = hora + minuto + segundo
    return total

prueba = Proceso("","",0,"","")

num_procesos = int(input("Dame el numero de procesos: "))
num_lotes = num_procesos/5
redondeado = math.ceil(num_lotes)
matriz = np.full((redondeado,5),prueba)

fila = 0 
columna = 0
contador_procesos = 1
lista_operandos = ["+","-","/","*"]



while contador_procesos <= num_procesos:
    tiempo_proceso = random.randint(6,16)
    
    var1_proceso = random.randint(0, 100)
    var1_proceso = str(var1_proceso)
    var2_proceso = random.randint(1, 100)
    var2_proceso = str(var2_proceso)
    var3_proceso = random.randint(0, 3)
    var4_proceso = lista_operandos[var3_proceso]
    operacion_proceso = var1_proceso + var4_proceso + var2_proceso
    operacion_resultado = eval(operacion_proceso)

    objeto = Proceso(contador_procesos, tiempo_proceso, 0, operacion_proceso, operacion_resultado)

    matriz[fila][columna] = objeto

    columna = columna + 1
    if columna == 5:
        fila = fila + 1
        columna = 0
    contador_procesos = contador_procesos+1

#MOSTRAR INFORMACION
contador_programa = 1
redondeado = redondeado-1
fila = 0
columna = 0
tiempo_estimado = -1
lista_enproceso = list()
lista_terminada = list()
lista_procesos_terminados = list()

procesos_espera_columna = 1
activador = 0
x = 0
hora_inicial = evaluar_hora()
while contador_programa <= num_procesos:
    contador_procesos_terminados = 0
    x = 0
    activador_llenado_terminado = 0
    if len(lista_enproceso) == 0:
        if redondeado!=0:
            for x in range(5):
                aux = matriz[fila][columna+x]
                lista_enproceso.append(aux)
        x = 0

    if len(lista_enproceso) == 0:
        auxprocvar = num_procesos%5

        for x in range(auxprocvar):
            aux = matriz[fila][columna+x]
            lista_enproceso.append(aux)  

        x = 0

    print("#################################################")
    print("Numero de lotes pendientes: ", redondeado)
    print("================================================")
    print("Procesos en Espera")
    print("================================================")
    for n in lista_enproceso:
        if x == 1:
            print(n)
        x = 1
        print("------------------------")
    print("================================================")
    print("Procesos Terminados")
    print("================================================")
    while contador_procesos_terminados < len(lista_procesos_terminados):
        aux = lista_procesos_terminados[contador_procesos_terminados]
        programa_numero = aux.darnumeroproceso()
        tiempo_estimado_programa = aux.dartiempo()
        print("Programa No.: ",programa_numero,"\nTiempo Estimado: ",tiempo_estimado_programa,"\nTranscurrido: ",tiempo_estimado_programa)
        print("------------------------")
        contador_procesos_terminados = contador_procesos_terminados+1
    print("Proceso en Ejecucion")
    print("================================================")
    aux = lista_enproceso[0]
    contador_objeto = aux.darnumeroproceso()
    print("Programa No.: ", contador_objeto)
    prueba = aux
    print("ID: ",contador_objeto)
    
    tiempo_estimado = aux.dartiempo()
    print("Tiempo Maximo Estimado: ",tiempo_estimado)
    contador_tiempo_estimado = aux.dartranscurrido()
    operacion_aux = aux.daroperacion()
    print("Operacion: ", operacion_aux)
    operacion_resultado = eval(operacion_aux)
    

    print("Tiempo transcurrido:     Tiempo Restante por ejecutar")
    while contador_tiempo_estimado < tiempo_estimado:

        restante = tiempo_estimado - contador_tiempo_estimado
        print(contador_tiempo_estimado, "                      ", restante)
        contador_tiempo_estimado = contador_tiempo_estimado + 1  
        if keyboard.is_pressed('i'):
            print("==============")
            print("|INTERRUPCION|")
            print("==============")
            time.sleep(0.5)
            aux.establecertranscurrido(contador_tiempo_estimado)
            lista_enproceso.append(aux)
            activador_llenado_terminado = 1
            columna = columna - 1
            num_procesos = num_procesos + 1
            break
        if keyboard.is_pressed('e'):
            print("==============")
            print("|ERROR|")
            print("==============")
            time.sleep(0.5)
            aux.establecerresultado("ERROR")
            lista_enproceso[0] = aux
            break
        if keyboard.is_pressed('p'):
            print("==============")
            print("|PAUSA|")
            print("==============")
            print("Presione la tecla 'c' para continuar")
            while keyboard.is_pressed('c') != True:
                continue

        time.sleep(1.0) 
        
    restante = tiempo_estimado - contador_tiempo_estimado
    print(contador_tiempo_estimado, "                      ", restante)

    columna = columna+1

    if len(lista_enproceso) != 0:
        if activador_llenado_terminado != 1:
            aux = lista_enproceso[0]
            lista_terminada.append(aux)
            lista_procesos_terminados.append(aux)
        objeto_aux = lista_enproceso.pop(0)
            
    if len(lista_enproceso) == 0:
        redondeado = redondeado-1
        lista_procesos_terminados = list()
        fila = fila+1
        columna = 0
        x = 0

    contador_tiempo_estimado = 0
    contador_programa = contador_programa+1

contador_final = 0
while contador_final < len(lista_terminada):
    aux = lista_terminada[contador_final]
    numero_proceso_result = aux.darnumeroproceso()
    operacion_proceso_result = aux.daroperacion()
    resultado_proceso_result = aux.darresultado()
    print("\n\nNumero de Programa: ",numero_proceso_result,"\nOperacion: ",operacion_proceso_result,"\nResultado: ",resultado_proceso_result,"\n")
    contador_final = contador_final+1

hora_final = evaluar_hora()
print("Tiempo total del programa: ",hora_final - hora_inicial)
os.system("pause")
os.system("cls")        



    



