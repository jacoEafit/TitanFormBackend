from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):

    respuesta_preguntaA = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )

    respuesta_preguntaB = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )

    respuesta_preguntaC = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )

    class Meta:
        model = Form
        fields = ['nombre_completo','cedula','correo_electronico','telefono','respuesta_pregunta1','respuesta_pregunta2','respuesta_preguntaA','respuesta_preguntaB','respuesta_preguntaC','respuesta_pregunta_comentarios']