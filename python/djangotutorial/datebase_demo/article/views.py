from django.shortcuts import render,HttpResponse
from .models import User,Article

def article_test(request):
    # user=User(username='cgx',password='11111')
    # user.save()
    # artilce=Article(title='小米',content='xxx',author=user)
    # artilce.save()
    article=Article.objects.first()
    print(article.author.username)
    return HttpResponse('xxx')