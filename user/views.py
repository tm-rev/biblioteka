
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from user.models import SiteUser
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import authenticate, login
from user.serializers import SiteUserSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['POST'])
def do_register(request):
    data = JSONParser().parse(request)
    serializer = SiteUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)


@api_view(['POST'])
def do_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response('LOGGED IN')
    else:
        return Response('AUTH FAILED', status=status.HTTP_400_BAD_REQUEST)