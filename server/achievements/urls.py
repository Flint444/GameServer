from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

from server import settings
from .views import ShowAchievements, GetAchievements, UserGetAchievements

urlpatterns = [
    path('achievements', ShowAchievements.as_view()),
    path('getachievements', GetAchievements.as_view()),
    path('usersgetachievements', UserGetAchievements.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
