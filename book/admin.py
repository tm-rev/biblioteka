from django.contrib import admin


from book.models import Ksiazka, Wydanie, Egzemplarz


# Re-register UserAdmin
class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tytul')

admin.site.register(Ksiazka, KsiazkaAdmin)

class WydanieAdmin(admin.ModelAdmin):
    list_display = ('id', 'ISBN', 'liczba_stron')

admin.site.register(Wydanie, WydanieAdmin)

class EgzemplarzAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'wydanie_ISBN')


admin.site.register(Egzemplarz, EgzemplarzAdmin)