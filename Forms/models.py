from django.db import models

class Form(models.Model):
    nombre_completo = models.CharField(max_length=80)
    cedula = models.CharField(max_length=30)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=80)

    respuesta_pregunta1 = models.CharField(max_length=20) #En relación a esta compra, ¿qué opinión tienes sobre la atención que recibiste del asesor?
    respuesta_pregunta2 = models.CharField(max_length=10) #¿Contaste con la asistencia de un asesor?

    respuesta_preguntaA = models.CharField(max_length=10, null=True, blank=True) #¿La información que te dio el asesor fue fácil de entender en cuanto al valor de la cuota y el plazo?
    respuesta_preguntaB = models.CharField(max_length=10, null=True, blank=True) #¿Fue el asesor amable y paciente al responder tus preguntas?
    respuesta_preguntaC = models.CharField(max_length=10, null=True, blank=True) #¿La cajera le informo en caja sobre el valor de la cuota y el plazo del credito?

    respuesta_pregunta_comentarios = models.CharField(max_length=300)