from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import Khanevar , Edari , EdariType


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):

        return User.objects.create_user( **validated_data)

    def validate(self, data):
        email = data.get("email")

        if len(User.objects.filter(email=email)) > 0:
            raise ValidationError("102")
        if not email or email=='':
            raise ValidationError("105")

        return data



class KhanevarEmailRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()


    class Meta:
        model = Khanevar
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        khanevar = Khanevar.objects.create(user=user,**validated_data)
        return khanevar


    # def validate(self, data):
    #     email = data.get("email")
    #     password = data.get("password")
    #
    #
    #     # if
    #     if len(password) < 6:
    #         raise ValidationError("110")
    #
    #     else:
    #         return data


class EdariTypeAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = EdariType
        fields = '__all__'
