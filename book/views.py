from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from book.models import Ksiazka
from book.serializers import KsiazkaSerializer
from rest_framework import mixins
from rest_framework import generics


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
 