from rest_framework import serializers
# from rest_framework.exceptions import ValidationError
# from django.contrib.auth.models import User
# from user.models import Khanevar , Edari , Tegari , Order

from user.models import Order , OrderHistory


class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderHistory
        fields = "__all__"


class OrderHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"



class ConfirmOrEditOrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    status_driver = serializers.CharField(default="")
    alminium = serializers.IntegerField(default=0)
    pet = serializers.IntegerField(default=0)
    khoshk = serializers.IntegerField(default=0)
    daftar_ketab = serializers.IntegerField(default=0)
    shishe = serializers.IntegerField(default=0)
    parche = serializers.IntegerField(default=0)
    naan = serializers.IntegerField(default=0)
    sayer = serializers.IntegerField(default=0)
