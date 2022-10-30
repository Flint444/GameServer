import uuid

from rest_framework.views import APIView

from .models import User
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializer import RegistrationSerializer, UserSerializer, RecordSerializer


# Create your views here.
class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "Пользователь успешно создан",
                "User": serializer.data}, status = status.HTTP_201_CREATED
            )

        return Response({"Errors": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(data=serializer.data)


class UserRecords(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        users = User.objects.order_by('-record')
        serializer = RecordSerializer(users, many=True)
        return Response(data=serializer.data)

class UpdateBalance(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def put(self, request):
        user = request.user
        user.balance = request.data["balance"]
        user.save()
        return Response(data={'message': 'Баланс успешно изменён'})

class UpdateRecord(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def put(self, request):
        user = request.user
        user.record = request.data["record"]
        user.save()
        return Response(data={'message': 'Рекорд успешно изменён'})

class UpdateClicks(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def put(self, request):
        user = request.user
        user.clicks_on_mole = request.data["clicks_on_mole"]
        user.save()
        return Response(data={'message': 'Кол-во кликов по кроту успешно изменено'})