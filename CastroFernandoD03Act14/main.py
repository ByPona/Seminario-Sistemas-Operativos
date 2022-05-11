from proceso import Proceso, Marco
import random
import time
import keyboard
import os
import numpy as np
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

    var_tamano = random.randint(5, 26)
    objeto = Proceso(contador_procesos, var_tamano,tiempo_proceso, 0, operacion_proceso, operacion_resultado,-1,-1,-1,-1,-1,-1,-1,-1,0, "Nuevo")
    lista_nuevo.append(objeto)
    contador_procesos = contador_procesos+1

def espacioslibres(memoria):
    libre = 0
    for n in memoria:
        if n.darmarcotamano() == "0/4":
            libre = libre + 1
    return libre
#############################################################
memoria = list()

marco_libre = Marco("0/4", "Libre","Libre")
for x in range(0,50):
    memoria.append(marco_libre)

marco_so = Marco("4/4", "SO","SO")
memoria[46] = marco_so
memoria[47] = marco_so
memoria[48] = marco_so
memoria[49] = marco_so

num_procesos = int(input("Dame el numero de procesos: "))
valor_quantum = int(input("Dame el valor del Quantum: "))

lista_nuevo = list()

contador_procesos = 0
lista_operandos = ["+","-","/","*"]

while contador_procesos < num_procesos:
    contador_procesos = contador_procesos+1
    tiempo_proceso = random.randint(6, 16)

    var1_proceso = str(random.randint(0, 100))
    var2_proceso = str(random.randint(1, 100))
    var3_proceso = random.randint(0, 3)
    var3_proceso = str(lista_operandos[var3_proceso])
    operacion_proceso = str(var1_proceso + var3_proceso + var2_proceso)
    operacion_resultado = eval(operacion_proceso)
    var_tamano = random.randint(5, 26)

    objeto = Proceso(contador_procesos, var_tamano,tiempo_proceso, 0, operacion_proceso, operacion_resultado,-1,-1,-1,-1,-1,-1,-1,-1,0, "Nuevo")
    lista_nuevo.append(objeto)

lista_listos = list()
lista_bloqueado = list()
lista_terminado = list()


contador_global = 0
contador_tiempo = 1
aux_bloqueado = 0
libre = 0

