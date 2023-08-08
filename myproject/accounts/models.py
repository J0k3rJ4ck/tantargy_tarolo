from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model): #felhasznalo model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Tantargy(models.Model):
    nev = models.CharField(max_length=200)
    felhasznalo = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nev


class Kovetelmeny(models.Model):
    leiras = models.TextField()
    statusz = models.BooleanField(default=False)
    tantargy = models.ForeignKey(Tantargy, related_name="kovetelmenyek", on_delete=models.CASCADE)
    felhasznalo = models.ForeignKey(User, related_name="kovetelmenyek", on_delete=models.CASCADE)
    hatarido = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.leiras