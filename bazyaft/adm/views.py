from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes



# Create your views here.

from .serializers import ImageSerializer
from .models import Image


@permission_classes((AllowAny,))
class getfirstimage(APIView):

    def get(self, request, format=None):
        img = Image.objects.all()[0].image
        return HttpResponse(img, content_type="image/png")



class ImageList(ListAPIView):

    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)
    queryset = Image.objects.all()



class ImageCreate(CreateAPIView):


    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)

    def post(self, request):

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():

            # Save request image in the database
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
