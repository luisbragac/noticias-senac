from rest_framework import serializers
from noticia.models import Noticia, Categoria

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'