from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)  # genero do filme (obs: ID NÃO É OBRIGATÓRIO)

    def __str__(self):
        return self.name
