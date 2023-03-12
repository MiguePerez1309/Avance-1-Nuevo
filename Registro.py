print('Bienvenido al programa de gestion de inventarios')
cantidad = []
productos = []
precio = []
descrip = []

while True:
    print("""
    (1) Anadir prodcutos
    (2) Buscar prodcutos
    (3) Modificar prodcutos
    (4) Ver prodcutos
    (5) Salir
    """)

    respuesta = int(input('Ingrese su opcion: '))
    if respuesta == 1:
        ac = int(input('Ingrese la cantidad de su produco: '))
        ap = input('Ingrese el nombre de su producto')
        apre = int(input('Ingrese el precio de su producto'))
        desc = input("Ingrese una breve descripción del producto")

        cantidad.append(ac)
        productos.append(ap)
        precio.append(apre)
        descrip.append(desc)

    elif respuesta == 2:
        buscador = input('Ingrese el nombre del producto que quiere buscar: ')
        posicion = productos.index(buscador)
        print('La cantidad del producto es: ', cantidad[posicion])
        print('El nombre del prodcuto es: ', productos[posicion])
        print('El precio del prodcuto es: ', precio[posicion])
        print('La descripción del prodcuto es: ', descrip[posicion])
    
    elif respuesta == 3:
        buscador = input('Ingrese el nombre del producto que quiere modificar: ')
        posicion = productos.index(buscador)
        ac = int(input('Ingrese la cantidad de su produco: '))
        ap = input('Ingrese el nombre de su producto')
        apre = int(input('Ingrese el precio de su producto'))
        cantidad[posicion] = ac
        productos[posicion] = ap
        precio[posicion] = apre
    
    elif respuesta == 4:
        print('La cantidad es: ', cantidad)
        print('El nombre es: ', productos)
        print('El precio es: ', precio)
    else:
        break