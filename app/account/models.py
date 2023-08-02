from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['id']
