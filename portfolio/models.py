from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=200, blank=True, default='')
    cliente = models.TextField(blank=True, default='')
    descricao = models.TextField(blank=True, default='')
    link_youtube = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class Imagem(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, blank=True, default=None)
    imagem = models.ImageField(upload_to='imagens/', blank=True)
    descricao = models.TextField(blank=True, default='')

    def __str__(self):
        return self.descricao
