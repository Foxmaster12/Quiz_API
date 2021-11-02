from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime


class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Answers(models.Model):
    answer = models.CharField(max_length=100)

    def __str__(self):
        return str(self.answer)

    class Meta:
        verbose_name_plural = 'Answers'


class Question(models.Model):
    number = models.IntegerField()
    question_type = NameField(max_length=100)
    question_text = models.CharField(max_length=500)
    answers = models.ManyToManyField(Answers)

    def __str__(self):
        return str(self.question_type)

    def clean(self):
        if str(self.question_type).lower() not in ['one text answer', 'one choice', 'several choices']:
            raise ValidationError('Incorrect type of question, acceptable types: one text answer, one choice, '
                                  'several choices')
        if self.number <= 0:
            raise ValidationError('Incorrect number of question, number must be more than zero')


class Quiz(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)
    questions = models.ManyToManyField(Question)

    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return str(self.name)

    def clean(self):
        if self.start >= self.end:
            raise ValidationError("Incorrect date of ending")


class UserAnswers(models.Model):
    question = models.CharField(max_length=500)
    text = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)


class Passed_quiz(models.Model):
    quiz_name = models.CharField(max_length=100)
    content = models.ManyToManyField(UserAnswers)


class User(models.Model):
    user_id = models.IntegerField()
    passed_quizes = models.ManyToManyField(Passed_quiz)
