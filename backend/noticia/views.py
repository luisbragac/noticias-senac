from rest_framework import viewsets
from noticia.serializers import NoticiaSerializer, CategoriaSerializer
from noticia.models import Noticia, Categoria

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer