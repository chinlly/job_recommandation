from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(null = True, max_length=20)
    keyword = models.CharField(null = True, max_length=20)
    skills = models.TextField(null = True, blank = True)
    keyword = models.CharField(null = True, max_length=20)

    def __str__(self) -> str:
        return f"{self.title}"
