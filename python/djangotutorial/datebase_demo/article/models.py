from django.db import models

class User(models.Model):
     username=models.CharField(max_length=20)
     password=models.CharField(max_length=100)

class Article(models.Model):
     title=models.CharField(max_length=100)
     content=models.TextField()
     # 外键
     author = models.ForeignKey("User", on_delete=models.CASCADE)