from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView,
)

from .views import RegistrationAPIView, UserView, UserRecords, UpdateBalance, UpdateRecord, UpdateClicks, LoginUser

urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', LoginUser.as_view()),
    path('user', UserView.as_view()),
    path('records', UserRecords.as_view()),
    path('updateuserbalance', UpdateBalance.as_view()),
    path('updateuserrecord', UpdateRecord.as_view()),
    path('updateuserclicksonmole', UpdateClicks.as_view()),
]