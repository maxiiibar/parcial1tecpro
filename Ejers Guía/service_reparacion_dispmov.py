# class Dispositivo:
#     def __init__(self, marca: str, modelo: str):
#         self.marca = marca
#         self.modelo = modelo


# class Celular(Dispositivo):
#     def __init__(self, marca: str, modelo: str, pantalla: bool):
#         super().__init__(marca, modelo)
#         self.pantalla = pantalla


# class Tablet(Dispositivo):
#     def __init__(self, marca: str, modelo: str, pantalla: bool, lapiz: bool):
#         super().__init__(marca, modelo)
#         self.pantalla = pantalla
#         self.lapiz = lapiz


# class Smartwatch(Dispositivo):
#     def __init__(self, marca: str, modelo: str, pantalla: bool, gps: bool):
#         super().__init__(marca, modelo)
#         self.pantalla = pantalla
#         self.gps = gps


# def contar_piezas_reparacion(dispositivos: list):
#     for dispositivo in dispositivos:
#         if isinstance(dispositivo, Celular):
#             print(contar_piezas_celular(dispositivo))
#         elif isinstance(dispositivo, Tablet):
#             print(contar_piezas_tablet(dispositivo))
#         elif isinstance(dispositivo, Smartwatch):
#             print(contar_piezas_smartwatch(dispositivo))


# # Funciones para contar piezas de repuesto específicas para cada tipo de dispositivo
# def contar_piezas_celular(celular: Celular):
#     return "Piezas requeridas para reparar el celular"


# def contar_piezas_tablet(tablet: Tablet):
#     return "Piezas requeridas para reparar la tablet"


# def contar_piezas_smartwatch(smartwatch: Smartwatch):
#     return "Piezas requeridas para reparar el smartwatch"


# # Ejemplo de uso
# dispositivos = [
#     Celular("Samsung", "Galaxy S20", True),
#     Tablet("Apple", "iPad Pro", True, True),
#     Smartwatch("Apple", "Watch Series 6", True, True),
# ]
# contar_piezas_reparacion(dispositivos)

#El princio que se viola es el de OCP, ya que si quisieras agregar un nuevo dispositivo deberíamos agregar una
#nueva clase y modificar la función contar_piezas_reparacion, lo que va en contra del principio de OCP (Open/Closed Principle).

from abc import ABC, abstractmethod


class Dispositivo(ABC):
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        
    @abstractmethod
    def contar_piezas_reparacion(self):
        pass

class Celular(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla
    
    def contar_piezas_reparacion(self):
        return "Piezas requeridas para reparar el celular"


class Tablet(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, lapiz: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla
        self.lapiz = lapiz
        
    def contar_piezas_reparacion(self):
        return "Piezas requeridas para reparar la tablet"


class Smartwatch(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, gps: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla
        self.gps = gps
        
    def contar_piezas_reparacion(self):
        return "Piezas requeridas para reparar el smartwatch"


def contar_piezas_reparacion(dispositivos: list):
    for dispositivo in dispositivos: 
        print(dispositivo.contar_piezas_reparacion())

# Ejemplo de uso
dispositivos = [
    Celular("Samsung", "Galaxy S20", True),
    Tablet("Apple", "iPad Pro", True, True),
    Smartwatch("Apple", "Watch Series 6", True, True),
]
contar_piezas_reparacion(dispositivos)