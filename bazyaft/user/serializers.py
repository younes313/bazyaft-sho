from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Khanevar , Edari , Tegari , Order


class GetTokenPhonenumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)


class GetTokenUsernameSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256)
    password = serializers.CharField(max_length=256)

class GetTokenEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=256)


class GetTokenPhoneSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256)
    code = serializers.IntegerField()

class UserKhanevarSerializer(serializers.ModelSerializer):
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
        # if not email or email=='':
        #     raise ValidationError("105")

        return data


class UserEdariTegariSerializer(serializers.ModelSerializer):
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

        return data




class KhanevarEmailRegisterSerializer(serializers.ModelSerializer):
    user = UserKhanevarSerializer()


    class Meta:
        model = Khanevar
        fields = '__all__'

    def validate_phone_number(self, value):
        if value != "":
            if Khanevar.objects.filter(phone_number=value).exists():
                raise ValidationError("120")
            if Edari.objects.filter(phone_number=value).exists():
                raise ValidationError("120")
            if Tegari.objects.filter(phone_number=value).exists():
                raise ValidationError("120")
        return value

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        khanevar = Khanevar.objects.create(user=user,**validated_data)
        return khanevar



class EdariEmailRegisterSerializer(serializers.ModelSerializer):
    user = UserEdariTegariSerializer()
    class Meta:
        model = Edari
        fields = '__all__'

    def validate_phone_number(self, value):
        if value != "":
            if Khanevar.objects.filter(phone_number=value).exists():
                raise ValidationError("120")
            if Edari.objects.filter(phone_number=value).exists():
                raise ValidationError("120")
            if Tegari.objects.filter(phone_number=value).exists():
                raise ValidationError("120")
        return value


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)

        edari = Edari.objects.create(user=user, **validated_data)
        return edari


class TegariEmailRegisterSerializer(serializers.ModelSerializer):
    user = UserEdariTegariSerializer()
    class Meta:
        model = Tegari
        fields = '__all__'


    def validate_phone_number(self, value):
        if value != "":
            if Khanevar.objects.filter(phone_number=value).exists():
                raise ValidationError("120")
            if Edari.objects.filter(phone_number=value).exists():
                raise ValidationError("120")
            if Tegari.objects.filter(phone_number=value).exists():
                raise ValidationError("120")
        return value


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)

        tegari = Tegari.objects.create(user=user, **validated_data)
        return tegari


class OrderSerializer(serializers.Serializer):
    # user = serializers.HiddenField( default=serializers.CurrentUserDefault() )
    # user = UserKhanevarSerializer()
    location_x = serializers.FloatField(default=0)
    location_y = serializers.FloatField(default=0)

    alminium = serializers.IntegerField(default=0)
    pet = serializers.IntegerField(default=0)
    khoshk = serializers.IntegerField(default=0)
    daftar_ketab = serializers.IntegerField(default=0)
    shishe = serializers.IntegerField(default=0)
    parche = serializers.IntegerField(default=0)
    naan = serializers.IntegerField(default=0)
    sayer = serializers.IntegerField(default=0)

    # kaghaz_moghava = serializers.IntegerField(default=0)
    # felezat = serializers.IntegerField(default=0)
    # ahan_sangin = serializers.IntegerField(default=0)
    # ahan_sabok = serializers.IntegerField(default=0)
    # zayeat_elecronic = serializers.IntegerField(default=0)

    # coins = serializers.IntegerField(default=0)
    # bag = serializers.IntegerField(default=0)
    # money = serializers.IntegerField(default=0)

    pelak_melak = serializers.CharField(default="")
    give_back_type =serializers.CharField(default="")




class OrderDriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