while True:
    activador = 0
    if len(lista_nuevo) == 0 and len(lista_listos) == 0 and len(lista_bloqueado) == 0:
        break

    while len(lista_listos) < 5 and len(lista_nuevo) > 0 and len(lista_bloqueado)==0:
        
        tamano_proceso = lista_nuevo[0].dartamano()
        libre = espacioslibres(memoria)
        id_proceso = str(lista_nuevo[0].darid())
        print("Agregando Proceso a Listo: ",id_proceso,"Tamaño: ",tamano_proceso)
        #time.sleep(1)
        os.system("pause")
        if libre>=tamano_proceso:
            
            aux = lista_nuevo.pop(0)   
            aux.establecerlista("Listo")

            aux.establecerllegada(contador_global)  

            aux.establecerespera(contador_global)
            aux.establecerhorainicial(contador_global)
            lista_listos.append(aux)
            rellenado = 0

            total = tamano_proceso//4
            residuo = tamano_proceso%4
            residuo2 = str(residuo)+"/4"

            #while total>0:
            for x in range(0,48):
                if total == 0:
                    break
                if memoria[x].darmarcotamano() == "0/4":
                    marco = Marco("4/4", str(id_proceso), "Listo")
                    memoria[x] = marco
                    total = total - 1

            if residuo > 0:
                for x in range(0,48):
                    if memoria[x].darmarcotamano() == "0/4":
                        #print("si entro")
                        #os.system("pause")
                        marco = Marco(residuo2, str(id_proceso), "Listo")
                        memoria[x] = marco
                        #os.system("pause")
                        break

                        

        else:
            break

    #for n in memoria:
        #print(n)
    #os.system("pause")
    os.system("cls")

    if len(lista_listos) > 0:
        aux = lista_listos.pop(0)
        aux.establecerlista("Ejecucion")
        obj_id = str(aux.darid())
        obj_tiempo = aux.dartiempo()
        obj_transc = aux.dartranscurrido()
        obj_oper = aux.daroperacion()
        contador_tiempo = obj_transc #Establecemos para comparar transcurrido con el contador

        restante = obj_tiempo
        aux_retorno = aux.darhorainicial()
        aux_res = contador_global - aux_retorno

        aux.establecerrespuesta(aux_res)
        aux.establecerespera(aux_res)

        quantum = 0

        for n in memoria:
            if n.darmarcoid() == obj_id:
                n.establecermarcolisto("Ejecucion")

        #mostrador_cuenta = 0
        #print("\n\nMemoria Inicio\n")
        #for n in memoria:
            #print(mostrador_cuenta,": ",n)
            #mostrador_cuenta = mostrador_cuenta + 1
        #os.system("pause")

        while contador_tiempo != obj_tiempo:
            lon_list_bloq_cont = 0
            cadena = memoria[0].darcadena()
            cadena = "| 0: " + cadena + " |"
            cadena2 = memoria[1].darcadena()
            cadena2 = " 1: "+ cadena2 + " |"
            cadena3 = memoria[2].darcadena()
            cadena3 = " 2:"+ cadena3 + " |"
            #print("=========PROCESOS EN NUEVO=============","{:>50}".format(cadena),"{:>10}".format(cadena2),"{:>10}".format(cadena3))
            print("\n\n\n\n\n=========PROCESOS EN NUEVO=============")
            cadena = memoria[3].darcadena()
            cadena = "| 3: " + cadena + " |"
            cadena2 = memoria[4].darcadena()
            cadena2 = " 4: "+ cadena2 + " |"
            cadena3 = memoria[5].darcadena()
            cadena3 = " 5:"+ cadena3 + " |"
            #print("Procesos en Nuevo: ", len(lista_nuevo),"{:>68}".format(cadena),"{:>14}".format(cadena2),"{:>20}".format(cadena3))
            print("Procesos en Nuevo: ", len(lista_nuevo))
            cadena = memoria[6].darcadena()
            cadena = "| 6: " + cadena + " |"
            cadena2 = memoria[7].darcadena()
            cadena2 = " 7: "+ cadena2 + " |"
            cadena3 = memoria[8].darcadena()
            cadena3 = " 8:"+ cadena3 + " |"
            #print("=========COLA DE LISTOS================","{:>46}".format(cadena),"{:>12}".format(cadena2),"{:>10}".format(cadena3))
            print("=========COLA DE LISTOS================")
            x = 9
            for n in lista_listos:
                #cadena = memoria[x].darcadena()
                #cadena = "| %s: " + cadena + " |" % (x)
                #cadena2 = memoria[x+1].darcadena()
                #cadena2 = " %s: "+ cadena2 + " |" % (x+1)
                #cadena3 = memoria[x+2].darcadena()
                #cadena3 = " 11:"+ cadena3 + " |" % (x+2)
                #print(n,"{:>46}".format(cadena),"{:>12}".format(cadena2),"{:>10}".format(cadena3))
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
            print("========PROCESO-EJECUCION========\nID:",obj_id,"\nOperacion: ",obj_oper,"\nEstimado: ",obj_tiempo)
            
            
            
            cont1 = contador_tiempo - obj_transc
            cont2 = restante - obj_transc
            print("|Quantum     Restante      Global|")
            print(cont1,"               ",cont2,"        ",contador_global)
            
            if len(lista_bloqueado)>0:
                print("\n==BLOQUEADO==")
                if activador_bloq == 0:
                    #tb = lista_bloqueado[lon_list_bloq_cont].dartiempoquellevabloqueado() + 1
                    #lista_bloqueado[lon_list_bloq_cont].establecertiempoquellevabloqueado(tb)
                    while len(lista_bloqueado) > lon_list_bloq_cont:
                        print("ID: ",lista_bloqueado[lon_list_bloq_cont].darid())
                        aux_bloqueado = lista_bloqueado[lon_list_bloq_cont].dartiempoquellevabloqueado() + 1
                        print("Tiempo bloqueado: ",aux_bloqueado)
                        lista_bloqueado[lon_list_bloq_cont].establecertiempoquellevabloqueado(aux_bloqueado)
    
                        #print(len(lista_bloqueado), lon_list_bloq_cont)

                    #os.system("pause")
                        if aux_bloqueado == 8:
                            lista_bloqueado[lon_list_bloq_cont].establecertiempoquellevabloqueado(0)
                            obj_bloqueado = lista_bloqueado.pop(lon_list_bloq_cont)
                            lista_listos.append(obj_bloqueado)
                            lon_list_bloq_cont = lon_list_bloq_cont - 1
                            bloq_id = str(obj_bloqueado.darid())
                            for n in memoria:
                                #print(type(n.darmarcoid()),type(bloq_id))
                                #os.system("pause")
                                if n.darmarcoid() == bloq_id:
                                    #print("Si entro")
                                    n.establecermarcolisto("Listo")
                                    #os.system("pause")
                            #print("final",len(lista_bloqueado), lon_list_bloq_cont)
                        lon_list_bloq_cont = lon_list_bloq_cont + 1
                else:
                    print("ID: ",lista_bloqueado[lon_list_bloq_cont].darid())
                    aux_bloqueado = lista_bloqueado[lon_list_bloq_cont].dartiempoquellevabloqueado() 
                    print("Tiempo bloqueado: ",aux_bloqueado)    

            if quantum==valor_quantum:
                if cont2 == 0:
                    os.system("cls")
                    pass
                else:
                    aux_quantum = aux.dartranscurrido()
                    aux.establecertranscurrido(aux_quantum + valor_quantum)
                    lista_listos.append(aux)
                    activador = 1
                    activador_bloq = 1
                    #os.system("pause")
                    for n in memoria:
                        if n.darmarcoid() == obj_id:
                            n.establecermarcolisto("Listo")
                    os.system("cls")
                    break
            if keyboard.is_pressed('i'):
                print("==============")
                print("|INTERRUPCION|")
                print("==============")
                time.sleep(0.5)

                aux.establecertranscurrido(contador_tiempo)

                aux.establecerlista("Bloqueado")

                for n in memoria:
                    if n.darmarcoid() == obj_id:
                        n.establecermarcolisto("Bloqueado")
                    

                lista_bloqueado.append(aux)
                activador = 1
                break

            if keyboard.is_pressed('e'):
                print("==============")
                print("|ERROR|")
                print("==============")
                time.sleep(0.5)
                aux.establecerresultado("ERROR")
                aux.establecerfinalizacion(contador_global)
                aux.establecertranscurrido(contador_tiempo)

                aux_retorno = aux.darhorainicial()
                fin = contador_global - aux_retorno
                aux.establecerservicio(fin)
                

                lista_terminado.append(aux)
                
                #obj_id es el id del aux
                for x in range(0,48):
                    #print(type(memoria[x].darmarcoid()), type(obj_id))
                    if memoria[x].darmarcoid() == obj_id:
                        #print("encontrado")
                        memoria[x] = marco_libre
                        #os.system("pause")
                
                #for n in memoria:
                    #print(n)
                #os.system("pause")
                os.system("cls")
                activador = 1
                break

            if keyboard.is_pressed('p'):
                print("==============")
                print("|PAUSA|")
                print("==============")
                x = 0
                print("\n")
                while x<50:
                    var1 = memoria[x].darcadena()
                    var2 = memoria[x+1].darcadena()
                    print(x, " | {:<20} |".format(var1),x+1," | {:>18} |".format(var2))
                    x = x+2
                print("Presione la tecla 'c' para continuar")
                while keyboard.is_pressed('c') != True:
                    continue

            if keyboard.is_pressed('n'):
                print("==============")
                print("|NUEVO PROCESO CREADO|")
                print("==============")
                agregarnuevoproceso(contador_procesos)
                contador_procesos = contador_procesos+1
                time.sleep(0.5)  

            if keyboard.is_pressed('t'):
                print("\n\n\n\n\n====================")
                print('TABLA DE PROCESOS')
                print("====================")
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
            if keyboard.is_pressed('a'):
                os.system("cls")
                print("==============")
                print("|TABLA DE PAGINAS|")
                print("==============")
                x = 0
                while x<50:
                    var1 = memoria[x].darcadena()
                    var2 = memoria[x+1].darcadena()
                    print(x, " | {:<20} |".format(var1),x+1," | {:>18} |".format(var2))
                    x = x+2
                print("Presione la tecla 'c' para continuar\n\n\n\n\n\n\n")
                while keyboard.is_pressed('c') != True:
                    continue

            x = 0
            print("\n")
            while x<50:
                var1 = memoria[x].darcadena()
                var2 = memoria[x+1].darcadena()
                print(x, " | {:<20} |".format(var1),x+1," | {:>18} |".format(var2))
                x = x+2
            
            
            

            time.sleep(1)
            contador_tiempo = contador_tiempo + 1
            contador_global = contador_global + 1
            quantum = quantum + 1
            restante = restante - 1
            activador_bloq = 0
            #os.system("pause")
            print('\n' * 150)

        if activador != 1:
            tiem = aux.dartiempo()
            aux.establecertranscurrido(tiem)

            hora_ret = contador_global
            hora_llegada = aux.darhorainicial()
            hora_llegada = hora_ret - hora_llegada
            aux.establecerretorno(hora_llegada)

            aux_finalizacion = contador_global
            aux.establecerfinalizacion(aux_finalizacion)

            servicio = contador_global
            servicio2 = aux.darhorainicial()
            servicio = servicio - servicio2
            aux.establecerservicio(servicio)

            lista_terminado.append(aux)
            for x in range(0,48):
                    if memoria[x].darmarcoid() == obj_id:
                        memoria[x] = marco_libre
    #mostrador_cuenta = 0
    #print("\n\nMemoria final\n")
    #for n in memoria:
        #print(mostrador_cuenta," ",n)
        #mostrador_cuenta = mostrador_cuenta + 1
    #os.system("pause")

os.system("cls")
print("\n\n\n\n\n\n")
for n in lista_terminado:
    print(n.darfinal())          
print("Tiempo Total: ", contador_global)  