from django.conf.urls.static import static
from django.urls import path

from server import settings
from .views import ShowStore, ShowInventory, Buy

urlpatterns = [
    path('store', ShowStore.as_view()),
    path('inventory', ShowInventory.as_view()),
    path('buy', Buy.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
