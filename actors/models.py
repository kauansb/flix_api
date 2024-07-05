from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),  # valor a esquerda é salvo no banco de dados e valor a direita é exposto no app
    ('BRAZIL', 'Brasil'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
