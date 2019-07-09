from django.contrib import admin
from django.urls import path, include
from .views import Quiz_View

app_name = 'Addon'
urlpatterns = [
    path('quiz_hello', Quiz_View.loadHello, name='quiz_hello'),
    path('quiz', Quiz_View.loadQuiz, name='quiz'),
    path('quiz_next', Quiz_View.loadNextQuiz, name='quiz'),
    path('quiz_over/<str:questionNum>/<str:score>', Quiz_View.loadOver, name='quiz'),
    path('quiz/<str:rightAns>/<str:optChoosen>/<str:timeLeft>', Quiz_View.judgeAns, name='quiz'),
]