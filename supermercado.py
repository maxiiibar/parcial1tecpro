# class Producto:
#     def __init__(self, nombre: str, categoria: str):
#         self.nombre = nombre
#         self.categoria = categoria
# class Carrito:
#     def __init__(self, productos: list):
#         self.productos = productos
# def calcular_descuento(productos: list):
#     for producto in productos:
#         if producto.categoria == 'alimentos':
#             print(f"Descuento del 10% en {producto.nombre}")
#         elif producto.categoria == 'limpieza':
#             print(f"Descuento del 5% en {producto.nombre}")
# # Añadir más condiciones para nuevos tipos de productos y descuentos
# productos = [
# Producto('manzanas', 'alimentos'),
# Producto('jabón', 'limpieza')
# ]
# carrito = Carrito(productos)
# calcular_descuento(carrito.productos)

# Se viola el Princio Abierto/Cerrado, ya que para agregar más descuentos debemos modificar la función
# "calcular_decuento", y lo ideal es que esta no deba ser modificada cada vez que se agrega
# un nuevo descuento.

# Mi solución:


class Producto:
    def __init__(self, nombre: str, categoria: str, descuento=None):
        self.nombre = nombre
        self.categoria = categoria
        self.descuento = descuento

    def set_descuento(self, descuento: int):
        self.descuento = descuento

    def calcular_descuento(self):
        if self.descuento:
            print(f"Descuento del {self.descuento}% en {self.nombre}")
        else:
            print(f'"{self.nombre}" no posee ningún descuento')


class Carrito:
    def __init__(self, productos: list):
        self.productos = productos

    def calcular_descuentos(self):
        for producto in self.productos:
            producto.calcular_descuento()


productos = [Producto("manzanas", "alimentos", 30), Producto("jabón", "limpieza")]

carrito = Carrito(productos)
carrito.calcular_descuentos()


