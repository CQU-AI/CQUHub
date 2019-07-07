from django.contrib import admin
from django.urls import path, include
from .views import Login_View, Register_Voew, logout_view, Info_Profile, Info_Reply, Revise_View

app_name = 'user'
urlpatterns = [
    path('login/', Login_View.as_view(), name='login'),
    path('register/', Register_Voew.as_view(), name='register'),
    path('revise/', Revise_View.as_view(), name='revise'),
    path('logout/', logout_view, name='logout'),
    path('<str:username1>/', Info_Profile.as_view(), name='infoprofile'),
    path('reply/<str:username1>/', Info_Reply.as_view(), name='inforeply'),
]
