from django.db import models

# Create your models here.

PORT_STATUS = (
        ('Oulu', 'Oulu'),
        ('Kokkola', 'Kokkola'),
        ('Vaasa', 'Vaasa'),
        ('Pori', 'Pori'),
        ('Aland', 'Aland'),
        ('Turku', 'Turku'),
        ('Helsinki', 'Helsinki'),
        ('Hamina', 'Hamina')
    )


class Boot(models.Model):
    STATUS_CHOICES = (
        ('driving', 'driving'),
        ('stopping', 'stopping')
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=255)

    port = models.CharField(choices=PORT_STATUS, max_length=255)

    def __str__(self):
        return self.port


class Voyage(models.Model):
    depart_time = models.DateTimeField()

    def __str__(self):
        return str(self.depart_time)


class Guide(models.Model):
    name = models.CharField(max_length=255)
    start = models.CharField(choices=PORT_STATUS, max_length=255)
    end = models.CharField(choices=PORT_STATUS, max_length=255)

    def __str__(self):
        return self.name
