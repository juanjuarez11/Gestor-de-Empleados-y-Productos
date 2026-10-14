from principal_pi import ejecutar_proceso
from Gestion_de_personal import admin
def menu():
    while True:
        res = ejecutar_proceso()
        if res == "administrador":
            while True:
                try:
                    print("---BIENVENIDO AL SISTEMA---")
                    print("Opciones de Administrador: ")
                    print("1. Busqueda y Actualización de Empleados")
                    print("2. Dar de Alta Empleados")
                    print("3. Dar de Baja Empleados")
                    print("4. Salir del Sistema")
                    opcion = int(input("Escoja una opción (1-4): "))
                    match opcion:
                        case 1:
                            admin.Busqueda_actualizacion()
                        case 2:
                            admin.Alta_integ()
                        case 3:
                            admin.Baja_empleado()
                        case 4:
                            print("Saliendo del sistema...")
                            break
                except Exception as e:
                    print(f"Error: {e}")
        elif res == "empleado":
            while True:
                try:
                    print("---BIENVENIDO AL SISTEMA---")
                    print("Opciones de Empleado")
                    print("1. Supervisor")
                    print("2. Cajero")
                    print("3. Vendedor")
                    print("4. Salir")
                    cargo = int(input("Elija una opción (1-4): "))
                    match cargo:
                        case 1:
                            while True:
                                try:
                                    print("="*25)
                                    print("Opciones de Supervisor:")
                                    print("-"*25)
                                    print("1. ")
                                    print("2. ")
                                    print("3. Salir.")
                                    opcion = int(input("Ingrese una opción (1-3): "))
                                    match opcion:
                                        case 1:
                                            pass
                                        case 2:
                                            pass
                                        case 3:
                                            print("Saliendo del sistema...")
                                            break
                                        case _:
                                            print("Opción no válida.")
                                except ValueError:
                                    print("Opción no valida.")
                                except Exception as e:
                                    print(f"Error: {e}")

                        case 2:
                            while True:
                                try:
                                    print("="*25)
                                    print("Opciones de Cajero:")
                                    print("-"*25)
                                    print("1. ")
                                    print("2. ")
                                    print("3. Salir.")
                                    opcion = int(input("Ingrese una opción (1-3): "))
                                    match opcion:
                                        case 1:
                                            pass
                                        case 2:
                                            pass
                                        case 3:
                                            print("Saliendo del sistema...")
                                            break
                                        case _:
                                            print("Opción no válida.")
                                except ValueError:
                                    print("Opción no válida")
                                except Exception as e:
                                    print(f"Error: {e}")

                        case 3:
                            while True:
                                try:
                                    print("="*25)
                                    print("Opciones de Vendedor:")
                                    print("-"*25)
                                    print("1. ")
                                    print("2. ")
                                    print("3. Salir.")
                                    opcion = int(input("Ingrese una opción (1-3): "))
                                    match opcion:
                                        case 1:
                                            pass
                                        case 2:
                                            pass
                                        case 3:
                                            print("Saliendo del sistema...")
                                            break
                                        case _:
                                            print("Opción no válida.")
                                except ValueError:
                                    print("Opción no válida.")
                                except Exception as e:
                                    print(f"Error: {e}")
                        case 4:
                            print("Saliendo..")
                            break     
                                
                except ValueError:
                    print("Opción Inválida")
        elif res == "cerrar":
            break

if __name__ == "__main__":
    menu()
