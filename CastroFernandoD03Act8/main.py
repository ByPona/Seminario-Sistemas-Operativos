from multiprocessing import ProcessError
from proceso import Proceso
import random
import time
from multiprocessing.connection import wait
import keyboard
import os

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

def agregarnuevoproceso(contador_procesos):
    contador_procesos = contador_procesos+1
    tiempo_proceso = random.randint(6,16)
    
    var1_proceso = random.randint(0, 100)
    var1_proceso = str(var1_proceso)
    var2_proceso = random.randint(1, 100)
    var2_proceso = str(var2_proceso)
    var3_proceso = random.randint(0, 3)
    var4_proceso = lista_operandos[var3_proceso]
    operacion_proceso = var1_proceso + var4_proceso + var2_proceso
    operacion_resultado = eval(operacion_proceso)

    objeto = Proceso(contador_procesos, tiempo_proceso, 0, operacion_proceso, operacion_resultado,0,0,0,"0",0,0,0,0,0)
    lista_nuevo.append(objeto)
    contador_procesos = contador_procesos+1

num_procesos = int(input("Dame el numero de procesos: "))

lista_nuevo = list()

contador_procesos = 0
lista_operandos = ["+","-","/","*"]

while contador_procesos < num_procesos:
    contador_procesos = contador_procesos+1
    tiempo_proceso = random.randint(6,16)
    
    var1_proceso = random.randint(0, 100)
    var1_proceso = str(var1_proceso)
    var2_proceso = random.randint(1, 100)
    var2_proceso = str(var2_proceso)
    var3_proceso = random.randint(0, 3)
    var4_proceso = lista_operandos[var3_proceso]
    operacion_proceso = var1_proceso + var4_proceso + var2_proceso
    operacion_resultado = eval(operacion_proceso)

    objeto = Proceso(contador_procesos, tiempo_proceso, 0, operacion_proceso, operacion_resultado,0,0,0,"0",0,0,0,0,0)
    lista_nuevo.append(objeto)

    

lista_listos = list()
lista_bloqueado = list()
lista_terminado = list()

lista_aborrar = list()
contador_tiempo = 1

start = time.time()
for r in range(1,20000):
    pass


