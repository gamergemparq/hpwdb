from django.db import models

# Create your models here.


class Gitlog3(models.Model):
    name = models.CharField(max_length=255)
    day = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
