from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length = 255)
    contact = models.CharField(max_length =225)
    address = models.CharField(max_length = 255)

def __str__(self):
    return f'{self.name} {self.contact} {self.address}'

