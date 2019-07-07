# -*- coding: utf-8 -*-
# from django.contrib import admin
from django.urls import path, include

from .views import Comment_View, deleteComment

app_name = "operation"
urlpatterns = [
    path("comment/<int:content_id>", Comment_View.as_view(), name="comment_url"),
    path(
        "deleteComment/<int:content_id>/<int:comment_id>",
        deleteComment.as_view(),
        name="deleteComment",
    ),
]
