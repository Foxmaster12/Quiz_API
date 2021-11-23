from . import views

from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('get_quiz/', views.QuizListView.as_view(), name='quiz_getter'),
    url(r'^pass_quiz/(?P<name>[\w]+)/$', views.PassQuiz.as_view(), name='quiz_passer'),
    url(r'^pass_quiz/(?P<name>[\w]+)/anon/$', views.PassQuizAnon.as_view(), name='anon_quiz_passer'),
    path('get_complited_quiz/', views.GetComplitedQuizes.as_view(), name='complete_quiz_getter'),
    path('', views.GetStartPage.as_view(), name='start_page')
]