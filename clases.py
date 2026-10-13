from abc import ABC,abstractmethod
import openpyxl
from datetime import datetime as dt, timedelta

class Producto(ABC):
    def __init__(self, Categoria, Marca, imei, id_producto,  stock):
        self.Cat = Categoria
        self.Ma = Marca
        self.imei = imei
        self.id_producto = id_producto
        self.stock = stock
        
    @abstractmethod
    def precentacion(self):
        pass
    
class Garantia:
    def __init__(self, f_venta, ticket, n_factura):
        self.f_venta = f_venta
        self.ticket = ticket
        self.n_factura = n_factura
        pass

class Celular(Producto):
    def __init__(self, Categoria, Marca, imei, id_producto,  stock, procesador, ram, c_almacenamiento, modelo, precio):
        super().__init__(Categoria, Marca, imei, id_producto,  stock)
        self.procesador = procesador
        self.ram = ram
        self.c_alm = c_almacenamiento
        self.modelo = modelo
        self.precio = precio
        
    def precentacion(self):
        print(f'Marca: {self.Ma}\nModelo: {self.modelo} \nProcesador: {self.procesador}\nRAM: {self.ram} GB\nAlmacenmiento: {self.c_alm}\nPrecio: ${self.precio}')
        print()
        
        
class Laptop(Producto):
    def __init__(self, Categoria, Marca, imei, id_producto, stock, procesador, ram, t_grafica, modelo, precio, t_pantalla, disco):
        super().__init__(Categoria, Marca, imei, id_producto, stock )
        self.procesador = procesador
        self.ram = ram
        self.t_grafica = t_grafica
        self.modelo = modelo
        self.precio = precio
        self.t_pantalla = t_pantalla
        self.disco = disco
        
    def precentacion(self):
        print(f'''Marca: {self.Ma}\nModelo: {self.modelo} \nProcesador: {self.procesador}\nTarjeta Gradica: {self.t_grafica}\nRAM: {self.ram} GB\nDisco: {self.disco}\nTamaño de pantalla: {self.t_pantalla}"\nPrecio: ${self.precio}''')
        print()
        

class Historial:
    def __init__(self, usuario, accion):
        self.usuario = usuario
        self.accion = accion
        self.fecha = dt.today()

    def __str__(self):
        fecha_formateada = self.fecha.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{fecha_formateada}] {self.usuario}: {self.accion}"


# 2. La clase Pila (Estructura dinámica)
class PilaHistorial:
    def _init_(self):
        self.__items = []  # Lista interna privada que actúa como pila

    def push(self, historial_objeto):
        """Agrega un nuevo registro al tope de la pila."""
        self.__items.append(historial_objeto)

    def pop(self):
        """Elimina y devuelve el último registro realizado (el del tope)."""
        if self.es_vacia():
            return None
        return self.__items.pop()

    def peek(self):
        """Muestra cuál fue la última acción sin borrarla."""
        if self.es_vacia():
            return None
        return self.__items[-1]

    def es_vacia(self):
        """Verifica si el historial no tiene registros."""
        return len(self.__items) == 0

    def mostrar_historial(self):
        """Muestra el historial desde la acción más reciente a la más antigua."""
        if self.es_vacia():
            print("El historial está vacío.")
            return
        
        # Invertimos la lectura para mostrar el tope primero
        print("\n=== HISTORIAL (De más reciente a más antiguo) ===")
        for registro in reversed(self.__items):
            print(registro)

celular_1=Celular('Moviles','Infinix', 24, 12, 'Mediateck', 12, '256 GB', 'GT 20 Pro',400)
celular_2=Celular('Moviles','Samsung', 26, 12, 'Snapdragon', 8, '536 GB', 'S23 Ultra', 550)
laptop1 = Laptop('PC Portatil', 'Dell', 25, 3, 'i7-7600U', 16, 'Intel(R) HD Graphics 620', 'Latitude 7480', 1000, 14, 'M.2 - 256 GB')
laptop1.precentacion()
celular_1.precentacion()
celular_2.precentacion()
