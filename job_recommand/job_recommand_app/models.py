from django.db import models


# Create your models here.
class Account(models.Model):
    # id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

class Profile(models.Model):
    skills = models.TextField()
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.title}"
