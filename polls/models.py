#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import  datetime
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

#使交互输出的时候不是显示对象名字,而是显示question_text,使对象显的更加直观
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() -datetime.timedelta(days=1)




class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text