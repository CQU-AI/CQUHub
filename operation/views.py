# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Topic_Comment
from user.models import User_Info
from topic.models import Create_Topic
from topic.forms import Comment_Forms


class Comment_View(View):
    def post(self, request, content_id):
        comment_theme = Create_Topic.objects.get(id=content_id)

        forms = Comment_Forms(request.POST)

        if forms.is_valid():
            comment_content = forms.cleaned_data["content_raw"]
            comment_content = comment_content.replace("<", " &lt;")
            comment_content = comment_content.replace(">", "&gt;")
            comment = Topic_Comment()
            comment.topic = comment_theme
            comment.user = User_Info.objects.get(username=request.user.username)
            comment.content = comment_content
            comment.save()
            return redirect(to="topic:topic_content1", content_id=content_id, page_id=1)

        return redirect(to="topic:topic_content1", content_id=content_id, page_id=1)


class deleteComment(View):
    def get(self, request, content_id, comment_id):
        commentTmp = Topic_Comment.objects.get(id=comment_id)
        commentTmp.delete()
        return redirect(to="topic:topic_content1", content_id=content_id, page_id=1)
