from rest_framework import serializers
from . models import Curso, Avaliacao

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
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
        read_only_fields = (
            'curso',
        )

class CursoSerializer(serializers.ModelSerializer):

    avaliacoes = AvaliacaoSerializer(many=True)

    class Meta:    
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
        )

    def create(self, validated_data):
        
        avaliacoes_data = validated_data.pop('avaliacoes')
        curso = Curso.objects.create(**validated_data)

        for avaliacao_data in avaliacoes_data:
            Avaliacao.objects.create(curso=curso, **avaliacao_data)
        return curso