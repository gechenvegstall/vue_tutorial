from django.urls import path
from . import views

app_name='blog_auth'

urlpatterns=[
    path('login',views.login,),
    path('register',views.register),
]