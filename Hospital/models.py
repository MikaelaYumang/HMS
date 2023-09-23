from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    bloodgroup = models.CharField(max_length=5)

    def __str__(self):
        return self.name


