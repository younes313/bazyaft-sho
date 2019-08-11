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
from datetime import datetime ,timedelta

from .models import Order
from .serializers import *

from django.utils import timezone

import requests
# import pytz
# utc=pytz.UTC

# headers = {"Authorization" : "Token e57304bda3e1f1da0fbe1248920896b499db8f48" ,}
# url = "http://Younes313.pythonanywhere.com/adm/ItemsList"
# respone = requests.get(url, headers=headers)
# return Response(respone.json() , status = respone.status_code)


class GetMyInProgresOrder(APIView):
    permission_classes = [ IsAuthenticated]

    def get(self, request, format=None):
        serializer = OrderDriverSerializer(Order.objects.filter(user=request.user) , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)


class CancelOrder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            id = request.data['id']
            try:
                order = Order.objects.get(id=id)
                order.delete()
                return Response( {"status":True, }  ,status=status.HTTP_200_OK)
            except:
                return Response( {"status":False, "error":"165" }  ,status=status.HTTP_200_OK)
        except:
            return Response( {"status":False, "error":"166" }  ,status=status.HTTP_200_OK)






@permission_classes((IsAuthenticated,))
class ConfirmOrCancel(APIView):

    def post(self, request, format=None):


        data = request.data
        id = data['id']
        try:
            order = Order.objects.get(id=id)
        except:
            return Response({"status":False, "error":"160"}, status=status.HTTP_200_OK)
        if order.order_status != "not confirmed":
            return Response({"status":False, "error":"161"}, status=status.HTTP_200_OK)

        if data['status'] == 'true':
            order.order_status = "in queue"
            order.save()
        else:
            order.delete()

        return Response({"status":True,} ,status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
class GetOrder(APIView):

    def post(self, request, format=None):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            dic = {"status":True}
            order = Order.objects.create(user=request.user, **serializer.validated_data)
            if hasattr(request.user , "khanevar"):
                coins = order.calculate_coins()
                total_coins = request.user.khanevar.coins + coins
                if order.give_back_type == "coin":
                    order.coins = coins
                    order.save()
                    dic.update({"coins": order.coins})
                elif order.give_back_type == "bag":
                    order.bag = total_coins//10
                    order.save()
                    dic.update({"bag": order.bag})
                else:
                    return Response({"status":False , "error":"150"} , status=status.HTTP_200_OK)

            elif hasattr(request.user , "edari"):
                if order.give_back_type == "money":
                    order.money = order.calculate_money()
                    order.save()
                    dic.update({"money": order.money})
                else:
                    return Response({"status":False , "error":"150"} , status=status.HTTP_200_OK)

            elif hasattr(request.user , "tegari"):
                if order.give_back_type == "money":
                    order.money = order.calculate_money()
                    order.save()
                    dic.update({"money": order.money})
                else:
                    return Response({"status":False , "error":"150"} , status=status.HTTP_200_OK)


            dic.update( {'user_id': order.user.id , 'order_id' : order.id  } )
            dic.update(serializer.data)

            return Response(dic , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@permission_classes((AllowAny,))
class GetTokenPhonenumber(APIView):

    def post(self, request, format=None):
        serializer = GetTokenPhonenumberSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = Khanevar.objects.get(phone_number = serializer.data["phone_number"]).user
                # userr = authenticate(request=request, username=user.username, password=serializer.data['password'])
                # if not userr:
                #     dic = { "status":False , "error" : "121"    }
                #     return Response(dic, status = status.HTTP_200_OK)
                # token , _ = Token.objects.get_or_create(user=user)
                # user_type = "khanevar"

                if user.khanevar.code_time.year == timezone.now().year and user.khanevar.code_time.month == timezone.now().month and user.khanevar.code_time.day == timezone.now().day and user.khanevar.code_time.hour == timezone.now().hour:
                    if user.khanevar.code_time.minute == timezone.now().minute:
                        remain = 60 -  (timezone.now().second - user.khanevar.code_time.second)
                        return Response({"status":False, 'error':'130', 'remain':remain }, status=status.HTTP_200_OK)
                    elif (timezone.now().minute - user.khanevar.code_time.minute) == 1  and  (timezone.now().second < user.khanevar.code_time.second):
                        remain = 60 - (timezone.now().second + 60 - user.khanevar.code_time.second)
                        return Response({"status":False, 'error':'130', 'remain':remain }, status=status.HTTP_200_OK)
                code = randint(100000 , 999999)
                # dic['data']['code'] = code
                user.khanevar.code = code
                user.khanevar.code_time = timezone.now()
                user.khanevar.save()
                return Response({"status":True, 'username':user.username, 'code':code}, status=status.HTTP_200_OK)
                # return Response({"status":True, "token":token.key, "user_type":user_type}, status=status.HTTP_200_OK)
            except:
                pass
            try:
                user = Edari.objects.get(phone_number = serializer.data["phone_number"]).user
                # userr = authenticate(request=request, username=user.username, password=serializer.data['password'])
                # if not userr:
                #     dic = { "status":False , "error" : "121"    }
                #     return Response(dic, status = status.HTTP_200_OK)
                # token , _ = Token.objects.get_or_create(user=user)
                # user_type = "edari"

                # return Response({"status":True, "token":token.key, "user_type":user_type}, status=status.HTTP_200_OK)
                if user.edari.code_time.year == timezone.now().year and user.edari.code_time.month == timezone.now().month and user.edari.code_time.day == timezone.now().day and user.edari.code_time.hour == timezone.now().hour:
                    if user.edari.code_time.minute == timezone.now().minute:
                        remain = 60 -  (timezone.now().second - user.edari.code_time.second)
                        return Response({"status":False, 'error':'130', 'remain':remain }, status=status.HTTP_200_OK)
                    elif (timezone.now().minute - user.edari.code_time.minute) == 1 and  (timezone.now().second < user.edari.code_time.second):
                        remain = 60 - (timezone.now().second + 60 - user.edari.code_time.second)
                        return Response({"status":False, 'error':'130', 'remain':remain }, status=status.HTTP_200_OK)
                code = randint(100000 , 999999)
                # dic['data']['code'] = code
                user.edari.code = code
                user.edari.code_time = timezone.now()
                user.edari.save()
                return Response({"status":True, 'username':user.username, 'code':code}, status=status.HTTP_200_OK)
            except:
                pass
            try:
                user = Tegari.objects.get(phone_number = serializer.data["phone_number"]).user
                # userr = authenticate(request=request, username=user.username, password=serializer.data['password'])
                # if not userr:
                #     dic = { "status":False , "error" : "121"    }
                #     return Response(dic, status = status.HTTP_200_OK)
                # token , _ = Token.objects.get_or_create(user=user)
                # user_type = "tegari"
                #
                # return Response({"status":True, "token":token.key, "user_type":user_type}, status=status.HTTP_200_OK)
                if user.tegari.code_time.year == timezone.now().year and user.tegari.code_time.month == timezone.now().month and user.tegari.code_time.day == timezone.now().day and user.tegari.code_time.hour == timezone.now().hour:
                    if user.tegari.code_time.minute == timezone.now().minute:
                        remain = 60 -  (timezone.now().second - user.tegari.code_time.second)
                        return Response({"status":False, 'error':'130', 'remain':remain }, status=status.HTTP_200_OK)
                    elif (timezone.now().minute - user.tegari.code_time.minute) == 1 and  (timezone.now().second < user.tegari.code_time.second):
                        remain = 60 - (timezone.now().second + 60 - user.tegari.code_time.second)
                        return Response({"status":False, 'error':'130', 'remain':remain }, status=status.HTTP_200_OK)
                code = randint(100000 , 999999)
                # dic['data']['code'] = code
                user.tegari.code = code
                user.tegari.code_time = timezone.now()
                user.tegari.save()
                return Response({"status":True, 'username':user.username, 'code':code}, status=status.HTTP_200_OK)
            except:
                pass

            dic = { "status":False , "error" : "131"    }
            return Response(dic, status = status.HTTP_200_OK)


        else:
            dic = { "status":False , "error" : "132"    }
            return Response(dic, status = status.HTTP_200_OK)




@permission_classes((AllowAny,))
class GetTokenPhone(APIView):

    def LessThanOneMinute(self, now, generated_time):
        if generated_time.year == now.year and generated_time.month == now.month and generated_time.day == now.day and generated_time.hour == now.hour:
            if generated_time.minute == now.minute:
                return True
            elif (now.minute - generated_time.minute) == 1  and  (now.second < generated_time.second):
                return True
        return False

    def post(self, request, format=None):
        serializer = GetTokenPhoneSerializer(data = request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(username = serializer.data["username"])
                try :
                    if str(user.khanevar.code) == str(serializer.data['code']) :
                        if not self.LessThanOneMinute(timezone.now(), user.khanevar.code_time):
                            return Response( {"status":False , "error" : "140"} , status = status.HTTP_200_OK)
                        token , _ = Token.objects.get_or_create(user=user)
                        return Response({"status":True, "token":token.key, "user_type":"khanevar"}, status=status.HTTP_200_OK)
                except:
                    pass
                try :
                    if user.edari.code == serializer.data['code'] :
                        if not self.LessThanOneMinute(timezone.now(), user.edari.code_time):
                            return Response( {"status":False , "error" : "140"} , status = status.HTTP_200_OK)
                        token , _ = Token.objects.get_or_create(user=user)
                        return Response({"status":True, "token":token.key, "user_type":"edari"}, status=status.HTTP_200_OK)
                except:
                    pass
                try :
                    if user.tegari.code == serializer.data['code'] :
                        if not self.LessThanOneMinute(timezone.now(), user.tegari.code_time):
                            return Response( {"status":False , "error" : "140"} , status = status.HTTP_200_OK)
                        token , _ = Token.objects.get_or_create(user=user)
                        return Response({"status":True, "token":token.key, "user_type":"tegari"}, status=status.HTTP_200_OK)
                except:
                    pass
            except:
                return Response( {"status":False , "error" : "112"} , status = status.HTTP_200_OK)
        else:
            return Response({"status":False , "error" : "114"}, status = status.HTTP_200_OK)


        return Response({"status":False , "error" : "113"}, status = status.HTTP_200_OK)


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
        # print(timezone.localtime(timezone.now()))
        serializer = GetTokenUsernameSerializer(data = request.data)
        if serializer.is_valid():
            userr = authenticate(request=request, username=serializer.data['username'], password=serializer.data['password'])
            if not userr:
                dic = { "status":False , "error" : "115"    }
                return Response(dic, status = status.HTTP_200_OK)
            token , _ = Token.objects.get_or_create(user=userr)
            if hasattr(userr , "khanevar"):
                user_type = "khanevar"
            elif hasattr(userr , "edari"):
                user_type = "edari"
            elif hasattr(userr , "tegari"):
                user_type = "tegari"
            return Response({"status":True, "token":token.key, "user_type":user_type}, status=status.HTTP_200_OK)
        else:
            dic = { "status":False , "error" : "114"    }
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
                    dic = { "status":False , "error" : "116"    }
                    return Response(dic, status = status.HTTP_200_OK)
                token , _ = Token.objects.get_or_create(user=user)
                if hasattr(userr , "khanevar"):
                    user_type = "khanevar"
                elif hasattr(userr , "edari"):
                    user_type = "edari"
                elif hasattr(userr , "tegari"):
                    user_type = "tegari"
                return Response({"status":True, "token":token.key, "user_type":user_type}, status=status.HTTP_200_OK)
            except:
                dic = { "status":False , "error" : "117"    }
                return Response(dic, status = status.HTTP_200_OK)
        else:
            dic = { "status":False , "error" : "118"    }
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
                user.khanevar.code_time = timezone.now()
                user.khanevar.save()
                return Response(dic, status=status.HTTP_201_CREATED)
            else:
                token, created = Token.objects.get_or_create(user=user)
                dic['data'].update({"token" : token.key ,"user_type":"khanevar"})
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
            try:
                dic['status'].extend(serializer.errors['phone_number'])
            except:
                pass
            dic2 = {'status':False , 'data': dic}
            # return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
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
                user.edari.code_time = timezone.now()
                user.edari.save()
                return Response(dic, status=status.HTTP_201_CREATED)
            else:
                token, created = Token.objects.get_or_create(user=user)
                dic['data'].update({"token" : token.key, "user_type":"edari"})
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

            try:
                dic['status'].extend(serializer.errors['phone_number'])
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
                user.tegari.code_time = timezone.now()
                user.tegari.save()
                return Response(dic, status=status.HTTP_201_CREATED)
            else:
                token, created = Token.objects.get_or_create(user=user)
                dic['data'].update({"token" : token.key, "user_type":"tegari"})
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

            try:
                dic['status'].extend(serializer.errors['phone_number'])
            except:
                pass
            dic2 = {'status':False , 'data': dic}
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(dic2 , status=status.HTTP_201_CREATED)
