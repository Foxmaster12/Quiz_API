from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from .serializers import QuizListSerializer
from .models import *


class GetStartPage(APIView):
    def get(self, request):
        return render(request, 'main/base.html')


class QuizListView(APIView):
    def get(self, request):
        quiz = Quiz.objects.filter(end__gte=datetime.now())
        return render(request, 'main/content.html', {'quiz': quiz})


class PassQuizAnon(APIView):

    def get(self, request, name):
        quiz = Quiz.objects.get(name=name)
        questions = Question.objects.filter(quiz__name=name)
        results = []
        for item in questions:
            results.append({'question': item, 'answers': Answers.objects.filter(question__pk=item.pk)})
        return render(request, 'main/quiz_form.html', {'quiz': quiz, 'results': results})

    def post(self, request, name):

        return render(request, 'main/success.html')


class PassQuiz(LoginRequiredMixin, PassQuizAnon):

    def post(self, request, name):
        user = request.user
        user1 = User.objects.create(user_id=user.id)
        passed_quiz = Passed_quiz.objects.create(quiz_name=name)
        for item in request.data:
            if item != 'csrfmiddlewaretoken':
                if len(request.POST.getlist(item)) >= 1:
                    for elem in request.POST.getlist(item):
                        answer = UserAnswers.objects.create(question=item,
                                                            text=Question.objects.get(pk=item).question_text, answer=elem)
                        passed_quiz.content.add(answer)
        user1.passed_quizes.add(passed_quiz)
        user1.save()
        return render(request, 'main/success.html')


class GetComplitedQuizes(LoginRequiredMixin, APIView):
    def get(self, request):
        identifier = request.user.id
        quizes = Passed_quiz.objects.filter(user__user_id=identifier)
        content = []
        for item in quizes:
            data = {}
            data[item.quiz_name] = UserAnswers.objects.filter(passed_quiz__pk=item.pk)
            content.append(data)
        if len(quizes) == 0:
            return render(request, 'main/empty_list.html')

        return render(request, 'main/quiz_list.html', {'content': content})

    def post(self, request):
        pass





