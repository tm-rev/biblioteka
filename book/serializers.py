from rest_framework import serializers
from book.models import Ksiazka, Wydanie, Egzemplarz


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

