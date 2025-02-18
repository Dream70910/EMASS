from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Instruction(models.Model):
    content = models.CharField(max_length=1000)

class BcColor(models.Model):
    color = models.CharField(max_length=100, default='rgb(254, 222, 117)')


