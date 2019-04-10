totito = False
while totito == False:
    print("BIENVENIDO AL JUEGO DE TOTITO! ")
    print(" instrucciones: seleciones un numero del 1 al 9 para seleccionar ")
    print("desea jugar contra un bot(1) o desea jugar con otro jugador(2)? ")
    seleccionar = int(input())
    if seleccionar == 1:

        jugadorr = input("ingrese nombre del jugador 1: ")
        print("desea jugar version Normal(1) o version Misere(2)?")
        opcion = int(input())

        if opcion == 1:

            import os
            import time
            import random

            tablero = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

            def tablero1():
                print("   |   |   ")
                print(""+tablero[1]+"  | "+tablero[2]+" | "+tablero[3]+" ")
                print("   |   |   ")
                print("---|---|---")
                print("   |   |   ")
                print(""+tablero[4]+"  | "+tablero[5]+" | "+tablero[6]+" ")
                print("   |   |   ")
                print("---|---|---")
                print("   |   |   ")
                print(""+tablero[7]+"  | "+tablero[8]+" | "+tablero[9]+" ")
                print("   |   |   ")
                print("___________________")    

            while True:
                os.system("cls")
                tablero1()

                while True:
                    print(jugadorr)
                    seleccion = input("seleccione en que casilla colocar X: ")
                    seleccion = int(seleccion)

                    if tablero[seleccion] == " ":
                        tablero[seleccion] = "X"
                        break
                    else:
                        print("casilla ya esta ocupada,intente de nuevo: ")
                        time.sleep(3)
                    
                if (tablero[1] == "X" and tablero[2] == "X" and tablero[3] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "GANA!")
                    break
                elif (tablero[4] == "X" and tablero[5] == "X" and tablero[6] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "GANA!")
                    break
                elif (tablero[7] == "X" and tablero[8] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "GANA!")
                    break
                elif (tablero[1] == "X" and tablero[4] == "X" and tablero[7] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "GANA!")
                    break
                elif (tablero[2] == "X" and tablero[5] == "X" and tablero[8] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "GANA!")
                    break
                elif (tablero[3] == "X" and tablero[6] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "GANA!")
                    break
                elif (tablero[1] == "X" and tablero[5] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "GANA!")
                    break
                elif (tablero[7] == "X" and tablero[5] == "X" and tablero[3] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "GANA!")
                    break

                os.system("cls")
                tablero1()

                empate = True
                for index in range(1, 10):
                    if tablero[index] == " ":
                        empate = False
                        break

                if empate == True:
                    tablero1()
                    print("EMPATE! ")
                    break

                #bot-----------------------------------------------------------------------
            
                while True:
                    
                    bots = ["RoboCop", "Terminator", "OptimusPrime", "R2D2", "Wall-E"]
                    secure_random = random.SystemRandom()
                    jugador2 = secure_random.choice(bots)

                    print("espere el turno del bot: ",jugador2,"...")
                    time.sleep(2)

                    seleccion = random.randint(1,9)
                    seleccion = int(seleccion)
                
                    if tablero[seleccion] == " ":
                        tablero[seleccion] = "O"
                        break
                    else:
                        print("casilla ya esta ocupada,",jugador2, "intente de nuevo: ")
                        time.sleep(3)
                    
                if (tablero[1] == "O" and tablero[2] == "O" and tablero[3] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "GANA!")
                    break
                elif (tablero[4] == "O" and tablero[5] == "O" and tablero[6] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "GANA!")
                    break
                elif (tablero[7] == "O" and tablero[8] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "GANA!")
                    break
                elif (tablero[1] == "O" and tablero[4] == "O" and tablero[7] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "GANA!")
                    break
                elif (tablero[2] == "O" and tablero[5] == "O" and tablero[8] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "GANA!")
                    break
                elif (tablero[3] == "O" and tablero[6] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "GANA!")
                    break
                elif (tablero[1] == "O" and tablero[5] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "GANA!")
                    break
                elif (tablero[7] == "O" and tablero[5] == "O" and tablero[3] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "GANA!")
                    break

                empate = True
                for index in range(1, 10):
                    if tablero[index] == " ":
                        empate = False
                        break
                    
                if empate == True:
                    tablero1()
                    print("EMPATE! ")
                    break
        
        if opcion == 2:

            import os
            import time
            import random

            tablero = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

            def tablero1():
                print("   |   |   ")
                print(""+tablero[1]+"  | "+tablero[2]+" | "+tablero[3]+" ")
                print("   |   |   ")
                print("---|---|---")
                print("   |   |   ")
                print(""+tablero[4]+"  | "+tablero[5]+" | "+tablero[6]+" ")
                print("   |   |   ")
                print("---|---|---")
                print("   |   |   ")
                print(""+tablero[7]+"  | "+tablero[8]+" | "+tablero[9]+" ")
                print("   |   |   ")
                print("modo MISERE... quien llene 3 casillas en linea PIERDE!... ")   
                print("___________________")

            while True:
                os.system("cls")
                tablero1()

                while True:

                    print(jugadorr)
                    seleccion = input("seleccione en que casilla colocar X: ")
                    seleccion = int(seleccion)

                    if tablero[seleccion] == " ":
                        tablero[seleccion] = "X"
                        break
                    else:
                        print("casilla ya esta ocupada,intente de nuevo: ")
                        time.sleep(3)
                    
                if (tablero[1] == "X" and tablero[2] == "X" and tablero[3] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "PIERDE!")
                    break
                elif (tablero[4] == "X" and tablero[5] == "X" and tablero[6] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "PIERDE!")
                    break
                elif (tablero[7] == "X" and tablero[8] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "PIERDE!")
                    break
                elif (tablero[1] == "X" and tablero[4] == "X" and tablero[7] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "PIERDE!")
                    break
                elif (tablero[2] == "X" and tablero[5] == "X" and tablero[8] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "PIERDE!")
                    break
                elif (tablero[3] == "X" and tablero[6] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "PIERDE!")
                    break
                elif (tablero[1] == "X" and tablero[5] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "PIERDE!")
                    break
                elif (tablero[7] == "X" and tablero[5] == "X" and tablero[3] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugadorr, "PIERDE!")
                    break

                os.system("cls")
                tablero1()

                empate = True
                for index in range(1, 10):
                    if tablero[index] == " ":
                        empate = False
                        break

                if empate == True:
                    tablero1()
                    print("EMPATE! ")
                    break

                #bot-----------------------------------------------------------------------
            
                while True:
                    
                    bots = ["RoboCop", "Terminator", "OptimusPrime", "R2D2", "Wall-E"]
                    secure_random = random.SystemRandom()
                    jugador2 = secure_random.choice(bots)

                    print("espere el turno del bot: ",jugador2,"...")
                    time.sleep(2)

                    seleccion = random.randint(1,9)
                    seleccion = int(seleccion)
                
                    if tablero[seleccion] == " ":
                        tablero[seleccion] = "O"
                        break
                    else:
                        print("casilla ya esta ocupada,",jugador2, "intente de nuevo: ")
                        time.sleep(3)
                    
                if (tablero[1] == "O" and tablero[2] == "O" and tablero[3] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "PIERDE!")
                    break
                elif (tablero[4] == "O" and tablero[5] == "O" and tablero[6] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "PIERDE!")
                    break
                elif (tablero[7] == "O" and tablero[8] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "PIERDE!")
                    break
                elif (tablero[1] == "O" and tablero[4] == "O" and tablero[7] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "PIERDE!")
                    break
                elif (tablero[2] == "O" and tablero[5] == "O" and tablero[8] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "PIERDE!")
                    break
                elif (tablero[3] == "O" and tablero[6] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "PIERDE!")
                    break
                elif (tablero[1] == "O" and tablero[5] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "PIERDE!")
                    break
                elif (tablero[7] == "O" and tablero[5] == "O" and tablero[3] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador2, "PIERDE!")
                    break

                empate = True
                for index in range(1, 10):
                    if tablero[index] == " ":
                        empate = False
                        break
                    
                if empate == True:
                    tablero1()
                    print("EMPATE! ")
                    break
    
    if seleccionar == 2:

        jugador_1 = input("ingrese nombre jugador 1: ")
        jugador_2 = input("ingrese nombre jugador 2: ")
        print("desea jugar version Normal(1) o version Misere(2)?")
        opcion = int(input())

        if opcion == 1:

            import os
            import time
            import random

            tablero = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

            def tablero1():
                print("   |   |   ")
                print(""+tablero[1]+"  | "+tablero[2]+" | "+tablero[3]+" ")
                print("   |   |   ")
                print("---|---|---")
                print("   |   |   ")
                print(""+tablero[4]+"  | "+tablero[5]+" | "+tablero[6]+" ")
                print("   |   |   ")
                print("---|---|---")
                print("   |   |   ")
                print(""+tablero[7]+"  | "+tablero[8]+" | "+tablero[9]+" ")
                print("   |   |   ")
                print("___________________")    

            while True:
                os.system("cls")
                tablero1()

                while True:
                    
                    print(jugador_1)
                    seleccion = input("seleccione en que casilla colocar X: ")
                    seleccion = int(seleccion)

                    if tablero[seleccion] == " ":
                        tablero[seleccion] = "X"
                        break
                    else:
                        print("casilla ya esta ocupada,intente de nuevo: ")
                        time.sleep(3)
                    
                if (tablero[1] == "X" and tablero[2] == "X" and tablero[3] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "GANA!")
                    break
                elif (tablero[4] == "X" and tablero[5] == "X" and tablero[6] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "GANA!")
                    break
                elif (tablero[7] == "X" and tablero[8] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "GANA!")
                    break
                elif (tablero[1] == "X" and tablero[4] == "X" and tablero[7] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "GANA!")
                    break
                elif (tablero[2] == "X" and tablero[5] == "X" and tablero[8] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "GANA!")
                    break
                elif (tablero[3] == "X" and tablero[6] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "GANA!")
                    break
                elif (tablero[1] == "X" and tablero[5] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "GANA!")
                    break
                elif (tablero[7] == "X" and tablero[5] == "X" and tablero[3] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "GANA!")
                    break

                os.system("cls")
                tablero1()

                empate = True
                for index in range(1, 10):
                    if tablero[index] == " ":
                        empate = False
                        break

                if empate == True:
                    tablero1()
                    print("EMPATE! ")
                    break

                    #JUGADOR
            
                while True:

                    print(jugador_2)
                    seleccion = input("seleccione en que casilla colocar O: ")
                    seleccion = int(seleccion)
                
                    if tablero[seleccion] == " ":
                        tablero[seleccion] = "O"
                        break
                    else:
                        print("casilla ya esta ocupada,intente de nuevo: ")
                        time.sleep(3)
                    
                if (tablero[1] == "O" and tablero[2] == "O" and tablero[3] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "GANA!")
                    break
                elif (tablero[4] == "O" and tablero[5] == "O" and tablero[6] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "GANA!")
                    break
                elif (tablero[7] == "O" and tablero[8] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "GANA!")
                    break
                elif (tablero[1] == "O" and tablero[4] == "O" and tablero[7] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "GANA!")
                    break
                elif (tablero[2] == "O" and tablero[5] == "O" and tablero[8] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "GANA!")
                    break
                elif (tablero[3] == "O" and tablero[6] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "GANA!")
                    break
                elif (tablero[1] == "O" and tablero[5] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "GANA!")
                    break
                elif (tablero[7] == "O" and tablero[5] == "O" and tablero[3] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "GANA!")
                    break

                empate = True
                for index in range(1, 10):
                    if tablero[index] == " ":
                        empate = False
                        break
                    
                if empate == True:
                    tablero1()
                    print("EMPATE! ")
                    break
        
        if opcion == 2:

            import os
            import time
            import random

            tablero = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

            def tablero1():
                print("   |   |   ")
                print(""+tablero[1]+"  | "+tablero[2]+" | "+tablero[3]+" ")
                print("   |   |   ")
                print("---|---|---")
                print("   |   |   ")
                print(""+tablero[4]+"  | "+tablero[5]+" | "+tablero[6]+" ")
                print("   |   |   ")
                print("---|---|---")
                print("   |   |   ")
                print(""+tablero[7]+"  | "+tablero[8]+" | "+tablero[9]+" ")
                print("   |   |   ")
                print("modo MISERE... quien llene 3 casillas en linea PIERDE!... ")
                print("___________________")    

            while True:
                os.system("cls")
                tablero1()

                while True:

                    print(jugador_1)
                    seleccion = input("seleccione en que casilla colocar X: ")
                    seleccion = int(seleccion)

                    if tablero[seleccion] == " ":
                        tablero[seleccion] = "X"
                        break
                    else:
                        print("casilla ya esta ocupada,intente de nuevo: ")
                        time.sleep(3)
                    
                if (tablero[1] == "X" and tablero[2] == "X" and tablero[3] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "PIERDE!")
                    break
                elif (tablero[4] == "X" and tablero[5] == "X" and tablero[6] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "PIERDE!")
                    break
                elif (tablero[7] == "X" and tablero[8] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "PIERDE!")
                    break
                elif (tablero[1] == "X" and tablero[4] == "X" and tablero[7] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "PIERDE!")
                    break
                elif (tablero[2] == "X" and tablero[5] == "X" and tablero[8] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "PIERDE!")
                    break
                elif (tablero[3] == "X" and tablero[6] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "PIERDE!")
                    break
                elif (tablero[1] == "X" and tablero[5] == "X" and tablero[9] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "PIERDE!")
                    break
                elif (tablero[7] == "X" and tablero[5] == "X" and tablero[3] == "X"):
                    os.system("cls")
                    tablero1()
                    print(jugador_1, "PIERDE!")
                    break

                os.system("cls")
                tablero1()

                empate = True
                for index in range(1, 10):
                    if tablero[index] == " ":
                        empate = False
                        break

                if empate == True:
                    tablero1()
                    print("EMPATE! ")
                    break

                    #JUGADOR
            
                while True:

                    print(jugador_2)
                    seleccion = input("seleccione en que casilla colocar O: ")
                    seleccion = int(seleccion)
                
                    if tablero[seleccion] == " ":
                        tablero[seleccion] = "O"
                        break
                    else:
                        print("casilla ya esta ocupada,intente de nuevo: ")
                        time.sleep(3)
                    
                if (tablero[1] == "O" and tablero[2] == "O" and tablero[3] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "PIERDE!")
                    break
                elif (tablero[4] == "O" and tablero[5] == "O" and tablero[6] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "PIERDE!")
                    break
                elif (tablero[7] == "O" and tablero[8] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "PIERDE!")
                    break
                elif (tablero[1] == "O" and tablero[4] == "O" and tablero[7] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "PIERDE!")
                    break
                elif (tablero[2] == "O" and tablero[5] == "O" and tablero[8] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "PIERDE!")
                    break
                elif (tablero[3] == "O" and tablero[6] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "PIERDE!")
                    break
                elif (tablero[1] == "O" and tablero[5] == "O" and tablero[9] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "PIERDE!")
                    break
                elif (tablero[7] == "O" and tablero[5] == "O" and tablero[3] == "O"):
                    os.system("cls")
                    tablero1()
                    print(jugador_2, "PIERDE!")
                    break

                empate = True
                for index in range(1, 10):
                    if tablero[index] == " ":
                        empate = False
                        break
                    
                if empate == True:
                    tablero1()
                    print("EMPATE! ")
                    break