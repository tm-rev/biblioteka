from django.db import models


class Autor(models.Model):
    imie = models.CharField(max_length=150)
    nazwisko = models.CharField(max_length=150)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

class Ksiazka(models.Model):
    kategorie = models.ManyToManyField(Kategoria)
    autorzy = models.ManyToManyField(Autor)
    tytul = models.CharField(max_length=500)


class Wydanie(models.Model):
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)

    ISBN = models.CharField(max_length=13)
    data_wydania = models.DateField()
    liczba_stron = models.IntegerField()
    wydawnictwo = models.CharField(max_length=350)


class Egzemplarz(models.Model):
    wydanie = models.ForeignKey(Wydanie, on_delete=models.CASCADE)

    status = models.IntegerField()

    @property
    def wydanie_ISBN(self):
        return self.wydanie.ISBN




