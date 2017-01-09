from rest_framework import serializers
from user.models import SiteUser


class SiteUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, max_length=250)
    password = serializers.CharField(required=True, max_length=250)
    email = serializers.CharField(required=True, max_length=250)
    first_name = serializers.CharField(required=True, max_length=250)
    last_name = serializers.CharField(required=True, max_length=250)
    status = serializers.IntegerField(read_only=True)
    stanowisko = serializers.CharField(max_length=150)
    kod_pocztowy = serializers.CharField(required=False, max_length=6)
    nr_tel = serializers.CharField(required=False, max_length=12)
    miasto = serializers.CharField(required=False, max_length=250)
    nr_domu = serializers.CharField(required=False, max_length=10)
    nr_lokalu = serializers.CharField(required=False, max_length=10)


    def create(self, validated_data):
        return SiteUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.kod_pocztowy = validated_data.get('kod_pocztowy', instance.kod_pocztowy)
        instance.nr_tel = validated_data.get('nr_tel', instance.nr_tel)
        instance.miasto = validated_data.get('miasto', instance.miasto)
        instance.nr_domu = validated_data.get('nr_domu', instance.nr_domu)
        instance.nr_lokalu = validated_data.get('nr_lokalu', instance.nr_lokalu)
        instance.save()
        return instance



