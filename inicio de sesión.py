#usuario_dado = "abc"
#contraseña_dada = "123"

datos_ingreso = ["abc" , "123"]


def inicio_sesion():
    for numeroIntentos in range(1, 4):
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Digite la contraseña: ")
        #if usuario == usuario_dado and contraseña == contraseña:dada:
        if usuario == datos_ingreso[0] and contraseña == datos_ingreso[1]:
            print("***** BIENVENIDO AL SISTEMA *****")
            print("  ")
            return True 
        else:
            print("** Datos de ingreso incorrectos, inténtelo de nuevo **")
            #print()
            print(f"Número de intento: {numeroIntentos}")
    print("Lo sentimos, ha alcanzado la cantidad máxima de intentos.")
    print("***** EL SISTEMA SE HA BLOQUEADO *****")
    return False

inicio_sesion()