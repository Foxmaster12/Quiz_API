from rest_framework import serializers

from .models import *


class QuizListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("name", )

