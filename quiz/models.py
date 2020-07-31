from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    #pk 는 자동으로 생성
    question_text = models.CharField(max_length = 200)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # 질문을 삭제 했을 때 연관 항목을 어떻게 할지 설정 - 자동 삭제
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.choice_text

class Create_Quiz(models.Model):
    user_name=models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    selected_choices1 = models.CharField(max_length=100)
    selected_choices2 = models.CharField(max_length=100)
    selected_choices3 = models.CharField(max_length=100)
    selected_choices4 = models.CharField(max_length=100)
    selected_choices5 = models.CharField(max_length=100)
    selected_choices6 = models.CharField(max_length=100)
    selected_choices7 = models.CharField(max_length=100)
    selected_choices8 = models.CharField(max_length=100)
    selected_choices9 = models.CharField(max_length=100)
    selected_choices10 = models.CharField(max_length=100)