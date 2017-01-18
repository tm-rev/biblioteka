from rest_framework import serializers
from book.models import Ksiazka, Wydanie, Egzemplarz, Ocena, Polka, Rezerwacja, Wypozyczenie


class KsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = '__all__'
        depth = 2

class WydanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wydanie
        fields = '__all__'


class EgzemplarzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egzemplarz
        fields = '__all__'

class OcenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocena
        fields = '__all__'

class PolkaSerializer(serializers.ModelSerializer):
    wydania = WydanieSerializer(many=True)
    class Meta:
        model = Polka
        fields = '__all__'

class RezerwacjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezerwacja
        fields = '__all__'

class WypozyczenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczenie
        fields = '__all__'
