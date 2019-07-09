from django.db import models

# Create your models here.
# 定义实体类，映射到数据库中的app_Quiz表
class Quiz(models.Model):
    # 属性映射成表中的字段
    quizno = models.AutoField(primary_key=True) # 主键自动增长
    question = models.CharField(max_length=100,default='') # 问题，字符型，最大长度100
    optionA = models.CharField(max_length=80,default='')   #选项A
    optionB = models.CharField(max_length=80,default='')   #选项B
    optionC = models.CharField(max_length=80,default='')   #选项C
    optionD = models.CharField(max_length=80,default='')   #选项D
    rightAns = models.CharField(max_length=5,default='')   #正确选项

    class Meta:
        verbose_name = 'Addon_quiz'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question

class Player(models.Model):
    # 属性映射成表中的字段
    palyerno = models.AutoField(primary_key=True) # 主键自动增长
    userName = models.CharField(max_length=50,default='')   #用户名
    score = models.IntegerField(default=0)  #得分

    class Meta:
        verbose_name = 'Addon_quiz'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.score