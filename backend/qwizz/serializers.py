from rest_framework import serializers
from .models import *

class QuizSerializer(serializers.ModelSerializer):
  qustion_count = serializers.SerializerMethodField('get_question_count')

  class Meta:
    model = Quiz
    fields = [
      'id',
      'tittle',
      'created_at',
      'updated_at',
      'qustion_count'
    ]

  def get_question_count(self, obj):
    return obj.question_count


class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = [
      'id',
      'answer',
      'is_correct'
    ]


class QuestionSerializer(serializers.ModelSerializer):
  quiz = QuizSerializer(read_only=True)
  answers = AnswerSerializer(many=True, read_only=True)

  class Meta:
    model = Question
    fields = [
      'id',
      'quiz',
      'question',
      'answers'
    ]
  

  def create(self, validated_data):
    answers = validated_data.pop('answers', [])
    question = Question.objects.create(**validated_data)
    for answer in answers:
      Answer.objects.create(question=question, **answer)
    return question


  def update(self, instance, validated_data):
    instance.question = validated_data.get('question', instance.question)
    answers = validated_data.pop('answers', [])           # Update the associated answers
    instance.answers.all().delete()                       # Delete the old answers
    for answer in answers:
      Answer.objects.update_or_create(question=instance, **answer)
    instance.save()
    return instance