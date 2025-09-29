from django.db import models

# Create your models here.

class Smuser(models.Model):
    firstname = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.firstname
    

