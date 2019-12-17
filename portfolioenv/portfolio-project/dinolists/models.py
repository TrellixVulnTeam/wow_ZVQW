from django.db import models

# Create your models here.
class Dinolist(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    overview = models.CharField(max_length=5000)
    character = models.CharField(max_length=5000)
    def __str__(self):
		return self.name
