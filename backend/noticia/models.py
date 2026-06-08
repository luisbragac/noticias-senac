from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    ativa = models.BooleanField()
    data_publicao = models.DateField(auto_now_add=True)

    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        blank= True, 
        null= True, 
        related_name='produtos'
        )


