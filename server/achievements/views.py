from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Achievements, UserAchievements
from .serializer import AchievementsSerializer, GetUserAchievements


class ShowAchievements(GenericAPIView):
    """Показать все достижения"""
    permission_classes = (IsAuthenticated,)

    serializer_class = AchievementsSerializer
    def get(self, request):
        user = Achievements.objects.all()

        selializer = AchievementsSerializer(user, many=True)

        return Response(selializer.data)

class UserGetAchievements(GenericAPIView):
    """Показать достижения пользователя"""
    permission_classes = (IsAuthenticated,)
    serializer_class = GetUserAchievements

    def get(self, request):
        user = request.user

        user_achievments = UserAchievements.objects.filter(nickname_id=user.id)

        selializer = GetUserAchievements(user_achievments, many=True)

        return Response(selializer.data)

class GetAchievements(GenericAPIView):
    """Получение достижения"""
    permission_classes = (IsAuthenticated,)

    serializer_class = GetUserAchievements
    def post(self, request):
        serializer = GetUserAchievements(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

