from rest_framework import serializers
from . models import Curso, Avaliacao

class CursoSerializer(serializers.ModelSerializer):

    class Meta:    
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'emal',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
