from django.urls import path
from . import views

app_name = 'blog_auth'

urlpatterns = [
    path('login', views.blog_login, name='login'),
    path('login', views.blog_logout, name='logout'),
    path('register', views.register, name='register'),
    path('email', views.send_email_captcha, name='email')
]
