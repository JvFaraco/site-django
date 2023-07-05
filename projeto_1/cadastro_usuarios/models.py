from django.db import models
# PARTE DO BANCO DE DADOS
class Usuario(models.Model):

    id_usuario = models.AutoField(primary_key=True)

    nome = models.TextField()

    idade = models.IntegerField()



