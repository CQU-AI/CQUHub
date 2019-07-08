# -*- coding: utf-8 -*-
from django.db import models

from user.models import User_Info

from topic.models import Create_Topic


class Topic_Comment(models.Model):
    user = models.ForeignKey(User_Info, on_delete=models.CASCADE, verbose_name="评论用户")
    topic = models.ForeignKey(
        Create_Topic, on_delete=models.CASCADE, verbose_name="关联主题"
    )
    content = models.TextField(verbose_name="评论内容")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")

    class Meta:
        verbose_name = "用户对主题进行评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


# 发帖回帖组：Topic_Reply Model，对帖子进行回复。两个外键：用户，关联评论


class Topic_Reply(models.Model):
    user = models.ForeignKey(
        User_Info, on_delete=models.CASCADE, verbose_name="进行回复操作的用户"
    )
    comment = models.ForeignKey(
        Topic_Comment, on_delete=models.CASCADE, verbose_name="关联评论"
    )
    content = models.TextField(verbose_name="评论内容")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")

    class Meta:
        verbose_name = "对特定评论进行回复"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


# 发帖回帖组: class Topic_Reply END
