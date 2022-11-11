from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User


class RegistrationSuccessSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, min_length=4)
    email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=50, write_only=True)
    message = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Данная почта уже зарегистрирована')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('Данная пользователь уже зарегистрирован')})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'access', 'refresh', 'message']


class MessageResponseSerializer(serializers.Serializer):
    message = serializers.CharField()

class DetailResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'balance', 'record', 'clicks_on_mole']


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'record']

class ChangeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['record']

class ChangeClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['clicks_on_mole']

class ChangeBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['balance']

