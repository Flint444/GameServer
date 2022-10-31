from django.db import models

from users.models import User


# Create your models here.

class Achievements(models.Model):
    title = models.CharField(max_length=255, unique=True)
    prize = models.CharField(max_length=255)
    image = models.ImageField(upload_to = '')

    def __str__(self):
        return str(self.image)

class UserAchievements(models.Model):
    title = models.ForeignKey(Achievements, on_delete=models.CASCADE)
    nickname = nickname = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('title', 'nickname')