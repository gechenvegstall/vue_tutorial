from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=100,null=False)
    author=models.CharField(max_length=20,null=False)
    put_time=models.DateTimeField(auto_now_add=True)
    price=models.FloatField(default=0)