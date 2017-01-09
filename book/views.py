from book.models import Ksiazka
from book.serializers import KsiazkaSerializer
from rest_framework import mixins
from rest_framework import generics


class KsiazkaList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class KsiazkaDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
