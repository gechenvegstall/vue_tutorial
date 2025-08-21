from django.shortcuts import render
from pymysql import connect


def index(request):
    return render(request,"index.html")

def info(request):
    username="CGX"
    return render(request,"home.html",context={'name':username,'age':1000})

def if_view(request):
    age=18
    return render(request,'if.html',context={'age':age})

def for_view(request):
    user=[{'name':'admin','password':123456},
          {'name':'admin','password':123456},
          ]

    dict1={'name':"cgx",
          'age':20,
          'phone':1111111}
    context={'users':user,'dict':dict1}
    return  render(request,'for.html',context=context)

def with_view(request):
    context={
        'users':[
            {'name': 'admin', 'password': 123456},
            {'name': 'admin', 'password': 123456},
        ]
    }
    return render(request,'with.html',context=context)