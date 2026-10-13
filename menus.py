from principal_pi import ejecutar_proceso
from Gestion_de_personal import admin
def menu():
    res = ejecutar_proceso()
    print("---BIENVENIDO AL SISTEMA---")
    if res == "administrador":
        while True:
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
    elif res == "empleado":
        try:
            while True:
                cargo = input("Que cargo tiene?: (supervisor/empleado): ").lower()
                if cargo == "supervisor" or cargo == "empleado":
                    break
                else:
                    print("El cargo especificado no existe, intente de nuevo")
            match cargo:
                case "supervisor":
                    print("="*25)
                    print("Opciones de Supervisor")
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
                            return False

                case "empleado":
                    print("="*25)
                    print("Opciones de Empleado")
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
                            return False
        
        except ValueError:
            print("El cargo escrito no existe. Intente de nuevo")

if __name__ == "__main__":
    menu()
