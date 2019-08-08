from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes



# Create your views here.

from .serializers import ItemsSerializer
from .models import Items


@permission_classes((AllowAny,))
class GetImage(APIView):

    def get(self, request, format=None):
        id = request.data['id']
        try:
            item = Items.objects.get(id=id)
            return HttpResponse(item.image, content_type="image/png")
        except:
            return Response({"status":False}, status=status.HTTP_201_CREATED)




class ItemsList(ListAPIView):

    serializer_class = ItemsSerializer
    permission_classes = (AllowAny,)
    queryset = Items.objects.all()



class ItemCreate(CreateAPIView):


    serializer_class = ItemsSerializer
    permission_classes = (AllowAny,)

    def post(self, request):

        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():

            # Save request image in the database
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
