from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegistrationAPIView, UserView, UserRecords, UpdateBalance, UpdateRecord, UpdateClicks, \
    MyObtainTokenPairView

urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', MyObtainTokenPairView.as_view()),
    #path('logout', UserLogout.as_view()),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('user', UserView.as_view()),
    path('records', UserRecords.as_view()),
    path('updateuserbalance', UpdateBalance.as_view()),
    path('updateuserrecord', UpdateRecord.as_view()),
    path('updateuserclicksonmole', UpdateClicks.as_view()),
]