# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User_Info(AbstractUser):
    nickname = models.CharField(max_length=20, verbose_name="昵称", default="")
    studentID = models.CharField(max_length=20, verbose_name="学号", default="")
    avatarID = models.CharField(max_length=50, default="defaultAvatar.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
