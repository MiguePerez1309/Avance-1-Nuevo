
#declaracion de variables
Usuario = ('Miguel','Diego','Alex')
Contraseña = ('1234')
 
#declaracion de funciones
def login(usuario,passw):
    if usuario in Usuario:
        if passw in Contraseña:
            return 1

        else:
            print("\n\tEsta no es la contraseña...\n")
    else:
        return 2
 #inicializacion de procesos
usuario=input('Usuario: ')
passw = input('Contraseña: ')
 
if login(usuario,passw)==1:
    print('Bienvenido ',usuario)
else: 

 print('ERROR! El usuario no está registrado.')