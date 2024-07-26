from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(max_length=500)
    description = models.TextField()
    created_date = models.DateField()
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'Публикации'


# Create your models here.
