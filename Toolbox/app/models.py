from django.db import models


class Application(models.Model):
    class Meta:
        verbose_name_plural = 'Applications'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    function = models.CharField(max_length=500)
    template_text = models.CharField(max_length=500)
    input_anzahl = models.IntegerField()
    output_anzahl = models.IntegerField()
    error_message = models.CharField(max_length=100)
