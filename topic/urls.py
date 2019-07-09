# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include
from .views import (
    Go_theme_Page,
    Theme1_View,
    PubTopic_View,
    Index_View,
    default_index,
    Topic_Content_View,
    Topic_Content_View1,
    Go_Page,
    Go_Comment_Page,
    Theme2_View,
    delete_topic,
    search1,
    search2,
    Go_Search_Page,
    topicmodify,
    modifypage
)

app_name = "topic"
urlpatterns = [
    path("", default_index, name="index"),
    path("create/<str:username>/", PubTopic_View.as_view(), name="create_topic"),
    path("page/<int:page_id>/", Index_View.as_view(), name="page"),
    path("content/<int:content_id>/", Topic_Content_View.as_view(), name="topic_content"),
    path("content/<int:content_id>/<int:page_id>", Topic_Content_View1.as_view(), name="topic_content1"),
    path("theme/<int:theme_id>/", Theme1_View.as_view(), name="theme1"),
    path("theme/<int:theme_id>/<int:page_id>/", Theme2_View.as_view(), name="theme1"),
    path("page/go/", Go_Page, name="go"),
    path("theme/go/<int:theme_id>/", Go_theme_Page, name="theme_change"),
    # path('info/go/<str:username1>/',Go_info_page, name='info_Pagego'),
    path("search/<int:page_id>/", search1, name="search1"),
    path("search/<str:keywords>/<int:page_id>/", search2, name="search2"),
    path("delete/<str:title1>/", delete_topic.as_view(), name="delete_topic"),
    path("search/go/", Go_Search_Page, name="go_search_page"),
    
    path("modifypage/<int:content_id>/", modifypage.as_view(), name="modifypage"),
    path("topicmodify/<int:content_id>/", topicmodify.as_view(), name="topicmodify"),
    path("comment/go/<int:content_id>", Go_Comment_Page.as_view(), name="go_comment"),
]
