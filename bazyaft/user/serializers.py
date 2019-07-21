from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import Khanevar


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user




class KhanevarEmailRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()


    class Meta:
        model = Khanevar
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        userr = User.objects.create(**user_data)
        khanevar = Khanevar.objects.create(user=userr,**validated_data)
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
