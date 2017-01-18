from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from book.models import Ksiazka, Ocena, Polka
from book.serializers import KsiazkaSerializer, OcenaSerializer, PolkaSerializer, RezerwacjaSerializer, WypozyczenieSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


class KsiazkaList(generics.ListAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'tytul', 'kategorie', 'autorzy')


class KsiazkaDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OcenaCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = OcenaSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OcenaList(generics.GenericAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer
    filter_backends = (DjangoFilterBackend)
    filter_fields = ('wydanie')


class PolkaCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PolkaSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PolkaViewSet(viewsets.ModelViewSet):
    queryset = Polka.objects.all()
    serializer_class = PolkaSerializer


class RezerwacjaCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = RezerwacjaSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WypozyczenieCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = WypozyczenieSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
