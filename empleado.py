# class Empleado:
#     def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
#         self.nombre = nombre
#         self.horas_trabajadas = horas_trabajadas
#         self.tarifa_por_hora = tarifa_por_hora
#     def calcular_salario(self):
#         return self.horas_trabajadas * self.tarifa_por_hora
#     def generar_reporte_desempenio(self):
#         pass

# Se viola el princio de responsabilidad único, ya que la clase Empleado tiene dos responsabilidades:
# 1. Calcular el salario del empleado.
# 2. Generar un reporte de desempeño.

# Mi solución:

class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
class Estadisticas:
    def calcular_salario(self, empleado : Empleado):
        return empleado.horas_trabajadas * empleado.tarifa_por_hora
    
    def generar_report_desenpenio(self, empleado : Empleado):
        return (
            f"Desempeño de {empleado.nombre}\n"
            f"Horas trabajadas: {empleado.horas_trabajadas}\n"
            f"Tarifa por hora: {empleado.tarifa_por_hora}"
        )
    
    
empleado = Empleado("Máximo", 36, 2500)
stats = Estadisticas();
print(stats.calcular_salario(empleado))
print(stats.generar_report_desenpenio(empleado))