from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'hello.html',{'message':'hello,wold'})
    # 1，传参数 2，模板名称 3，内容