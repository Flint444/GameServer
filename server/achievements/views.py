from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import AchievementsSerializer, GetUserAchievements
from .models import Achievements, UserAchievements
from rest_framework.permissions import IsAuthenticated

class ShowAchievements(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = Achievements.objects.all()

        selializer = AchievementsSerializer(user, many=True)

        return Response(selializer.data)

class UserGetAchievements(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = UserAchievements.objects.all()

        selializer = GetUserAchievements(user, many=True)

        return Response(selializer.data)

class GetAchievements(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = GetUserAchievements(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

