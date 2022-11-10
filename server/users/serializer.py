from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=50, min_length=4)
    email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=50, write_only=True)
    Message = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['Message','username', 'email', 'password']

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)

        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': ('email already exist')})
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError({'username': ('nickname already exist')})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

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

