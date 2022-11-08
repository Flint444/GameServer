from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from users.serializer import UserSerializer
from .serializer import StoreSerializer, InventorySerializer
from .models import Store, Inventory
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ShowStore(GenericAPIView):
    """Отобразить магазин"""
    permission_classes = (IsAuthenticated,)

    serializer_class = StoreSerializer
    def get(self, request):
        user = Store.objects.order_by('title')

        selializer = StoreSerializer(user, many=True)

        return Response(selializer.data)

class ShowInventory(GenericAPIView):
    """Отобразить инвентарь"""
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user

        user_inventory = Inventory.objects.filter(nickname_id = user.id)

        selializer = InventorySerializer(user_inventory, many=True)

        return Response(selializer.data)

class Buy(GenericAPIView):
    """Покупка предмета в магазине"""
    permission_classes = (IsAuthenticated,)

    serializer_class = InventorySerializer
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