restante = 0
inicio_principal = evaluar_hora()
while True:
    activador = 0  
    contador_bloqueados = 0
    if len(lista_bloqueado) > 0:
        while contador_bloqueados < len(lista_bloqueado):
            
            inicio = lista_bloqueado[contador_bloqueados].darbloqueado()
            fin = evaluar_hora()
            hora = fin-inicio
            #print(hora)
            #os.system("pause")
            lista_bloqueado[contador_bloqueados].establecertiempoquellevabloqueado(hora)
            if hora>=8:
                aux = lista_bloqueado.pop(contador_bloqueados)
                lista_listos.append(aux)
                contador_bloqueados = contador_bloqueados-1
            contador_bloqueados = contador_bloqueados+1

    #print(len(lista_nuevo))  
    #print(len(lista_listos)) 
    #print(len(lista_bloqueado))  
    #os.system("pause")      
    

    if len(lista_nuevo) == 0 and len(lista_listos) == 0 and len(lista_bloqueado) == 0:
        break

    if len(lista_listos) < 5 and len(lista_nuevo) > 0:
        while len(lista_listos) < 5 and len(lista_nuevo) > 0:
            aux = lista_nuevo.pop(0)
            tiempo = time.strftime('%H:%M:%S',time.localtime())
            tiempostr = str(tiempo)
            aux.establecerllegada(tiempostr)
            inicio = time.time()
            aux.establecerhorainicial(inicio)
            hora2 = format(inicio-start)
            aux.establecerespera(hora2)
            lista_listos.append(aux)

    if len(lista_listos) > 0:
        aux = lista_listos.pop(0)
    print("=========PROCESOS EN NUEVO=============")
    print("Procesos en Nuevo: ", len(lista_nuevo))
    print("=========COLA DE LISTOS================")
    for n in lista_listos:
        print(n)
        print('--------------------------')
    print("=========COLA DE BLOQUEADOS============")
    for n in lista_bloqueado:
        print(n)
        print("Tiempo Bloqueado: ", n.dartiempoquellevabloqueado())
        print('--------------------------')
    print("=========PROCESOS TERMINADOS===========")
    for n in lista_terminado:
        print("ID: ",n.darid())
        print("Operacion: ",n.daroperacion())
        print("Resultado: ",n.darresultado())
        print('--------------------------')
    print("=========PROCESOS EN EJECUCION=========")
    obj_id = aux.darid()
    obj_tiempo = aux.dartiempo()
    obj_transc = aux.dartranscurrido()
    obj_oper = aux.daroperacion()
    print("Programa No.: ", obj_id)
    print("Operacion: ", obj_oper)
    print("Tiempo Estimado: ", obj_tiempo)
    contador_tiempo = obj_transc

    print("Tiempo transcurrido:     Tiempo Restante por ejecutar")
    restante = obj_tiempo

    aux_retorno = aux.darhorainicial()
    fin = time.time()
    hora = format(fin-aux_retorno)
    aux.establecerrespuesta(hora)
    

    while contador_tiempo < obj_tiempo:
        time.sleep(1)
        contador_tiempo = contador_tiempo + 1
        restante = restante - 1
        print(contador_tiempo-obj_transc,"                      ",restante-obj_transc)
        if keyboard.is_pressed('i'):
            print("==============")
            print("|INTERRUPCION|")
            print("==============")
            time.sleep(0.5)
            aux.establecertranscurrido(contador_tiempo)
            hora_inicio_bloqueado = evaluar_hora()
            aux.establecertiempobloqueado(hora_inicio_bloqueado)

            lista_bloqueado.append(aux)
            activador = 1
            break
        if keyboard.is_pressed('e'):
            print("==============")
            print("|ERROR|")
            print("==============")
            time.sleep(0.5)
            aux.establecerresultado("ERROR")
            tiempo = time.strftime('%H:%M:%S',time.localtime())
            tiempostr = str(tiempo)
            aux.establecerfinalizacion(tiempostr)
            aux.establecertranscurrido(contador_tiempo)

            aux_retorno = aux.darhorainicial()
            fin = time.time()
            hora = format(fin-aux_retorno)
            aux.establecerretorno(hora)

            hora2 = format(fin-start)
            aux.establecerservicio(hora2)

            lista_terminado.append(aux)
            activador = 1
            break 
        if keyboard.is_pressed('p'):
            print("==============")
            print("|PAUSA|")
            print("==============")
            print("Presione la tecla 'c' para continuar")
            while keyboard.is_pressed('c') != True:
                continue
        if keyboard.is_pressed('n'):
            print("==============")
            print("|NUEVO PROCESO CREADO|")
            print("==============")
            agregarnuevoproceso(contador_procesos)
            contador_procesos = contador_procesos+1
        
        if keyboard.is_pressed('t'):
            print("==============")
            print('TABLA DE PROCESOS')
            print("==============")
            print("=========COLA DE NUEVOS================")
            for n in lista_nuevo:
                print(n.darteclat())
                print('--------------------------')
            print("=========COLA DE LISTOS================")
            for n in lista_listos:
                print(n.darteclat())
                print('--------------------------')
            print("=========COLA DE BLOQUEADOS============")
            for n in lista_bloqueado:
                print(n.darteclat())
                print('--------------------------')
            print("=========PROCESOS TERMINADOS===========")
            for n in lista_terminado:
                print(n.darteclat())
                print('--------------------------')
            print("Presione la tecla 'c' para continuar")
            while keyboard.is_pressed('c') != True:
                continue


    if activador != 1:
        tiem = aux.dartiempo()
        aux.establecertranscurrido(tiem)

        aux.establecerfinalizacion(tiempostr)

        fin = time.time()
        hora = format(fin-aux_retorno)
        aux.establecerretorno(hora)

        tiempo = time.strftime('%H:%M:%S',time.localtime())
        tiempostr = str(tiempo)
        aux.establecerfinalizacion(tiempostr)
        hora2 = format(fin-start)
        aux.establecerservicio(hora2)

        lista_terminado.append(aux)
        
os.system("cls")
for n in lista_terminado:
    print(n.darfinal())

fin_principal = evaluar_hora()
print("Tiempo Total: ", fin_principal-inicio_principal)
        

    

    





