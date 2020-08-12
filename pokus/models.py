from django.db import models

class Zbozi(models.Model):
    nazev = models.CharField(max_length=30)
    cena = models.FloatField(max_length=10)

    def __str__(self):
        return "Nazev: {0} | Cena: {1}".format(self.nazev, self.cena)

class Komentar(models.Model):
    hlavicka = models.CharField(max_length=30)
    koment = models.TextField(max_length=200)



    def __str__(self):
        return "recenze: {0}".format(self.koment)
