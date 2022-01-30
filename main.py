import numpy as np
import math
from procesos import Proceso
from procesos import Proceso_Resultado
import os
import time

def evaluar_tiempo(tiempo):
    while tiempo<=0:
        print("----------------------------------")
        print("Error tiempo menor o igual a 0")
        print("----------------------------------")
        tiempo = int(input("Dame el tiempo: "))
    return True 

def evaluar_operacion(operacion):
    activador = 0
    try:
        eval(operacion)
    except:
        print("---------------------")
        print("Operacion invalida")
        print("---------------------")
        activador = 1

    while activador == 1:
        operacion = input("Dame la operacion (x+x,x-x,x*x,x/x): ")
        activador = 0
        try:
            eval(operacion)
        except:
            print("---------------------")
            print("Operacion invalida")
            print("---------------------")
            activador = 1
    return operacion

def evaluar_id1(numero, lista):
    activador = 0
    for n in lista:
        if n == numero:
            activador = 1
    if activador == 1:
        return False
    else: 
        return True

def evaluar_id2(numero, lista):
    while evaluar_id1(numero, lista) == False:
        print("-----------------------")
        print("Dato duplicado")
        print("-----------------------")
        numero = int(input("Dame el ID: "))
    return numero

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

prueba = Proceso("", "", "","")
activador = 0
contador_procesos = 0
lista_id = list()

num_procesos = int(input("Dame el numero de procesos: "))
num_lotes = num_procesos/5
redondeado = math.ceil(num_lotes) #Lo redondeamos para crear la matriz de objetos
matriz = np.full((redondeado,5),prueba)

fila = 0
columna = 0
#Almacenar informacion
while contador_procesos < num_procesos:
#Comenzamos a pedir los parametros
    nombre_objeto = input("Dame el nombre: ")

    operacion_objeto = input("Dame la operacion (x+x,x-x,x*x,x/x): ")
    operacion_objeto = evaluar_operacion(operacion_objeto)

    tiempo_objeto = int(input("Dame el tiempo (segundos): "))
    evaluar_tiempo(tiempo_objeto)

    id_objeto = int(input("Dame el ID: "))
    id_objeto = evaluar_id2(id_objeto,lista_id)
    lista_id.append(id_objeto)

    objeto = Proceso(nombre_objeto, operacion_objeto, id_objeto, tiempo_objeto)
    matriz[fila][columna] = objeto
    os.system('cls')
    print("Informacion Almacenada\n----------------------")
    print("Nombre: ", nombre_objeto)
    print("Operacion: ", operacion_objeto)
    print("Tiempo: ", tiempo_objeto)
    print("ID: ", id_objeto)
    print("----------------------")
    columna = columna + 1

    if columna >= 5:
        fila = fila + 1
        columna = 0
    contador_procesos = contador_procesos + 1

os.system("cls")

#Fin almacenado informacion
contador_programa = 1
redondeado = redondeado - 1
fila = 0
columna = 0
tiempo_estimado = 0
contador_tiempo_transcurrido = 0
lista_resultado = list()
hora_inicial = evaluar_hora()
while contador_programa <= num_procesos:
    print("--------------------------------------------")
    print("Numero de lotes pendientes: ",  redondeado)
    print("--------------------------------------------")
    print("Programa No.: ", contador_programa)
    aux = matriz[fila][columna]
    tiempo_estimado = aux.dartiempo()
    operacionaux = aux.daroperacion()
    operacion_resultado = eval(operacionaux)

    print("Tiempo Maximo Estimado: ",  tiempo_estimado)
    print(aux)
    objeto2 = Proceso_Resultado(contador_programa, operacionaux , operacion_resultado, fila)
    lista_resultado.append(objeto2)

    print("Tiempo transcurrido:     Tiempo Restante por ejecutar")
    
    while contador_tiempo_transcurrido < tiempo_estimado:
        restante = tiempo_estimado - contador_tiempo_transcurrido 
        print(contador_tiempo_transcurrido, "                      ", restante)
        contador_tiempo_transcurrido = contador_tiempo_transcurrido + 1
        time.sleep(1.0)

    columna = columna+1

    if columna==5:
        #os.system("cls")
        #print("             \nProcesos Terminados")
        #print("-----------------------------------------------")
        #for n in lista_resultado:
            #objeto = n
            #filaaux = objeto.darfila()
            #if filaaux == fila:
                #print(filaaux)
                #print(n)
        redondeado = redondeado - 1
        fila = fila+1
        columna = 0
        filaaux = 0
        

    if contador_programa == num_procesos:
        os.system("cls")
        print("             \nProcesos Terminados")
        print("-----------------------------------------------")
        for n in lista_resultado:
            #objeto = n
            #filaaux = objeto.darfila()
            #if filaaux == fila:
                #print(filaaux)
            print(n)
        redondeado = redondeado - 1
        fila = fila+1
        columna = 0
        filaaux = 0

    
    contador_tiempo_transcurrido = 0
    #print(fila,columna)
    




    contador_programa = contador_programa + 1
    
    

hora_final = evaluar_hora()
print("Tiempo total del programa: ",hora_final - hora_inicial)
os.system("pause")
os.system("cls")



#print("Numero de lotes pendientes %s")
