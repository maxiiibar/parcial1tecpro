from abc import ABC, abstractmethod

# class IUsuario(ABC):
#     @abstractmethod
#     def solicitar_prestamo_libro(self):
#         pass

#     @abstractmethod
#     def devolver_libro(self):
#         pass

#     @abstractmethod
#     def buscar_libro(self):
#         pass

#     @abstractmethod
#     def solicitar_reserva_sala_estudio(self):
#         pass

# class Estudiante(IUsuario):
#     def solicitar_prestamo_libro(self):
#         print("Estudiante solicitando préstamo de libro.")

#     def devolver_libro(self):
#         print("Estudiante devolviendo libro.")

#     def buscar_libro(self):
#         print("Estudiante buscando libro en el catálogo.")

#     def solicitar_reserva_sala_estudio(self):
#         raise NotImplementedError("Los estudiantes no pueden reservar salas de estudio.")

# class Profesor(IUsuario):
#     def solicitar_prestamo_libro(self):
#         print("Profesor solicitando préstamo de libro.")

#     def devolver_libro(self):
#         print("Profesor devolviendo libro.")

#     def buscar_libro(self):
#         print("Profesor buscando libro en el catálogo.")

#     def solicitar_reserva_sala_estudio(self):
#         print("Profesor solicitando reserva de sala de estudio.")

# # Ejemplo de uso
# estudiante = Estudiante()
# profesor = Profesor()

# estudiante.solicitar_prestamo_libro()
# estudiante.devolver_libro()
# estudiante.buscar_libro()

# profesor.solicitar_prestamo_libro()
# profesor.devolver_libro()
# profesor.buscar_libro()
# profesor.solicitar_reserva_sala_estudio()


# El principio que se viola es el de segregación de interfaces, ya que la interfaz IUsuario
# obliga a todos los usuarios a implementar métodos que no son relevantes para cada tipo de usuario.

class IPrestamo(ABC):
    @abstractmethod
    def solicitar_prestamo_libro(self): pass

    @abstractmethod
    def devolver_libro(self): pass

    @abstractmethod
    def buscar_libro(self): pass

class IReservaSalaEstudio(ABC):
    @abstractmethod
    def solicitar_reserva_sala_estudio(self): pass

class Estudiante(IPrestamo):
    def solicitar_prestamo_libro(self):
        print("Estudiante solicitando préstamo de libro.")

    def devolver_libro(self):
        print("Estudiante devolviendo libro.")

    def buscar_libro(self):
        print("Estudiante buscando libro en el catálogo.")
        

class Profesor(IPrestamo, IReservaSalaEstudio):
    def solicitar_prestamo_libro(self):
        print("Profesor solicitando préstamo de libro.")

    def devolver_libro(self):
        print("Profesor devolviendo libro.")

    def buscar_libro(self):
        print("Profesor buscando libro en el catálogo.")

    def solicitar_reserva_sala_estudio(self):
        print("Profesor solicitando reserva de sala de estudio.")

# Ejemplo de uso
estudiante = Estudiante()
profesor = Profesor()

estudiante.solicitar_prestamo_libro()
estudiante.devolver_libro()
estudiante.buscar_libro()

profesor.solicitar_prestamo_libro()
profesor.devolver_libro()
profesor.buscar_libro()
profesor.solicitar_reserva_sala_estudio()