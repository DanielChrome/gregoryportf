from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Postagem(models.Model):
    titulo         = models.CharField(max_length = 255)
    datapublicacao = models.DateField()
    usuario        = models.ForeignKey(User)
