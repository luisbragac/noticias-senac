from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    ativa = models.BooleanField()
    data_publicao = models.DateField(auto_now_add=True)

    