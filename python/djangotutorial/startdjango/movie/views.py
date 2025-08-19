from django.shortcuts import render,HttpResponse

def movie_list(request):
    return HttpResponse("电影列表")

def movie_list_query(request,name):
    return HttpResponse (f"您要看到的是电影：{name}")