from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
# ####################
from .forms import DriverSignupForm , UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
######################

from user.models import Order
from user.serializers import OrderSerializer
from user.serializers import OrderDriverSerializer



@permission_classes((permissions.AllowAny,))
class GetToken(APIView):

    def post(self, request, format=None):
        try:
            username = request.data['phone_number']
            password = request.data['national_code']
        except:
            dic = { "status":False , "error" : "170"  }
            return Response(dic, status = status.HTTP_200_OK) #incorrect input

        user = authenticate(request=request, username=username, password=password)
        if not (user and hasattr(user, 'drivermodel') ):
            dic = { "status":False , "error" : "171"    }   # incorrect phone_number or national_code
            return Response(dic, status = status.HTTP_200_OK)
        token , _ = Token.objects.get_or_create(user=user)
        return Response({"status":True, "token":token.key, }, status=status.HTTP_200_OK)




###############################
def index(request):
    return render(request,'driver/index.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def special(request):
    return HttpResponse("You are logged in !")

@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = DriverSignupForm(data=request.POST)
        if profile_form.is_valid() and user_form.is_valid() :
            user = user_form.save(commit=False)
            user.username = profile_form.cleaned_data['phone_number']
            user.set_password(profile_form.cleaned_data['national_code'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = DriverSignupForm()
    return render(request,'driver/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and user.is_superuser:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Only superuser can login")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'driver/login.html', {})


###############################3



class GetMyAcceptedOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        serializer = OrderDriverSerializer(Order.objects.filter(driver=request.user) , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)




class AcceptOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        if len(Order.objects.filter(driver=request.user)) >= 20:
            return Response( {"status":False, "error":"167" }  ,status=status.HTTP_200_OK)
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
                if request.user.drivermodel.coins > 5 :
                    request.user.drivermodel.coins -= 5
                else:
                    request.user.drivermodel.coins = 0
                request.user.drivermodel.save()
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
