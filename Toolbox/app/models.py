from django.db import models

# Create your models here.

class Application(models.Model):
    class Meta:
        verbose_name_plural = 'Applications'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    functionname = models.CharField(max_length=50)
    templatetext = models.CharField(max_length=500)
    inputanzahl = models.IntegerField()
    outputanzahl = models.IntegerField()

