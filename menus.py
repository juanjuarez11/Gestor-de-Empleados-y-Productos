from principal_pi import ejecutar_proceso
from Gestion_de_personal import admin
def menu():
    res = ejecutar_proceso()
    print("---BIENVENIDO AL SISTEMA---")
    if res == "administrador":
        while True:
            try:
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
                cargo = input("Que cargo tiene?(supervisor/cajero/vendedor): ").lower()
                match cargo:
                    case "supervisor":
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

                    case "cajero":
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

                    case "vendedor":
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
                            
        
            except ValueError:
                print("El cargo escrito no existe. Intente de nuevo")

if __name__ == "__main__":
    menu()
