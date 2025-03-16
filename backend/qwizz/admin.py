from django.contrib import admin
from .models import *

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'author', 'question_count']

class AnswerInlineModel(admin.TabularInline):
  model = Answer
  fields = ['answer', 'is_correct']

class QuestionAdmin(admin.ModelAdmin):
  fields = ['question', 'quiz']
  list_display = ['id', 'question', 'quiz', 'created_at']
  inlines = [AnswerInlineModel]

class AnswerAdmin(admin.ModelAdmin):
  fields = ['question', 'answer', 'is_correct']
  list_display = ['id', 'question', 'answer', 'is_correct']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)