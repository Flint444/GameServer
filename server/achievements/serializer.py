from rest_framework import serializers
from .models import Achievements, UserAchievements


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = '__all__'

class GetUserAchievements(serializers.ModelSerializer):
    class Meta:
        model = UserAchievements
        fields = ['title','nickname']