from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import Khanevar


class KhanevarEmailRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

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
