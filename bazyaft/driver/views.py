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
from user.serializers import OrderSerializer
from user.serializers import OrderDriverSerializer


class GetMyAcceptedOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        serializer = OrderDriverSerializer(Order.objects.filter(driver=request.user) , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)




class AcceptOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            id = request.data['id']
            try:
                order = Order.objects.get(id=id)
                order.driver = request.user
                order.order_status = "accepted"
                order.save()
                return Response( {"status":True, }  ,status=status.HTTP_200_OK)
            except:
                return Response( {"status":False, "error":"165" }  ,status=status.HTTP_200_OK)
        except:
            return Response( {"status":False, "error":"166" }  ,status=status.HTTP_200_OK)


class CancelOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            id = request.data['id']
            try:
                order = Order.objects.get(id=id)
                order.driver = None
                order.order_status = "in queue"
                order.save()
                return Response( {"status":True, }  ,status=status.HTTP_200_OK)
            except:
                return Response( {"status":False, "error":"165" }  ,status=status.HTTP_200_OK)
        except:
            return Response( {"status":False, "error":"166" }  ,status=status.HTTP_200_OK)







class GetAllOrders (APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get(self, request, format=None):

        serializer = OrderDriverSerializer( Order.objects.filter(order_status="in queue") , many=True)
        # if serializer.is_valid():
        return Response(serializer.data , status=status.HTTP_200_OK)

        # else:
        return Response(serializer.errors  , status=status.HTTP_400_BAD_REQUEST)
