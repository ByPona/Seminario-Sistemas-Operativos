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
valor_quantum = int(input("Dame el valor del Quantum: "))

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

    objeto = Proceso(contador_procesos, tiempo_proceso, 0, operacion_proceso, operacion_resultado,-1,-1,-1,-1,-1,-1,-1,-1,-1)
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
            
            fin_llegada = evaluar_hora()
            aux_llegada = fin_llegada - inicio_principal
            aux.establecerllegada(aux_llegada)
            
            llegada_hora_inicial = evaluar_hora()
            hora_espera = llegada_hora_inicial - inicio_principal
            
            aux.establecerespera(hora_espera)
            aux.establecerhorainicial(llegada_hora_inicial)
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

    print("Tiempo transcurrido:     Tiempo Restante por ejecutar            Quantum")
    restante = obj_tiempo

    aux_retorno = aux.darhorainicial()
    aux_res = evaluar_hora()
    aux_res = aux_res - aux_retorno 

    aux.establecerrespuesta(aux_res)
    aux.establecerespera(aux_res)
    
    quantum = 0
    while contador_tiempo < obj_tiempo:
        time.sleep(1)
        contador_tiempo = contador_tiempo + 1
        restante = restante - 1
        quantum = quantum + 1
        cont1 = contador_tiempo-obj_transc
        cont2 = restante-obj_transc
        print(cont1,"                      ",cont2, "                                       ", quantum)
        if quantum==valor_quantum:
            if cont2==0:
                pass
            else:
                aux_quantum = aux.dartranscurrido()
                aux.establecertranscurrido(aux_quantum + valor_quantum)
                lista_listos.append(aux)
                activador = 1
                break
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
            fin_finalizacion = evaluar_hora()
            aux_finalizacion = fin_finalizacion - inicio_principal
            aux.establecerfinalizacion(aux_finalizacion)
            aux.establecertranscurrido(contador_tiempo)

            aux_retorno = aux.darhorainicial()
            fin = evaluar_hora()
            fin = fin - aux_retorno
            aux.establecerretorno(fin)

            aux.establecerservicio(fin)

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
                print(n.darfinalizacion())
                print('--------------------------')
            print("Presione la tecla 'c' para continuar")
            while keyboard.is_pressed('c') != True:
                continue


    if activador != 1:
        tiem = aux.dartiempo()
        aux.establecertranscurrido(tiem)

        hora_ret = evaluar_hora()
        hora_llegada = aux.darhorainicial()
        hora_llegada = hora_ret - hora_llegada
        aux.establecerretorno(hora_llegada)

        fin_finalizacion = evaluar_hora()
        aux_finalizacion = fin_finalizacion - inicio_principal
        aux.establecerfinalizacion(aux_finalizacion)

        servicio = evaluar_hora()
        servicio2 = aux.darhorainicial()
        servicio = servicio - servicio2
        aux.establecerservicio(servicio)

        lista_terminado.append(aux)
        
os.system("cls")
print("\n\n\n\n\n\n")
for n in lista_terminado:
    print(n.darfinal())

fin_principal = evaluar_hora()
print("Tiempo Total: ", fin_principal-inicio_principal)
        

    

    





