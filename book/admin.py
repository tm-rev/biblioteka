from django.contrib import admin


from book.models import Ksiazka, Wydanie, Egzemplarz, Autor, Kategoria, Ocena, Polka, Rezerwacja, Wypozyczenie


# Re-register UserAdmin
class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('tytul',)
    filter_horizontal = ('autorzy', 'kategorie')

admin.site.register(Ksiazka, KsiazkaAdmin)


class WydanieAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'liczba_stron')

admin.site.register(Wydanie, WydanieAdmin)


class EgzemplarzAdmin(admin.ModelAdmin):
    list_display = ('status', 'wydanie_ISBN')

admin.site.register(Egzemplarz, EgzemplarzAdmin)


class AutorAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko')



admin.site.register(Autor, AutorAdmin)


class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('nazwa',)

admin.site.register(Kategoria, KategoriaAdmin)


class OcenaAdmin(admin.ModelAdmin):
    list_display = ('wydanie_ISBN', 'oceniajacy')

admin.site.register(Ocena, OcenaAdmin)


class PolkaAdmin(admin.ModelAdmin):
    list_display = ('wlasciciel', 'nazwa')

admin.site.register(Polka, PolkaAdmin)


class RezerwacjaAdmin(admin.ModelAdmin):
    list_display = ('wydanie_ISBN', 'rezerwujacy')

admin.site.register(Rezerwacja, RezerwacjaAdmin)


class WypozyczenieAdmin(admin.ModelAdmin):
    list_display = ('wydanie_ISBN', 'wypozyczajacy')

admin.site.register(Wypozyczenie, WypozyczenieAdmin)

