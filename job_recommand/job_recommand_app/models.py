from django.db import models


# Create your models here.
class Account(models.Model):
    # id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
