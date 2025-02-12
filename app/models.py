from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
