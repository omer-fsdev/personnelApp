from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="site_user"
    )
    avatar = models.ImageField(upload_to="pictures", default="avatar.png")
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"
