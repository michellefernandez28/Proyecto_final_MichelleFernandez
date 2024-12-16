def menu():
    #empresa_seleccionada = #seleccionar_empresa()#:
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
            #agregar_ingreso(empresa_seleccionada)
            print(" PRUEBA")
        elif opcion == "2":
            #agregar_gasto(empresa_seleccionada)
            print(" PRUEBA1")
        elif opcion == "3":
            #mostrar_resumen(empresa_seleccionada)
            print(" PRUEBA2")
        elif opcion == "4":
            #historial_transacciones(empresa_seleccionada)
            print(" PRUEBA3")
        elif opcion == "5":
            #empresa_seleccionada = seleccionar_empresa()
            print(" PRUEBA4")
        elif opcion == "6":
            print("El sistema se ha cerrado. Gracias por utilizarnos, vuelva pronto")
            break
        else:
            print(" ")
            print("Opción no válida, debe digitar uno de los número anteriores.")
            print(" ")

menu()