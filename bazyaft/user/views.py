# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .serializers import KhanevarEmailRegisterSerializer  ,EdariEmailRegisterSerializer, TegariEmailRegisterSerializer


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
