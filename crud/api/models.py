from django.db import models

# Create your models here.
class User(models.Model):
    
    name=models.CharField(max_length=500)
    email=models.EmailField(max_length=500)
    password=models.IntegerField(max_length=100)


def _str_(self):
    return self.name