from django.db import models

from django.contrib.auth.models import AbstractUser

class  User_Info(AbstractUser):
    nick_name = models.CharField(max_length=20,verbose_name='昵称',default='')
    studentID = models.CharField(max_length=200, verbose_name='学号')
    avatar = models.ImageField(upload_to='image/%Y/%m',default='image/github.png',verbose_name='用户头像',max_length=200)

    class  Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def  __str__(self):
        return   self.username
