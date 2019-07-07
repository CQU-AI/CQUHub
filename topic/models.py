# -*- coding: utf-8 -*-
from django.db import models

from user.models import User_Info


# from  operation.models import Topic_Comment
# Create your models here.


# 外键
class Create_Topic(models.Model):
    user = models.ForeignKey(User_Info, on_delete=models.CASCADE, verbose_name='发帖人')

    title = models.CharField(max_length=200, verbose_name='标题')

    content = models.TextField(verbose_name='编写内容')

    pub_time = models.DateTimeField(auto_now_add=True)

    read_nums = models.IntegerField(default=0, verbose_name=u"阅读次数")

    last_time = models.DateTimeField(auto_now=True)

    theme = (
        ('那个谁，我想对你说', '那个谁，我想对你说'),
        ('动手动脚找东西', '动手动脚找东西'),
        ('CQU公告', 'CQU公告'),
        ('CQU身边事', 'CQU身边事'),
        ('技术栏目', '技术栏目'),
        ('文学交流', '文学交流'),
        # ('comments', '论坛公告'),
    )

    xuanze = (
        ('不匿名', '不匿名'),
        ('匿名', '匿名'),
    )

    node = models.CharField(max_length=50, choices=theme, verbose_name='主题结点')
    ifAnony = models.CharField(max_length=50, choices=xuanze, verbose_name='是否匿名')
    top = models.CharField(max_length=5, verbose_name="是否置顶")
    notice = models.CharField(max_length=5, verbose_name='公告')

    class Meta:
        verbose_name = '发布主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
