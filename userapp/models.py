# Create your models here.
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUser(AbstractUser):
    # 添加你需要的自定义字段，例如用户头像、个人信息等
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png', null=True, blank=True)
    bio = models.TextField(blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username
