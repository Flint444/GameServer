import uuid

from rest_framework.views import APIView

from .models import User
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response

from .serializer import RegistrationSerializer, UserSerializer


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

    def get(self, request):
        pass


