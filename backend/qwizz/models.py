from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField

# Create your models here.
class Quiz(models.Model):
  title = models.CharField(_('Title'),max_length=255, unique=True)
  author = models.CharField(_('Author'),max_length=100)
  slug = AutoSlugField(populate_from='title', unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  @property
  def question_count(self):
    return self.questions.count()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = _('Quiz')
    verbose_name_plural = _('Quizzes')
    ordering = ['id']

class Question(models.Model):
  quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
  question = models.CharField(_('Question'),max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = _('Question')
    verbose_name_plural = _('Questions')
    ordering = ['id']
  
  def __str__(self):
    return self.question


class Answer(models.Model):
  question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
  answer = models.CharField(_('Answer'),max_length=255, null=True, blank=True)
  is_correct = models.BooleanField(_('Is Correct'), default=False, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = _('Answer')
    verbose_name_plural = _('Answers')
    ordering = ['id']
  
  def __str__(self):
    return self.answer
