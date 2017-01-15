from django.contrib import admin


from book.models import Ksiazka, Wydanie, Egzemplarz, Autor, Kategoria


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

