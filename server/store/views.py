from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializer import UserSerializer, UnAuthenticated
from .models import Store, Inventory
from .serializer import StoreSerializer, InventorySerializer


# Create your views here.

class ShowStore(GenericAPIView):
    """Отобразить магазин"""
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer

    @extend_schema(responses={201: StoreSerializer,
                              401: UnAuthenticated})
    def get(self, request):
        user = Store.objects.order_by('title')

        selializer = StoreSerializer(user, many=True)

        return Response(selializer.data)

class ShowInventory(GenericAPIView):
    """Отобразить инвентарь"""
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    @extend_schema(responses={201: InventorySerializer,
                              401: UnAuthenticated})
    def get(self, request):
        user = request.user

        user_inventory = Inventory.objects.filter(nickname_id = user.id)

        selializer = InventorySerializer(user_inventory, many=True)

        return Response(selializer.data)

class Buy(GenericAPIView):
    """Покупка предмета в магазине"""
    permission_classes = (IsAuthenticated,)
    serializer_class = InventorySerializer

    @extend_schema(responses={201: InventorySerializer,
                              401: UnAuthenticated})
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
