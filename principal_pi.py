import Funciones_Proyecto as fp
def ejecutar_proceso():
    print("="*20)
    print("INICIO DE SESIÓN")
    print("="*20)
    try:
        while True:
            res = fp.letras("Está tratando de iniciar sesión como Empleado o como Administrador?: ").strip().lower()
            if res:
                if res == "empleado":
                    fp.validar_empleado()
                elif res == "administrador":
                    fp.validar_admin()
    except Exception as e:
        print(f"Error. {e}")
if __name__=="__main__":
    ejecutar_proceso()