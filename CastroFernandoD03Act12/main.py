import random
import os
import time
import keyboard
import threading
buffer = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]

def validarbuffer(buffer):
    libre = 0
    ocupado = 0
    lugares_libres = list()
    lugares_ocupados = list()
    for x in range(0,20):
        if buffer[x] == "-":
            libre = libre + 1
            lugares_libres.append(x)
        else:
            ocupado = ocupado + 1
            lugares_ocupados.append(x)
    return libre, lugares_libres, ocupado, lugares_ocupados


def listener():
    while True:
        if keyboard.read_key() == "esc":
            while True:
                os.system("cls")
                

def funcionprincipal():
    apuntador_buffer = 0
    contador_consumidor = 0
    contador_productor = 0
    random_productor = random.randint(4,10)
    random_consumidor = random.randint(4,10)

    while True:

        activador = 0
        print("_________________________________________________________________________________")
        for x in range(0,20):
            print("|",buffer[x], end=" ")

            if x == 19:
                print("|")
        print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|")

        libre = 0
        lugares_libres = list()

        ocupado = 0
        lugares_ocupados = list()




        if random_productor == contador_productor:
            random_introduce = random.randint(2,5)
            libre, lugares_libres, ocupado, lugares_ocupados = validarbuffer(buffer)
            contador_lugares_libres = 0

            if libre >= random_introduce:
            
                print("Productor Despierto: ")
                print("Introduce: ",random_introduce)
                os.system("pause")
                os.system("cls")
                if apuntador_buffer == 20:
                    apuntador_buffer_consumidor = 0
                apuntador_buffer_consumidor = apuntador_buffer 
                while contador_lugares_libres<random_introduce:
                    if apuntador_buffer == 20:
                        apuntador_buffer = 0
                    if buffer[apuntador_buffer] == "-":
                        contador_lugares_libres = contador_lugares_libres + 1
                        buffer[apuntador_buffer] = "+"
                    apuntador_buffer = apuntador_buffer + 1

                    activador = 1
                print("_________________________________________________________________________________")
                for x in range(0,20):
                    print("|",buffer[x], end=" ")

                    if x == 19:
                        print("|")
                print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|")
            random_productor = random.randint(4,10)
            contador_productor = 0

        if random_consumidor == contador_consumidor:
            random_retira = random.randint(2,5)
            libre, lugares_libres, ocupado, lugares_ocupados = validarbuffer(buffer)
            contador_retirar = 0
            print("Consumidor Despierto: ")
            print("Retira: ",random_retira)
            
            if random_retira <= ocupado:
                
                while contador_retirar < random_retira:
                    #print(apuntador_buffer_consumidor)
                    if apuntador_buffer_consumidor == 20:
                        apuntador_buffer_consumidor = 0
                    if buffer[apuntador_buffer_consumidor] == "+":
                        buffer[apuntador_buffer_consumidor] = "-"
                        contador_retirar = contador_retirar + 1
                    apuntador_buffer_consumidor = apuntador_buffer_consumidor + 1

            else:
                print("Productos insuficientes")
            os.system("pause")
            os.system("cls")
            print("_________________________________________________________________________________")
            for x in range(0,20):
                print("|",buffer[x], end=" ")

                if x == 19:
                    print("|")
            print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|")
            contador_consumidor = 0
            random_consumidor = random.randint(4,10)

        contador_productor = contador_productor + 1
        contador_consumidor = contador_consumidor + 1
        if activador!=1:
            print("Productor Dormido: ",contador_productor, random_productor)
            print("Consumidor Dormido: ",contador_consumidor, random_consumidor)
        time.sleep(1)

        os.system("cls")

t1 = threading.Thread(target = funcionprincipal, args=())
t2 = threading.Thread(target = listener, args=())

t1.start()
t2.start()

t1.join()
t2.join()



