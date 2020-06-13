from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ExpirationList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    expiration_list = models.ForeignKey(ExpirationList, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    good = models.CharField(max_length=50)
    date_bought = models.DateTimeField(default=timezone.now)
    date_expired = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
