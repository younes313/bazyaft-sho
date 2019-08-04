# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.core.mail import EmailMessage
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect

from random import randint
from datetime import datetime

from .models import Order
from .serializers import *


from PIL import Image

@permission_classes((AllowAny,))
class image_view(APIView):

    def get(self, request ,format=None):

        try:
            img  = Image.open("static/images/a.png")
        except:
            return Response({"sd":"Sdf"} , status=status.HTTP_400_BAD_REQUEST)
        return redirect("/../static/images/a.png")


@permission_classes((IsAuthenticated,))
class GetOrder(APIView):

    def post(self, request, format=None):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():

            order = Order.objects.create(user=request.user, **serializer.validated_data)

            dic = {'user_id': request.user.id , 'order_id' : order.id }
            dic.update(serializer.data)

            return Response(dic , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny,))
class GetTokenPhone(APIView):

    def post(self, request, format=None):
        serializer = GetTokenPhoneSerializer(data = request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(username = serializer.data["username"])
                try :
                    if str(user.khanevar.code) == str(serializer.data['code']) :
                        token , _ = Token.objects.get_or_create(user=user)
                        return Response({"status":True, "token":token.key}, status=status.HTTP_200_OK)
                except:
                    pass
                try :
                    if user.edari.code == serializer.data['code'] :
                        token , _ = Token.objects.get_or_create(user=user)
                        return Response({"status":True, "token":token.key}, status=status.HTTP_200_OK)
                except:
                    pass
                try :
                    if user.tegari.code == serializer.data['code'] :
                        token , _ = Token.objects.get_or_create(user=user)
                        return Response({"status":True, "token":token.key}, status=status.HTTP_200_OK)
                except:
                    pass
            except:
                return Response( {"status":False , "error" : "101"} , status = status.HTTP_200_OK)
        else:
            return Response({"status":False , "error" : "103"}, status = status.HTTP_200_OK)


        return Response({"status":False , "error" : "102"}, status = status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
class UserLogout(APIView):

    def post(slef, request, format=None):
        try:
            request.user.auth_token.delete()
            return Response({'status':True}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



@permission_classes((AllowAny,))
class GetTokenUsername(APIView):

    def post(self, request, format=None):
        serializer = GetTokenUsernameSerializer(data = request.data)
        if serializer.is_valid():
            userr = authenticate(request=request, username=serializer.data['username'], password=serializer.data['password'])
            if not userr:
                dic = { "status":False , "error" : "101"    }
                return Response(dic, status = status.HTTP_200_OK)
            token , _ = Token.objects.get_or_create(user=userr)
            return Response({"status":True, "token":token.key}, status=status.HTTP_200_OK)
        else:
            dic = { "status":False , "error" : "103"    }
            return Response(dic, status = status.HTTP_200_OK)

@permission_classes((AllowAny,))
class GetTokenEmail(APIView):

    def post(self, request, format=None):
        serializer = GetTokenEmailSerializer(data = request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email = serializer.data["email"])
                userr = authenticate(request=request, username=user.username, password=serializer.data['password'])
                if not userr:
                    dic = { "status":False , "error" : "101"    }
                    return Response(dic, status = status.HTTP_200_OK)
                token , _ = Token.objects.get_or_create(user=user)
                return Response({"status":True, "token":token.key}, status=status.HTTP_200_OK)
            except:
                dic = { "status":False , "error" : "102"    }
                return Response(dic, status = status.HTTP_200_OK)
        else:
            dic = { "status":False , "error" : "103"    }
            return Response(dic, status = status.HTTP_200_OK)


@permission_classes((AllowAny,))
class KhanevarEmailRegister(APIView):
    serializer_class = KhanevarEmailRegisterSerializer()

    def post(self, request, format=None):
        serializer = KhanevarEmailRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            dic = {'data' :serializer.data }
            dic.update({'status': True})
            dic['data'].update({'status':'101'})
            # print(serializer.data)
            # email = EmailMessage('email_subject', "message", to=['younesmoradi313@gmail.com',])
            # email.send()
            user = User.objects.get(username = serializer.data['user']['username'])
            if user.khanevar.phone_number != "":
                code = randint(100000 , 999999)
                dic['data']['code'] = code
                user.khanevar.code = code
                user.khanevar.save()
                return Response(dic, status=status.HTTP_201_CREATED)
            else:
                token, created = Token.objects.get_or_create(user=user)
                dic['data'].update({"token" : token.key})
                return Response(dic, status=status.HTTP_201_CREATED)
        else:
            dic = dict({'status': [] })
            try:
                dic["status"].extend( serializer.errors['user']["non_field_errors"] )
            except:
                pass
            try:
                for err in serializer.errors['user']['email'] :
                    # if str(err) == "user email with this email already exists.":
                    #     dic['status'].append('102')
                    if str(err) ==  "Enter a valid email address.":
                        dic['status'].append('103')
                    if str(err) == "Ensure this field has no more than 254 characters.":
                        dic['status'].append('104')
                    # if str(err) == "This field may not be blank.":
                    #     dic['status'].append('105')
            except:
                pass
            try:
                for err in serializer.errors['user']['username']:
                    if str(err) == "A user with that username already exists.":
                        dic['status'].append('110')
                    if str(err) ==  "This field may not be blank.":
                        dic['status'].append('111')

            except:
                pass
            dic2 = {'status':False , 'data': dic}
            # return Response(serializer.errors , sta   tus=status.HTTP_400_BAD_REQUEST)
            return Response(dic2 , status=status.HTTP_201_CREATED)


@permission_classes((IsAuthenticated,))
class GetMyCoins(APIView):

    def get(self, request, format=None):
        try:
            return Response( {'coins':request.user.khanevar.coins , } , status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny,))
class EdariEmailRegister(APIView):
    serializer_class = EdariEmailRegisterSerializer

    def post(self, request, format=None):
        serializer = EdariEmailRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            dic = {'data' :serializer.data }
            dic.update({'status': True})
            dic['data'].update({'status':'101'})

            user = User.objects.get(username = serializer.data['user']['username'])
            if user.edari.phone_number != "":
                code = randint(100000 , 999999)
                dic['data']['code'] = code
                user.edari.code = code
                user.edari.save()
                return Response(dic, status=status.HTTP_201_CREATED)
            else:
                token, created = Token.objects.get_or_create(user=user)
                dic['data'].update({"token" : token.key})
                return Response(dic, status=status.HTTP_201_CREATED)
        else:
            dic = dict({'status': [] })
            try:
                dic["status"].extend( serializer.errors['user']["non_field_errors"] )
            except:
                pass
            try:
                for err in serializer.errors['user']['email'] :
                    # if str(err) == "user email with this email already exists.":
                    #     dic['status'].append('102')
                    if str(err) ==  "Enter a valid email address.":
                        dic['status'].append('103')
                    if str(err) == "Ensure this field has no more than 254 characters.":
                        dic['status'].append('104')
                    # if str(err) == "This field may not be blank.":
                    #     dic['status'].append('105')
            except:
                pass
            try:
                for err in serializer.errors['user']['username']:
                    if str(err) == "A user with that username already exists.":
                        dic['status'].append('110')
                    if str(err) ==  "This field may not be blank.":
                        dic['status'].append('111')

            except:
                pass
            dic2 = {'status':False , 'data': dic}
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(dic2 , status=status.HTTP_201_CREATED)


@permission_classes((AllowAny,))
class TegariEmailRegister(APIView):
    serializer_class = TegariEmailRegisterSerializer

    def post(self, request, format=None):
        serializer = TegariEmailRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            dic = {'data' :serializer.data }
            dic.update({'status': True})
            dic['data'].update({'status':'101'})

            user = User.objects.get(username = serializer.data['user']['username'])
            if user.tegari.phone_number != "":
                code = randint(100000 , 999999)
                dic['data']['code'] = code
                user.tegari.code = code
                user.tegari.save()
                return Response(dic, status=status.HTTP_201_CREATED)
            else:
                token, created = Token.objects.get_or_create(user=user)
                dic['data'].update({"token" : token.key})
                return Response(dic, status=status.HTTP_201_CREATED)
        else:
            dic = dict({'status': [] })
            try:
                dic["status"].extend( serializer.errors['user']["non_field_errors"] )
            except:
                pass
            try:
                for err in serializer.errors['user']['email'] :
                    # if str(err) == "user email with this email already exists.":
                    #     dic['status'].append('102')
                    if str(err) ==  "Enter a valid email address.":
                        dic['status'].append('103')
                    if str(err) == "Ensure this field has no more than 254 characters.":
                        dic['status'].append('104')
                    # if str(err) == "This field may not be blank.":
                    #     dic['status'].append('105')
            except:
                pass
            try:
                for err in serializer.errors['user']['username']:
                    if str(err) == "A user with that username already exists.":
                        dic['status'].append('110')
                    if str(err) ==  "This field may not be blank.":
                        dic['status'].append('111')

            except:
                pass
            dic2 = {'status':False , 'data': dic}
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(dic2 , status=status.HTTP_201_CREATED)
