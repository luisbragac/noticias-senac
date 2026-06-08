from rest_framework import viewsets
from noticia.serializers import NoticiaSerializer
from noticia.models import Noticia

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer