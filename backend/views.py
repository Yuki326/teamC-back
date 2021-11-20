from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def test(request):
    id='0'
    if 'id' in request.GET:
      id = int(request.GET['id'])
    id = id+1
    return Response(str(id), status=status.HTTP_201_CREATED)
