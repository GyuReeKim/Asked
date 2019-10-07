from django.db import models

# Create your models here.
class Question(models.Model):
    content = models.TextField()

class Answer(models.Model):
    content = models.CharField(max_length=100)
    # 값을 가져오기 위해 외래키를 사용한다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)