from django.db import models
from user.models import SiteUser


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


class Ocena(models.Model):
    uzytkownik = models.ForeignKey(SiteUser)
    wydanie = models.ForeignKey(Wydanie, on_delete=models.CASCADE)
    wartosc = models.IntegerField()

    @property
    def oceniajacy(self):
        return self.uzytkownik.username

    @property
    def wydanie_ISBN(self):
        return self.wydanie.ISBN


class Polka(models.Model):
    uzytkownik = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=50)
    wydania = models.ManyToManyField(Wydanie)

    @property
    def wlasciciel(self):
        return self.uzytkownik.username


class Rezerwacja(models.Model):
    NOWA = 0
    ROZPATRZONA = 1
    STATUSY_REZERWACJI = (
        (NOWA, 'Nowa'),
        (ROZPATRZONA, 'Rozpatrzona')
    )
    uzytkownik = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    wydanie = models.ForeignKey(Wydanie, on_delete=models.CASCADE)
    data_rezerwacji = models.DateField()
    status = models.IntegerField(default = NOWA, choices = STATUSY_REZERWACJI)

    @property
    def rezerwujacy(self):
        return self.uzytkownik.username

    @property
    def wydanie_ISBN(self):
        return self.wydanie.ISBN


class Wypozyczenie(models.Model):
    czytelnik = models.ForeignKey(SiteUser)
    egzemplarz = models.ForeignKey(Egzemplarz, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(SiteUser, related_name='wypozyczajacy_pracownik')
    data_wypozyczenia = models.DateField()
    data_zwrotu = models.DateField()

    @property
    def wypozyczajacy(self):
        return self.czytelnik.username

    @property
    def wydanie_ISBN(self):
        return self.egzemplarz.wydanie_ISBN
