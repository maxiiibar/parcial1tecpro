# 1) 
#   1. Clase Persona no está marcada como abstracta:
#   Persona parece ser usada solo como clase base, ya que no tiene sentido que exista una persona 
#   “genérica” en este sistema que no sea ni diputado, ni senador, ni asesor. Sin embargo, el diagrama
#   no la marca como abstracta.

#   2. Atributos posiblemente redundantes en las subclases: 
#   Las subclases (Diputado, Senador, Asesor) solo agregan un atributo específico cada una, lo que puede
#   ser un diseño pobre o sintomático de que el atributo que las diferencia podría modelarse de otra manera
#   (por ejemplo, mediante una relación con otra clase que represente su "rol" o su "especialización"). 
#   Quizas esto se deba a que falta bastante de la consigna que nos explique más a detalle las funcionalidades
#   que se esperan del sistema

#2) 
#   Yo lo que haría sería hacer a persona una clase abstracta, luego de ella saldría legislador que usaría esa,
#   interfaz, y de esta última se obtendrían las clases diputados y senadores. 
#   Ya que se pide de manera escrita, habría que especificar que existiría una relación entre legislador y proyecto 
#   de ley, ya que el proyecto de ley es presentado por un único legislador. Esta relación será en entre PDL y 
#   Legislador, no con sus clases hijas, y sería de 1 a muchos (el legislador estar a cargo de 0 a muchos proyectoes
#   y el proyecto tendrá exactamente un legislador a cargo). Luego si habrá otra relación con funcionalidad de muchos
#   a muchos entre legisladores y proyecto, que tendrán roles secundarios en el proyecto (no serán los que lo presenten).
#   Habría que hacer un historico entre legislador y firmantes del proyecto con la fecha, en realidad esa sería la relación.
#   Y los asesores son los que tendrán una relación con la clase legislador. 