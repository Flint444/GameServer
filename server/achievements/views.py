from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializer import UnAuthenticated
from .models import Achievements, UserAchievements
from .serializer import AchievementsSerializer, GetUserAchievements


class ShowAchievements(GenericAPIView):
    """Показать все достижения"""
    permission_classes = (IsAuthenticated,)
    serializer_class = AchievementsSerializer

    @extend_schema(responses={201: AchievementsSerializer,
                              401: UnAuthenticated})
    def get(self, request):
        user = Achievements.objects.all()

        selializer = AchievementsSerializer(user, many=True)

        return Response(selializer.data)

class UserGetAchievements(GenericAPIView):
    """Показать достижения конкретного пользователя"""
    permission_classes = (IsAuthenticated,)
    serializer_class = GetUserAchievements

    @extend_schema(responses={201: GetUserAchievements,
                              401: UnAuthenticated})
    def get(self, request):
        user = request.user

        user_achievments = UserAchievements.objects.filter(nickname_id=user.id)

        selializer = GetUserAchievements(user_achievments, many=True)

        return Response(selializer.data)

class GetAchievements(GenericAPIView):
    """Получение достижения по достижению какого-то результата в игре"""
    permission_classes = (IsAuthenticated,)
    serializer_class = GetUserAchievements

    @extend_schema(responses={201: GetUserAchievements,
                              401: UnAuthenticated})
    def post(self, request):
        serializer = GetUserAchievements(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

