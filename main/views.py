from django.shortcuts import render
from rest_framework.response import Response
from .models import Letter
from rest_framework.views import APIView
from .serializers import LetterSerializer
from .thecamp_sender import test_send, send


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


class PingAPI(APIView):
    def get(self, *args, **kwargs):
        return Response(
            {'ping': 'pong'}
            , status=200
        )


class LetterAPI(APIView):
    def post(self, request):
        serializer = LetterSerializer(data=request.data)
        if serializer.is_valid():
            test_send(serializer.save())
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

