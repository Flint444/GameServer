from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import User


class RegistrationSuccessSerializer(serializers.ModelSerializer):
    message = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Данная почта уже зарегистрирована'})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'Данный пользователь уже зарегистрирован'})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'access', 'refresh', 'message')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}


class MessageResponseSerializer(serializers.Serializer):
    message = serializers.CharField()

class DetailResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()


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

