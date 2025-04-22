# Utilizando el Principio de Inversión de Dependencias (DIP), modificar el siguiente código de manera que se puedan incorporar otros
# mecanismos de comunicación además de Correo Electrónico para enviar notificaciones.


# class CorreoElectronico:
#     def enviar_notificacion(self, destinatario: str, mensaje: str):
#         # Lógica para enviar notificación por correo electrónico
#         print(f"Correo electrónico enviado a {destinatario}: {mensaje}")


# class Notificador:
#     def __init__(self, correo_electronico: CorreoElectronico):
#         self.correo_electronico = correo_electronico

#     def enviar_notificacion(self, destinatario: str, mensaje: str):
#         self.correo_electronico.enviar_notificacion(destinatario, mensaje)


# # Uso del código actual
# correo_electronico = CorreoElectronico()
# notificador = Notificador(correo_electronico)
# notificador.enviar_notificacion("usuario@example.com", "¡Tu tarea está lista!")


from abc import ABC, abstractmethod

class Medio(ABC):
    @abstractmethod
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        pass

class CorreoElectronico(Medio):
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        # Lógica para enviar notificación por correo electrónico
        print(f"Correo electrónico enviado a {destinatario}: {mensaje}")

class SMS(Medio):
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        # Lógica para enviar notificación por correo electrónico
        print(f"Sms enviado a {destinatario}: {mensaje}")

class Notificador:
    def __init__(self, medio: Medio):
        self.medio = medio

    def enviar_notificacion(self, destinatario: str, mensaje: str):
        self.medio.enviar_notificacion(destinatario, mensaje)


# Uso del código actual
correo_electronico = CorreoElectronico()
notificador = Notificador(correo_electronico)
notificador.enviar_notificacion("usuario@example.com", "¡Tu tarea está lista!")

sms = SMS()

notificador = Notificador(sms)
notificador.enviar_notificacion("3425986910", "¡Tu tarea está lista!")