from django.contrib import admin
from .models import *


class TestStack(admin.TabularInline):
    model = Quiz.questions.through
    extra = 1


class Connection(admin.TabularInline):
    model = Question.answers.through
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end')
    readonly_fields = ('start', )
    inlines = [TestStack]
    exclude = ('questions', )


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question_type', 'question_text')
    inlines = [Connection]
    exclude = ('answers', )


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('answer', )


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answers, AnswersAdmin)

