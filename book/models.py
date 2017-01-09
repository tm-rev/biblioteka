from django.db import models


class Ksiazka(models.Model):
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



