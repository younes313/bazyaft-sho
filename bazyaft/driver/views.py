from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


from user.models import Order
from user.serializers import OrderDriverSerializer





class GetAllOrders (APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get(this, request, format=None):

        serializer = OrderDriverSerializer( Order.objects.all() , many=True)
        # if serializer.is_valid():
        return Response(serializer.data , status=status.HTTP_200_OK)

        # else:
        return Response(serializer.errors  , status=status.HTTP_400_BAD_REQUEST)
