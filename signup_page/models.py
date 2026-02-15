from django.db import models


# Create your models here.

class Signup(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
