import os
os.system("cls")


datos_ingreso = ["abc", "123"] 
empresas = {
    "Mollys Su": [],
    "Maramasas Derla": [],
    "Dollys Chick": [],
}

transacciones = {}  # inicialmente era tipo lista, pero la informacion no se guardaba en cada empresa, o sea, la arrastraba a la otra

#########################################################################################################################################

def inicio_sesion():
    for numeroIntentos in range(1, 4):
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Digite la contraseña: ")
        if usuario == datos_ingreso[0] and contraseña == datos_ingreso[1]:
            print("***** BIENVENIDO AL SISTEMA *****")
            print("  ")
            return True
        else:
            print("** Datos de ingreso incorrectos, inténtelo de nuevo **")
            print(f"Número de intento: {numeroIntentos}")
    print("Lo sentimos, ha alcanzado la cantidad máxima de intentos.")
    print("***** EL SISTEMA SE HA BLOQUEADO *****")
    return False

#########################################################################################################################################

def seleccionar_empresa():
    print("A continuación se muestran las empresas disponibles:")
    print("  ")
    for i, empresa in enumerate(empresas.keys(), 1):
        print(f"{i}. {empresa}")
    while True:
        try:
            eleccion = int(input("Digite el número de la empresa que desea seleccionar: "))
            if 1 <= eleccion <= len(empresas):
                empresa_elegida = list(empresas.keys())[eleccion - 1]
                print(f"Empresa: {empresa_elegida}")
                return empresa_elegida
            else:
                print("Opción inválida, intente de nuevo.")
        except ValueError:
            print("Entrada no válida, por favor ingrese un número.")

#########################################################################################################################################

def agregar_ingreso(empresa):
    fecha = input("Digite la fecha del ingreso (día/mes/año): ")
    nume_factura = int(input("Escriba el número de factura: "))
    monto = float(input("Monto del ingreso: "))
    descripcion = input("Descripción del ingreso: ")
    if empresa not in transacciones:
        transacciones[empresa] = []  # Asegúrate de inicializar las transacciones para la empresa seleccionada.
    transacciones[empresa].append({"Tipo": "Ingreso", "Fecha": fecha, "Factura": nume_factura, "Descripción": descripcion, "Monto": monto})

#########################################################################################################################################

def agregar_gasto(empresa):
    fecha = input("Digite la fecha del gasto (día/mes/año): ")
    nume_factura = int(input("Escriba el número de factura: "))
    monto = float(input("Monto del gasto: "))
    descripcion = input("Descripción del gasto: ")
    if empresa not in transacciones:
        transacciones[empresa] = []  # Asegúrate de inicializar las transacciones para la empresa seleccionada.
    transacciones[empresa].append({"Tipo": "Gasto", "Fecha": fecha, "Factura": nume_factura, "Descripción": descripcion, "Monto": monto})

#########################################################################################################################################

def mostrar_resumen(empresa):
    if empresa not in transacciones:
        print("No hay transacciones para mostrar.")
        return
    total_ingresos = sum(t["Monto"] for t in transacciones[empresa] if t["Tipo"] == "Ingreso")
    total_gastos = sum(t["Monto"] for t in transacciones[empresa] if t["Tipo"] == "Gasto")
    print("-- Resumen Financiero ---")
    print(f"Total Ingresos: ₡{total_ingresos}")
    print(f"Total Gastos: ₡{total_gastos}")
    print(f"Balance: ₡{total_ingresos - total_gastos}\n")

#########################################################################################################################################

def historial_transacciones(empresa):
    if empresa not in transacciones:
        print("No hay transacciones para mostrar.")
        return
    print("  ")
    print("\n--- Historial de Transacciones ---")
    for t in transacciones[empresa]: #revisar que las mayusculas esten bien
        print(f"{t['Tipo'].capitalize()} - Fecha: {t['Fecha']} - Factura: {t['Factura']} - Monto: ₡{t['Monto']} - Descripción: {t['Descripción']}")
    print(" ")

#########################################################################################################################################

def menu():
    empresa_seleccionada = seleccionar_empresa()
    while True:
        print("**** MENÚ PRINCIPAL ****")
        print(" ")
        print("1. Agregar Ingreso")
        print("2. Agregar Gasto")
        print("3. Mostrar Resumen Financiero")
        print("4. Historial de Transacciones")
        print("5. Elegir otra empresa")
        print("6. Salir")
        print(" ")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_ingreso(empresa_seleccionada)
        elif opcion == "2":
            agregar_gasto(empresa_seleccionada)
        elif opcion == "3":
            mostrar_resumen(empresa_seleccionada)
        elif opcion == "4":
            historial_transacciones(empresa_seleccionada)
        elif opcion == "5":
            empresa_seleccionada = seleccionar_empresa()
        elif opcion == "6":
            print("El sistema se ha cerrado. Gracias por utilizarnos, vuelva pronto")
            break
        else:
            print(" ")
            print("Opción no válida, debe digitar uno de los número anteriores.")
            print(" ")

#########################################################################################################################################

if inicio_sesion():
    menu()
