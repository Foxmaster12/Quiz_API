from . import views

from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('get_quiz/', views.QuizListView.as_view()),
    url(r'^pass_quiz/(?P<name>[\w]+)/$', views.PassQuiz.as_view()),
    url(r'^pass_quiz/(?P<name>[\w]+)/anon/$', views.PassQuizAnon.as_view()),
    path('get_complited_quiz/', views.GetComplitedQuizes.as_view()),
    path('', views.GetStartPage.as_view(), )
]