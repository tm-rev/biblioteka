from django.db import models

from django.contrib.auth.models import User

class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    status = models.IntegerField()
    stanowisko = models.CharField(max_length=150)
    kod_pocztowy = models.CharField(max_length=6)
    nr_tel = models.CharField(max_length=12)
    miasto = models.CharField(max_length=250)
    nr_domu = models.CharField(max_length=10)
    nr_lokalu = models.CharField(max_length=10)