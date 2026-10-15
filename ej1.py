tienda = {
    "accion": ["mono enojado I", "Valorant"],
    "ciencia ficcion": ["aprobar fisica"],
    "terror": ["la maldición del tomi leyes"],
}
biblioteca = {}

while True:
    print("\netec station\n1. tienda\n2. jugar\n3. salir")
    op = input("opcion: ")

    if op == "1":
        while True:
            print("\n1. comprar\n2. ingresar juego\n3. volver")
            op2 = input("opcion: ")

            if op2 == "1":
                gen = input("genero: ")
                if gen in tienda:
                    for i in range(len(tienda[gen])):
                        print(i, tienda[gen][i])
                    n = int(input("numero: "))
                    if 0 <= n < len(tienda[gen]):
                        biblioteca[len(biblioteca) + 1] = tienda[gen][n]
                else:
                    print("el genero no existe")

            elif op2 == "2":
                gen = input("genero: ")
                juego = input("juego: ")
                if gen not in tienda:
                    tienda[gen] = []
                tienda[gen].append(juego)

            elif op2 == "3":
                break

    elif op == "2":
        for i in biblioteca:
            print(i, biblioteca[i])
        if len(biblioteca) > 0:
            n = int(input("número del juego: "))
            if n in biblioteca:
                input("jugando a " + biblioteca[n] + "... enter para volver")

    elif op == "3":
        break
