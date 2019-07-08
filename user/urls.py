# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import (
    Login_View,
    Register_View,
    logout_view,
    Info_Profile,
    Info_Reply,
    upload,
    Info_page,
    Go_info_page,
    Info_View,
    Verify_View,
)

app_name = "user"
urlpatterns = [
    path("login/", Login_View.as_view(), name="login"),
    path("register/", Register_View.as_view(), name="register"),
    path("info/<str:username>", Info_View.as_view(), name="info"),
    path("logout/", logout_view, name="logout"),
    path("verify/", Verify_View.as_view(), name="verify"),
    path("info/go/<str:username1>/", Go_info_page, name="info_Pagego"),
    path("reply/<str:username1>/", Info_Reply.as_view(), name="inforeply"),
    url(r"^upload", upload),
    path("<str:username1>/<int:page_id>/", Info_page, name="infoPage"),
    path("<str:username1>/", Info_Profile.as_view(), name="infoprofile"),
]
