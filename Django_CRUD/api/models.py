from django.db import models

# Create your models here.
class User(models.Model):
    nama = models.CharField(max_length=100)
    usia = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama