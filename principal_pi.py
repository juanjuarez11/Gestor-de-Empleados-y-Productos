import Funciones_Proyecto as fp

def ejecutar_proceso():
    print("=" * 20)
    print("INICIO DE SESIÓN")
    print("=" * 20)

    try:
        while True:
            print("1. Iniciar como Administrador.")
            print("2. Iniciar como Empleado.")
            print("3. Cerrar sistema.")
            res = input("Ingrese una opción (administrador/empleado/cerrar): ").strip().lower()
            
            if not res:
                print("Error. Debe escoger una respuesta.\n")
                continue
                
            if res == "empleado":
                if fp.validar_empleado():
                    print("Sesión de empleado iniciada correctamente.")
                    break 
                else:
                    print("No se pudo iniciar sesión como empleado. Intente nuevamente.\n")
                    
            elif res == "administrador":
                if fp.validar_admin():
                    print("Sesión de administrador iniciada correctamente.")
                    break 
                else:
                    print("No se pudo iniciar sesión como administrador. Intente nuevamente.\n")
                    
            elif res == "cerrar":
                print("Cerrando sistema...")
                break

            else:
                print("Opción no válida. Por favor escriba 'empleado' o 'administrador'.\n")

        return res
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar_proceso()