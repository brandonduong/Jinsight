from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ExpirationList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expirationlist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    expiration_list = models.ForeignKey(ExpirationList, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    good = models.BooleanField()

    def __str__(self):
        return self.text
