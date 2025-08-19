from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def info(request):
    username="CGX"
    return render(request,"home.html",context={'name':username,'age':1000})