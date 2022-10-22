from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import AchievementsSerializer
from .models import Achievements
from rest_framework.permissions import IsAuthenticated

class ShowAchievements(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = Achievements.objects.all()

        selializer = AchievementsSerializer(user, many=True)

        return Response(selializer.data)